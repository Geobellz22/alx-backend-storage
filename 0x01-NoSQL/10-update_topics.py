#!/usr/bin/env python3
"""
This function changes all topics of a school document based on school names.

Parameters:
    mongo_collection (pymongo.collection.Collection): A PyMongo collection object connected to the "school" collection.
    name (str): The name of the school to update.
    topics (list of str): The list of topics to set for the school.

Returns:
    pymongo.results.UpdateResult: The result of the update operation, including the number of matched documents.

Example:
    To update topics for a school with the name "Example School," you can use the function like this:
    update_topics(my_mongo_collection, "Example School", ["Math", "Science", "History"])
"""
def update_topics(mongo_collection, name, topics):
     """Changes all topics of a school document"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
