def hour_angle(hour, minute, second, millisecond):
    """
    one hour angle is 30 degrees
    multiply to H hours + M / 60 munutes + S / 360 seconds + MS / 60 * 60 * 1000 milliseconds
    """
    return 30.0 * ( \
        hour / 1.0 + \
        minute / 60.0 + \
        second / ( 60.0 * 60.0 ) + \
        millisecond / ( 60.0 * 60.0 * 1000.0 ) \
    )


def minute_angle(minute, second, millisecond):
    """
    one minute angle is 6 degrees
    multiply to M minutes + S / 60 seconds + MS / 60000 milliseconds
    """
    return 6.0 * ( \
        minute / 1.0 + \
        second / 60.0 + \
        millisecond / ( 60.0 * 1000.0 ) \
    )

def second_angle(second, millisecond):
    """
    one second angle is 6 degrees
    multiply to S seconds + MS / 1000 milliseconds
    """
    return 6.0 * ( \
        second / 1.0 + \
        millisecond / 1000.0 \
    )

def millisecond_angle(millisecond):
    """
    one millisecond angle is 0.36 degrees
    """
    return 0.36 * millisecond


for h in xrange(0, 12):
    for m in xrange(0, 60):
        for s in xrange(0, 60):
            for ms in xrange(0, 1000):
                ha = hour_angle(h, m, s, ms)
                ma = minute_angle(m, s, ms)
                sa = second_angle(s, ms)
                msa = millisecond_angle(ms)
                if abs(ha - ma) < 0.001:
                    print '{:02d}:{:02d}:{:02d}:{:04d} - {:.3f} / {:.3f} / {:.3f} / {:.3f}'.format(
                        h, m, s, ms, ha, ma, sa, msa)
