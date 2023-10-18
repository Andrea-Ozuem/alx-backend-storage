#!/usr/bin/env python3
""" 101-main """


def top_students(mongo_collection):
    '''Python function that returns all students sorted by average score
    computes avgscore and returns all sorted by average score'''
    return mongo_collection.aggregate([
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
