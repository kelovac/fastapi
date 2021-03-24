from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
res = es.search(index="customer", body={
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {
          }
        }
      ],
      "must_not": [
      ],
      "should": [
      ]
    }
  },
  "from": 0,
  "size": 10
})
#print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']))

