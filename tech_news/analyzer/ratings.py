from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    pipeline = [
        {"$sortByCount": "$category"},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    categories = [doc["_id"] for doc in get_collection().aggregate(pipeline)]

    return categories
