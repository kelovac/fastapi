from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elasticsearch import Elasticsearch
import logging

app = FastAPI()
es = Elasticsearch()


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


class Customer(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    jmbg: int
    card_number: int


@app.get("/customer")
def get_customer():
    body = {
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
        "size": 10000
    }
    res = es.search(index="customer", body=body)
    return res['hits']['hits']


@app.post("/customer")
def create_customer(customer: Customer):
    body = {
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'address': customer.address,
        'phone_number': customer.phone_number,
        'jmbg': customer.jmbg,
        'card_number': customer.card_number,
    }

    try:
        res = es.index(index="customer", body=body, id=customer.first_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return res


@app.get("/customer/id/{term}")
def search_customer(term: int):
    body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "multi_match": {
                            "query": term + "*",
                            "fields": [
                                "jmbg",
                                "card_number"
                            ]
                        }
                    },
                    {
                        "match_all": {}
                    }
                ],
                "filter": []
            }
        },
        "highlight": {
            "fields": {
                "*": {}
            }
        }
    }

    res = es.search(index="customer", body=body)

    return res['hits']['hits']


@app.get("/customer/search/{term}")
def search_customer(term: str):
    body = {
        "query": {
            "simple_query_string": {
                "query": term + "*",
                "fields": ["first_name", "last_name"],
                "default_operator": "and"
            }
        }
    }

    res = es.search(index="customer", body=body)

    return res['hits']['hits']


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
