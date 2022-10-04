from mongodb.mongodb import MongoDB
import re



def search(mongodb: MongoDB, database: str, collection: str, keyword: str):
    
    headline_result = search_headline(mongodb, database, collection, keyword)

    if headline_result.count() == 0:
        article_body_result = search_article_body(mongodb, database, collection, keyword)
        result_to_return = article_body_result
    else:
        result_to_return = headline_result

    return result_to_return



def search_headline(mongodb: MongoDB, database: str, collection: str, keyword: str):
    mongodb.setDb(database)
    mongodb.setCollection(collection)

    regx = re.compile(keyword, re.IGNORECASE)
    query_condition = {"headline": regx}

    result = mongodb.findDocument(query_condition)

    return result


def search_article_body(mongodb: MongoDB, database: str, collection: str, keyword: str):
    mongodb.setDb(database)
    mongodb.setCollection(collection)

    regx = re.compile(keyword, re.IGNORECASE)
    query_condition = {"body": regx}

    result = mongodb.findDocument(query_condition)

    return result


