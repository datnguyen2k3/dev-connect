from django_elasticsearch_dsl import Document, fields
from .models.Company import Company

class CompanyDocument(Document):
    class Index:
        name = 'company_index'

    class Django:
        model = Company
        
        fields = [
            'name'
        ]