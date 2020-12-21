import requests
# r =requests.get('http://localhost')

from elasticsearch import Elasticsearch 
es = Elasticsearch([{'host': 'localhost', 'port' : 9200}])

print(es.get(index='sw', doc_type='people', id=5))