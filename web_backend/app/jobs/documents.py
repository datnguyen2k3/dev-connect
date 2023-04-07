from django_elasticsearch_dsl import Document, Index
from .models.Job import Job
from django_elasticsearch_dsl import fields
from app.companies.models.Company import Company

job_index = Index('job_index')


@job_index.document
class JobDocument(Document):
    
    company = fields.ObjectField(properties={
        'id': fields.TextField(),
        'name': fields.TextField(),
        'type': fields.TextField(),
    })
    
    skills = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    
    levels = fields.ObjectField(properties={
        'level': fields.TextField(),
    })
    
    class Index:
        name = 'job_index'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Job
        
        fields = [
            # 'company',
            # 'skills',
            # 'levels',
            'id',
            'is_active',
            'working_model',
            'title',
            'advantage',
            'description',
            'qualification',
            'benefit'
        ]
        


