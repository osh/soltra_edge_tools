#!/usr/bin/env python2.7
import pymongo

c = pymongo.MongoClient()

for dbn in c.database_names():
    db = getattr(c, dbn)
    print "Database: ", dbn
    print db.collection_names()


db = c.inbox

db.stix.update({"data.idns" : "http://www.hailataxii.com"}, { "$set" : { "data.idns": "http://hailataxii.com" } } , upsert=False, multi=True );

#r = db.stix.find({"data.idns" : "http://www.hailataxii.com"}).limit(1)
#print r[0]
#print r[0]["_id"]
#print r.count()
#for r_i in r:
#    db.stix.update({"_id" : r_i["_id"] }, { "$set" : { "data.idns": "http://hailataxii.com"} }
#    r2 = db.stix.find({"_id" : r_i["_id"] })
#    db.stix.update({"data.idns" : "http://www.hailataxii.com"}, { "$set" : { "data.idns": "http://hailataxii.com" } } , { upsert: false, multi: true } );


