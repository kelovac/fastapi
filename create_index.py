from elasticsearch import Elasticsearch


_es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

_es.indices.delete(index="customer", ignore=[400, 404])

request_body = {
    "settings": {
        "analysis": {
            "analyzer": {
                "autocomplete_analyzer": {
                    "tokenizer": "autocomplete",
                    "filter": [
                        "lowercase"
                    ]
                },
                "autocomplete_search_analyzer": {
                    "tokenizer": "keyword",
                    "filter": [
                        "lowercase"
                    ]
                }
            },
            "tokenizer": {
                "autocomplete": {
                    "type": "edge_ngram",
                    "min_gram": 1,
                    "max_gram": 30,
                    "token_chars": [
                        "letter",
                        "digit",
                        "whitespace"
                    ]
                }
            }
        }
    },
    'mappings': {
        'doc': {
            'properties': {
                'first_name':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    },
                'last_name':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    },
                'address':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    },
                'phone_number':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    },
                'jmbg':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    },
                'card_number':
                    {
                        'type': 'text',
                        "fields": {
                            "complete": {
                                "type": "text",
                                "analyzer": "autocomplete_analyzer",
                                "search_analyzer": "autocomplete_search_analyzer"
                            }
                        }
                    }
            }
        }
    }
}


res = _es.index(index="customer", body=request_body)
print(res)