#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that cover a specific topic.

    Parameters:
        mongo_collection (pymongo.collection.Collection): A PyMongo collection object connected to the "school" collection.
        topic (str): The topic you want to search for.

    Returns:
        list of dict: A list of school documents that cover the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
