from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()

s = Search(using=client, index="sound_recordings") \
    .query("match", title="Shape of You")   \

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

