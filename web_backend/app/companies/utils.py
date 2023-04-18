from src.utils import get_elasticsearch_client

def search_companies(query=None):
    if not query:
        es = get_elasticsearch_client()
        resp = es.search(index='company_index', query={"match_all": {}}, size = 10000)
        return [result['_source'] for result in resp['hits']['hits']]
    
    search_query = query.get("search_query", "")
    company_type_filter = query.get("company_type", "")

    words = search_query.split(" ")
    words = [word.lower() for word in words]
    words = [word.capitalize() for word in words]
    
    
    def get_fuzzy(field_name: str, value: str):
        return {
            "fuzzy": {
                field_name: {
                    "value": value,
                    "fuzziness":"2"
                } 
            }
        }
        
    company_name_clauses = [
        {
            "span_multi": {
                "match": get_fuzzy("name", word)
            }
        } for word in words
    ]
    
    match_company_name = {
        "span_near": {
            "clauses": company_name_clauses,
            "slop": 0,
            "in_order": False
        }  
    }
    
    search_query = [match_company_name]
    
    filter_query = []
    
    if company_type_filter:
        filter_query.append({
            "match": {
                "type": company_type_filter
            }
        })
        
        
    match_skill = [
        {
            "multi_match": {
                'query': word,
                'fuzziness': '2',
                "slop": 1,
                "fields": ["skills.name"],
                
            }
        } for word in words
    ]
    
    search_query += match_skill
    
    payload = {
        "bool": {
            "should": search_query,
            "must": filter_query
        }
    }
    
    es = get_elasticsearch_client()
    resp = es.search(index='company_index', query=payload, size = 10000)
    
    first_resp = [result['_source'] for result in resp['hits']['hits']]
    
    match_each_word = [
        {
            "multi_match": {
                'query': word,
                'fuzziness': '2',
                "slop": 1,
                "fields": ['overview', 'advantage', 'full_name'],
                
            }
        } for word in words
    ]
    
    search_query += match_each_word
    
    payload = {
        "bool": {
            "should": search_query,
            "must": filter_query
        }
    }
    
    resp = es.search(index='company_index', query=payload, size = 10000) 
    second_resp = [result['_source'] for result in resp['hits']['hits']]
    
    for job in second_resp:
        if job not in first_resp:
            first_resp.append(job)
    
    
    
    return first_resp 