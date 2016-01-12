import random


def get_bit(num, bit):
    return 1 if (num & 1 << bit) else 0

def set_bit(num, bit):
    return num | 1 << bit

def clear_bit(num, bit):
    return num & ~(1 << bit)

def get_mask(st, en=None):
    if st <= en:
        return
    if en is None:
        return bin((1 << (st)) - 1)[2:]
    else:
        return None
        #return bin(((1 << (st + 1)) - 1) & ~((1 << (en + 1)) - 1))[2:]

def bit_not(a):
    binary = ''
    for i in xrange(len(a)):
        aa = a[i]
        if aa not in ('0', '1'):
            return
        if aa == '0':
            binary += '1'
        else:
            binary += '0'
    return binary

def bit_and(a, b):
    binary = ''
    if len(b) > len(a):
        a, b = b, a
    for i in xrange(1, len(a) + 1):
        aa = a[-i]
        bb = b[-i] if i <= len(b) else '0'
        if aa not in ('0', '1'):
            return
        if bb not in ('0', '1'):
           return
        #
        if aa == '1' and bb == '1':
            binary += '1'
        else:
            binary += '0'
        #
    return binary[::-1]

def bit_or(a, b):
    binary = ''
    if len(b) > len(a):
        a, b = b, a
    for i in xrange(1, len(a) + 1):
        aa = a[-i]
        bb = b[-i] if i <= len(b) else '0'
        if aa not in ('0', '1'):
            return
        if bb not in ('0', '1'):
            return
        #
        if aa == '1' or bb == '1':
            binary += '1'
        else:
            binary += '0'
        #
    return binary[::-1]

def bit_xor(a, b):
    binary = ''
    if len(b) > len(a):
        a, b = b, a
    for i in xrange(1, len(a) + 1):
        aa = a[-i]
        bb = b[-i] if i <= len(b) else '0'
        if aa not in ('0', '1'):
            return
        if bb not in ('0', '1'):
            return
        #
        if (aa == '1' and bb == '0') or (aa == '0' and bb == '1'):
            binary += '1'
        else:
            binary += '0'
        #
    return binary[::-1]


# ---

def insert_M_to_N(N, M, i, j):
    if (j - i + 1) != len(bin(M)) - 2:
        return
    for m in xrange((j - i + 1)):
        bit = get_bit(M, m)
        if bit:
            N = set_bit(N, i + m)
    return N

def int_to_bin(num, bits=32):
    num = int(num)
    if num == 0:
        return '0b0'
    #
    negative = False
    if num < 0:
        negative = True
        num *= -1
        num -= 1
    #
    binary = ''
    while num:
        num, bit = num / 2, num % 2
        binary += str(bit)
    binary = binary[::-1]
    #
    if negative:
        mask = get_mask(bits)
        binary = bit_xor(mask, binary)
    else:
        mask = get_mask(bits)
        mask = bit_not(mask)
        binary = bit_or(mask, binary)
    #
    return binary

def float_to_bin(num):
    # 62 bits
    # sign = 1 bit
    # mantissa = 52 bits
    # exponent = 11 bits / bias = 1023
    #
    sign = '0' if num > 0 else '1'
    #
    num = float(num)
    num = str(num)
    #
    dot_pos = num.find('.')
    # < 0
    if num[0] == '0':
        num = num.replace('.', '')
        zero_count = 0
        for i in xrange(len(num)):
            if num[i] == '0':
                zero_count += 1
            else:
                break
        #
        mantissa = num[zero_count:]
        exponent = - zero_count
        #
    # < 10
    elif dot_pos == 1:
        exponent = 0
        mantissa = num.replace('.', '')
    # > 10
    else:
        exponent = dot_pos - 1
        mantissa = num.replace('.', '')
    #
    mantissa = int_to_bin(mantissa, 52)
    exponent = int_to_bin(exponent + 1023, 11)
    return sign + exponent + mantissa


if __name__ == '__main__':
    #
    #print bin(insert_M_to_N(0b10000000000, 0b10011, 2, 6))
    #print bin(insert_M_to_N(0b1001000, 0b1111, 1, 4))

    #
    #val = -2
    #print val, int_to_bin(val)
    #val = -20
    #print val, int_to_bin(val)
    #val = -32000
    #print val, int_to_bin(val)
    #val = 32000
    #print val, int_to_bin(val)
    #for i in xrange(10):
    #    val = random.randrange(0, 32000)
    #    assert int_to_bin(val) == bin(val)
    #    print val, int_to_bin(val), bin(val)

    #
    val = 0.0729
    print val, float_to_bin(val)

    import sys; sys.exit(-1)

    num = 0b0101
    for i in xrange(7):
        print is_bit(num, i)
    print '='*4

    num = 0b101010
    for i in xrange(7):
        print bin(set_bit(num, i))
    print '='*4

    num = 0b101010
    for i in xrange(7):
        print bin(clear_bit(num, i))
    print '='*4

    for i in xrange(7):
        print bin(get_mask(i))
    print '='*4

    for i in xrange(7):
        print bin(get_mask(i, 2))
    print '='*4
