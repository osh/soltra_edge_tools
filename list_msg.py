#!/usr/bin/env python2.7
import pymongo,pprint

c = pymongo.MongoClient()

for dbn in c.database_names():
    db = getattr(c, dbn)
#    print "***********************"
#    print "Database: ", dbn
    for collection in db.collection_names():
        print "***********************"
        print "Database(%s).Collection(%s):"%(dbn, collection)
        r = db[collection].find_one()
        pprint.pprint(r)

