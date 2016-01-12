# MongoDB tests with Python

### sandalone conf
```
~/dev/_bin/mongodb/bin/mongod --dbpath ~/dev/_bin/mongodb/bases/standalone/db
```

### replica-set conf
```
~/dev/_bin/mongodb/bin/mongod --port 27020 --dbpath ~/dev/_bin/mongodb/bases/replica_set/rs0_0 --replSet rs0 --smallfiles --oplogSize 128
~/dev/_bin/mongodb/bin/mongod --port 27021 --dbpath ~/dev/_bin/mongodb/bases/replica_set/rs0_1 --replSet rs0 --smallfiles --oplogSize 128
~/dev/_bin/mongodb/bin/mongod --port 27022 --dbpath ~/dev/_bin/mongodb/bases/replica_set/rs0_2 --replSet rs0 --smallfiles --oplogSize 128
```

### load data for aggregation
data source: mongodb.org
```
~/dev/_bin/mongodb/bin/mongoimport -d test -c restaurants --drop ./raw/restaurants.json
~/dev/_bin/mongodb/bin/mongoimport -d test -c zips --drop ./raw/zips.json
```
