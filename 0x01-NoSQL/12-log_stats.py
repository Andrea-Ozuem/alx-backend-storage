#!/usr/bin/env python3

'script that provides some stats about Nginx logs stored in MongoDB'

from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
log_collection = client.logs.nginx
print(log_collection.count_documents({}), 'logs')
print('Methods:')
print(f'\tmethod GET: {log_collection.count_documents({"method": "GET"})}')
print(f'\tmethod POST: {log_collection.count_documents({"method": "POST"})}')
print(f'\tmethod PUT: {log_collection.count_documents({"method": "PUT"})}')
patch = log_collection.count_documents({"method": "PATCH"})
print(f'\tmethod PATCH: {patch}')
delete = log_collection.count_documents({"method": "DELETE"})
print(f'\tmethod DELETE: {delete}')
status = log_collection.count_documents({"method": "GET", "path": "/status"})
print(f'{status} status check')
