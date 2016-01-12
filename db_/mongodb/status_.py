import pprint

import pymongo


client = pymongo.MongoClient()
db = client.test

print '#' * 40
print 'server info'
print '#' * 40
pprint.pprint(client.server_info())

print '#' * 40
print 'serverStatus'
print '#' * 40
pprint.pprint(db.command('serverStatus'))

print '#' * 40
print 'dbStats'
print '#' * 40
pprint.pprint(db.command('dbStats'))

print '#' * 40
print 'collStats'
print '#' * 40
pprint.pprint(db.command('collStats', 'test'))
