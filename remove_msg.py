#!/usr/bin/env python2.7
import datetime,pymongo,pprint

c = pymongo.MongoClient()

for dbn in c.database_names():
    db = getattr(c, dbn)
    print "Database: ", dbn
    print db.collection_names()


db = c.inbox


t_start = datetime.datetime(2016,9,8,00,0,0,0)
t_end = datetime.datetime(2016,9,10,00,0,0,0)

r = db.stix.find({"created_on" :
                    {
                    "$gte":t_start,
                    "$lte":t_end
                    }
                })

print "Removing %d records... "%(r.count())



r = db.stix.remove({"created_on" :
                    {
                    "$gte":t_start,
                    "$lte":t_end
                    }
                })

