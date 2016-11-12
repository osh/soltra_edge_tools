#!/usr/bin/env python2.7
import pymongo,pprint

c = pymongo.MongoClient()
db = c.inbox

uri = "opensource:URI-c98c7613-0322-4ce7-bb13-a56f1c4c113c"

r = db.stix.find_one({"data.api.object.id":uri})
pprint.pprint(r)

dnum = db.stix.remove({"data.api.object.id":uri})
print dnum

