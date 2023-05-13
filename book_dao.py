from pymongo_connector import collection
from pymongo_connector import pubcollection

# returns all books from the Book table
def findAll():
    results = collection.find()
    return results

# returns the book from the Book table that has the 
# indicated ISBN (if one exists)
def findByISBN(isbn):
    results = collection.find({'ISBN': isbn})
    return results

# returns books from the Book table that have the indicated title
def findByTitle(title):
    results = collection.find({'title': title})
    return results

# returns books from the Book table that were published by the 
# indicated publisher (publisher name provided)
def findByPublisher(publisher):
    results = collection.find({'published_by': publisher})
    return results

# returns books from the Book table with the 
# indicated title and publisher
def findByTitleAndPublisher(title, publisher):
    results = collection.find({'title': title, 'published_by': publisher})
    return results

# returns books from the Book table that were published 
# in the indicated year
def findByYear(year):
    results = collection.find({'year': year})
    return results

# returns books from the Book table within the indicated 
# price range (lowprice to highprice, inclusive)
def findByPriceRange(lowprice, highprice):
    results = collection.find({'price': {"$lte": highprice, "$gte": lowprice}})
    return results

# adds a publisher with the indicated
# attributes to the Publisher table
def addPublisher(name, phone, city):
    pubcollection.insert_one({'name': name, 'phone': phone, 'city': city})

# adds a book with the indicated attributes
# to the Book table
def addBook(bISBN, btitle, byear, bpublished_by, bprev_edition, bprice):
    if(bpublished_by == 'null' and bprev_edition == 'null'):
        collection.insert_one({
            'ISBN': bISBN,
            'title': btitle,
            'year': byear,
            'published_by': None,
            'previous_edition': None,
            'price': bprice
        })
    elif(bpublished_by == 'null'):
        collection.insert_one({
            'ISBN': bISBN,
            'title': btitle,
            'year': byear,
            'published_by': None,
            'previous_edition': bprev_edition,
            'price': bprice
        })
    elif(bprev_edition == 'null'):
        collection.insert_one({
            'ISBN': bISBN,
            'title': btitle,
            'year': byear,
            'published_by': bpublished_by,
            'previous_edition': None,
            'price': bprice
        })
    else:
        collection.insert_one({
            'ISBN': bISBN,
            'title': btitle,
            'year': byear,
            'published_by': bpublished_by,
            'previous_edition': bprev_edition,
            'price': bprice
        })

# helper method that checks whether a book with the 
# indicated ISBN exists in the Book table
def checkISBN(bISBN):
    results = collection.find({'ISBN': bISBN})
    return results

# helper method that checks whether a publisher with 
# name publisher_name already exists in the 
# Publisher table
def checkPublisher(publisher_name):
    results = pubcollection.find({'name': publisher_name})
    return results

# deletes a book with the given ISBN from the Book table
def deleteBook(ISBN):
    collection.delete_one({'ISBN': ISBN})

# updates a book with the indicated ISBN with the 
# indicated new values
def editBook(ISBN, newISBN, newTitle, newYear, newPublished_by, newPrev_edition, newPrice):
   

    # construct and execute query based on which 
    # foreign key attributes get null values
    if(newPublished_by == 'null' and newPrev_edition == 'null'):
        collection.update({'ISBN': ISBN}, {'$set': {'ISBN': newISBN, 'title': newTitle, 'year': newYear, "published_by": None, "previous_edition": None, "price": newPrice}})
    elif(newPublished_by == 'null'):
        collection.update({'ISBN': ISBN}, {'$set': {'ISBN': newISBN, 'title': newTitle, 'year': newYear, "published_by": None, "previous_edition": newPrev_edition, "price": newPrice}})
    elif(newPrev_edition == 'null'):
        collection.update({'ISBN': ISBN}, {'$set': {'ISBN': newISBN, 'title': newTitle, 'year': newYear, "published_by": newPublished_by, "previous_edition": None, "price": newPrice}})
    else:
        collection.update({'ISBN': ISBN}, {'$set': {'ISBN': newISBN, 'title': newTitle, 'year': newYear, "published_by": newPublished_by, "previous_edition": newPrev_edition, "price": newPrice}})