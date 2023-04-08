from django_elasticsearch_dsl import Document, fields, Index
from .models.Company import Company


company_index = Index('company_index')


@company_index.document
class CompanyDocument(Document):
    
    class Index:
        name = 'company_index'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Company
        
        fields = [
            "id",
            'name',
            "full_name",
            "type",
            "working_time"
        ]