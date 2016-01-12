try:
    try:
        t = 1
        raise Exception('wow!')
    finally:
        print 'finnaly'
        del t
    print 'never!'
except Exception as ex:
    print str(ex)
    try:
        print t
    except NameError:
        pass
