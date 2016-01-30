"""
https://habrahabr.ru/post/238513/

session.query().with_for_update(read=True)  # SELECT .. LOCK IN SHARE MODE
session.query().with_for_update(read=False)  # SELECT .. FOR UPDATE
"""

import uuid
import threading

import sqlalchemy
import sqlalchemy.ext.declarative


print_lock = threading.Lock()

def log(*args):
    with print_lock:
        for a in args:
            print a,
        print


# Declare model

BaseModel = sqlalchemy.ext.declarative.declarative_base()


class ID(BaseModel):
    __tablename__ = 'id'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    value = sqlalchemy.Column(sqlalchemy.String(20), unique=True)


# create engine with isolation level
def get_engine(isolation_level):
    # REPEATABLE READ, READ COMMITTED, SERIALIZABLE, READ UNCOMMITTED
    return sqlalchemy.create_engine(
        'mysql+pymysql://ilya:ilya@localhost/test_transactions',
        isolation_level=isolation_level,
    )


########################################
# Read
########################################

def test__read__repeatable():
    """
    Test read with REPEATABLE READ:
    S1 select - not found
    S2 select - not found
    S1 insert - OK
    S1 select - found
    S2 select - not found
    S1 commit - OK
    S2 select - not found
    """

    print 'REPEATABLE READ: read'

    Engine = get_engine('REPEATABLE READ')
    BaseModel.metadata.create_all(Engine)
    Session = sqlalchemy.orm.sessionmaker(bind=Engine)

    s1 = Session()
    s2 = Session()

    value = uuid.uuid4().hex[:20]
    e_query = threading.Event()
    e_flush = threading.Event()
    e_commit = threading.Event()

    def processor_1(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value not exists: False =', res)
        # wait for S2 query
        e_query.wait()
        #
        i = ID(value=value)
        s.add(i)
        #
        s.flush()  # OK
        log('S1: inserted')
        # S1 flush is OK
        e_flush.set()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value exists: True =', res)
        #
        s.commit()  # OK
        log('S1: commited')
        # S1 commit is OK
        e_commit.set()

    def processor_2(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists: False =', res)
        # S2 query OK
        e_query.set()
        # wait for S1 flush
        e_flush.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists after S1 insert: False =', res)
        # wait for S1 commit
        e_commit.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists after S1 commit: False =', res)
        #
        s.close()

    th = [
        threading.Thread(target=processor_1, args=(s1, value)),
        threading.Thread(target=processor_2, args=(s2, value)),
    ]
    [t.start() for t in th]
    [t.join() for t in th]

    print '-' * 10


def test__read__commited():
    """
    Test read with READ COMMITTED:
    S1 select - not found
    S2 select - not found
    S1 insert - OK
    S1 select - found
    S2 select - not found
    S1 commit - OK
    S2 select - found
    """

    print 'READ COMMITTED: read'

    Engine = get_engine('READ COMMITTED')
    BaseModel.metadata.create_all(Engine)
    Session = sqlalchemy.orm.sessionmaker(bind=Engine)

    s1 = Session()
    s2 = Session()

    value = uuid.uuid4().hex[:20]
    e_query = threading.Event()
    e_flush = threading.Event()
    e_commit = threading.Event()

    def processor_1(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value not exists: False =', res)
        # wait for S2 query
        e_query.wait()
        #
        i = ID(value=value)
        s.add(i)
        #
        s.flush()  # OK
        log('S1: inserted')
        # S1 flush is OK
        e_flush.set()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value exists: True =', res)
        #
        s.commit()  # OK
        log('S1: commited')
        # S1 commit is OK
        e_commit.set()

    def processor_2(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists: False =', res)
        # S2 query OK
        e_query.set()
        # wait for S1 flush
        e_flush.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists after S1 insert: False =', res)
        # wait for S1 commit
        e_commit.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value exists after S1 commit: True =', res)
        #
        s.close()

    th = [
        threading.Thread(target=processor_1, args=(s1, value)),
        threading.Thread(target=processor_2, args=(s2, value)),
    ]
    [t.start() for t in th]
    [t.join() for t in th]

    print '-' * 10


def test__read__uncommited():
    """
    Test read with READ UNCOMMITTED:
    S1 select - not found
    S2 select - not found
    S1 insert - OK
    S1 select - found
    S2 select - found
    S1 commit - OK
    S2 select - found
    """

    print 'READ UNCOMMITTED: read'

    Engine = get_engine('READ UNCOMMITTED')
    BaseModel.metadata.create_all(Engine)
    Session = sqlalchemy.orm.sessionmaker(bind=Engine)

    s1 = Session()
    s2 = Session()

    value = uuid.uuid4().hex[:20]
    e_query = threading.Event()
    e_flush = threading.Event()
    e_commit = threading.Event()

    def processor_1(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value not exists: False =', res)
        # wait for S2 query
        e_query.wait()
        #
        i = ID(value=value)
        s.add(i)
        #
        s.flush()  # OK
        log('S1: inserted')
        # S1 flush is OK
        e_flush.set()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value exists: True =', res)
        #
        s.commit()  # OK
        log('S1: commited')
        # S1 commit is OK
        e_commit.set()

    def processor_2(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists: False =', res)
        # S2 query OK
        e_query.set()
        # wait for S1 flush
        e_flush.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value exists after S1 insert: True =', res)
        # wait for S1 commit
        e_commit.wait()
        #
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value exists after S1 commit: True =', res)
        #
        s.close()

    th = [
        threading.Thread(target=processor_1, args=(s1, value)),
        threading.Thread(target=processor_2, args=(s2, value)),
    ]
    [t.start() for t in th]
    [t.join() for t in th]

    print '-' * 10


########################################
# Write
########################################

def test__write():
    """
    Test write:
    S1 select - not found
    S2 select - not found
    S1 insert - OK
    S2 insert - Failure with "Duplicate"
    """

    print 'write'

    Engine = get_engine('REPEATABLE READ')
    BaseModel.metadata.create_all(Engine)
    Session = sqlalchemy.orm.sessionmaker(bind=Engine)

    s1 = Session()
    s2 = Session()

    value = uuid.uuid4().hex[:20]
    e_query = threading.Event()
    e_flush = threading.Event()

    def processor_1(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S1: value not exists: False =', res)
        # wait for S2 query
        e_query.wait()
        #
        i = ID(value=value)
        s.add(i)
        #
        s.flush()  # OK
        log('S1: inserted')
        # S1 flush is OK
        e_flush.set()
        #
        s.commit()  # OK
        log('S1: commited')

    def processor_2(s, value):
        res = s.query(sqlalchemy.sql.exists().where(
            ID.value == value)).scalar()
        log('S2: value not exists: False =', res)
        # S2 query OK
        e_query.set()
        #
        i = ID(value=value)
        s.add(i)
        # wait for S1 flush
        e_flush.wait()
        #
        try:
            s.flush()  # not OK on S1 commit
        except sqlalchemy.exc.IntegrityError as ex:
            log('S2: insert error with:', ex.message)
        #
        s.close()

    th = [
        threading.Thread(target=processor_1, args=(s1, value)),
        threading.Thread(target=processor_2, args=(s2, value)),
    ]
    [t.start() for t in th]
    [t.join() for t in th]

    print '-' * 10



if __name__ == '__main__':
    test__read__repeatable()
    test__read__commited()
    test__read__uncommited()
    #
    test__write()
