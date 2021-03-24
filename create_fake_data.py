from faker import Factory
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def create_names(fake):
    for x in range(50):
        genFname = fake.first_name()
        genLname = fake.last_name()
        genAddress = fake.address()
        genPhone = fake.phone_number()
        go = es.index(
            index="customer",
            body={
                "first_name": genFname,
                "last_name": genLname,
                "address": genAddress,
                "phone_number": genPhone,
            }
        )
        print(json.dumps(go))


if __name__ == '__main__':
    fake = Factory.create()
    create_names(fake)
