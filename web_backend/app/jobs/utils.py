from elasticsearch_dsl import Q, Search
from src.utils import get_elasticsearch_client


def search_jobs(query=None):
    if not query:
        es = get_elasticsearch_client()
        resp = es.search(index='job_index', query={"match_all": {}}, size = 10000)
        return [result['_source'] for result in resp['hits']['hits']]
        
    
    search_query = query.get("search_query", "")
    job_level_filter = query.get("job_level", "")
    company_type_filter = query.get("company_type", "")
    working_model_filter = query.get("working_model", "")
    
    
    words = search_query.split(" ")
    
    def get_fuzzy(field_name: str, value: str):
        return {
            "fuzzy": {
                field_name: {
                    "value": value,
                    "fuzziness":"AUTO"
                } 
            }
        }

    job_title_clauses = [
        {
            "span_multi": {
                "match": get_fuzzy("title", word)
            }
        } for word in words
    ]
    
    match_job_title = {
        "span_near": {
            "clauses": job_title_clauses,
            "slop": "5",
            "in_order": False
        }  
    }
    
    company_name_clauses = [
        {
            "span_multi": {
                "match": get_fuzzy("company.name", word)
            }
        } for word in words
    ]

    match_company_name = {
        "span_near": {
            "clauses": company_name_clauses,
            "slop": "5",
            "in_order": False
        }  
    }
    
    search_query = [match_job_title, match_company_name]
    
    match_each_word = [
        {
            "multi_match": {
                "query": word,
                "fields": [ "skills.name", "company.type", "advantage", "benefit", "description", "qualification"],
                "fuzziness": "AUTO" 
            }
        } for word in words
    ]
    
    search_query += match_each_word
    
    
    filter_query = []
    
    if job_level_filter:
        filter_query.append({
            "match": {
                "levels.level": job_level_filter
            }
        })
    
    if company_type_filter:
        filter_query.append({
            "match": {
                "company.type": company_type_filter
            }
        })

    if working_model_filter:
        filter_query.append({
            "match": {
                "working_model": working_model_filter
            }
        })
    
    
    
    payload = {
        "bool": {
            "should": search_query,
            "must": filter_query
        }
    }

    es = get_elasticsearch_client()
    resp = es.search(index='job_index', query=payload, size = 10000)

    return [result['_source'] for result in resp['hits']['hits']]
