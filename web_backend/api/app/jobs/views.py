from app.jobs.models.Job import Job
from elasticsearch import Elasticsearch
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from src.utils import get_elasticsearch_client
from app.jobs.documents import JobDocument
import subprocess


@api_view(['DELETE'])
def delete_els_job_data_view(request):
    client = get_elasticsearch_client()
    response = client.indices.delete(index='job_index', ignore=[400, 404])
    return Response(response)