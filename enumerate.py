#!/usr/bin/env python2.7
import pymongo

c = pymongo.MongoClient()

for dbn in c.database_names():
    db = getattr(c, dbn)
    print "Database: ", dbn
    print db.collection_names()


db = c.inbox

