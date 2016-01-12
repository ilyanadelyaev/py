import time
import random


def generate_random_string(length, E=None):
    if E is None:
        E = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for _ in xrange(length):
        ret += random.choice(E)
    return ret


# Simple search

def simple_search(haystack, needle):
    if not haystack or not needle:
        return -1
    haystack_i = 0
    while haystack_i < len(haystack):
        needle_i = 0
        while needle_i < len(needle):
            if haystack_i + needle_i >= len(haystack):
                return -1
            if haystack[haystack_i+needle_i] == needle[needle_i]:
                if needle_i == len(needle) - 1:
                    return haystack_i
                needle_i += 1
                continue
            break
        haystack_i += 1
    return -1


# Boyer Moore search

def __create_suffixes(needle):
    suffixes = {'': 1}
    for needle_i in xrange(len(needle)-1, 0-1, -1):
        suffix = needle[needle_i:]
        search_i = len(needle)-1-1
        suffix_i = len(suffix)-1
        while True:
            if needle[search_i] == suffix[suffix_i]:
                if suffix not in suffixes:
                    suffixes[suffix] = len(needle) - 1 - search_i
                suffix_i -= 1
            elif suffix in suffixes:
                del suffixes[suffix]
                suffix_i = len(suffix)-1
                search_i += 1
            search_i -= 1
            if search_i < 0 or suffix_i < 0:
                break
        if suffix not in suffixes:
            suffixes[suffix] = len(needle)
    return suffixes


def __create_stop_sumbols__advanced(needle):
    """
    May be used without suffixes
    Shift always positiv value
    """
    stop_symbols = {}
    for needle_i in xrange(len(needle)-1):
        stop_symbol = needle[needle_i]
        stop_symbols.setdefault(stop_symbol, []).append(needle_i)
    return stop_symbols


def __get_stop_symbol_shift__advanced(haystack, needle, haystack_i, needle_i, stop_symbols):
    stop_symbol_shift = len(needle) - needle_i
    stop_symbol = haystack[haystack_i-needle_i]
    stop_symbol_array = stop_symbols.get(stop_symbol, None)
    if stop_symbol_array is not None:
        for x in xrange(len(stop_symbol_array)):
            stop_symbol_i = stop_symbol_array[-1-x]
            stop_symbol_shift = len(needle) - needle_i - 1 - stop_symbol_i
            if stop_symbol_shift > 0:
                break
        if stop_symbol_shift <= 0:
            stop_symbol_shift = len(needle) - needle_i
    return stop_symbol_shift


def boyer_moore_search(haystack, needle):
    if not haystack or not needle:
        return -1

    stop_symbols = __create_stop_sumbols__advanced(needle)
    #suffixes = __create_suffixes(needle)

    haystack_i = len(needle) - 1
    while haystack_i < len(haystack):
        needle_i = 0
        while needle_i < len(needle):
            if haystack[haystack_i-needle_i] == needle[len(needle)-1-needle_i]:
                needle_i += 1
                if needle_i >= len(needle):
                    return haystack_i - len(needle) + 1
                continue
            break

        # suffix
        #suffix = haystack[haystack_i+1-needle_i:haystack_i+1]
        #suffix_shift = suffixes.get(suffix, len(needle))

        # stop symbol
        stop_symbol_shift = __get_stop_symbol_shift__advanced(haystack, needle, haystack_i, needle_i, stop_symbols)

        # shift max
        #haystack_i += stop_symbol_shift if stop_symbol_shift > suffix_shift else suffix_shift
        haystack_i += stop_symbol_shift

    return -1


if __name__ == '__main__':

    TIMES = 10000
    HAYSTACK_LEN = 100
    NEEDLE_LEN = 5

    # TESTS
    for search in (
            simple_search,
            boyer_moore_search,
        ):
        # empty
        assert search('', '') == -1
        assert search('a', '') == -1
        assert search('', 'a') == -1
        # greater
        for _ in xrange(50):
            s = generate_random_string(10)
            ss = generate_random_string(20)
            assert search(s, ss) == -1
            ss = generate_random_string(50)
            assert search(s, ss) == -1
            ss = generate_random_string(100)
            assert search(s, ss) == -1
        # equal
        for _ in xrange(50):
            s = generate_random_string(10)
            assert search(s, s) == 0
            s = generate_random_string(50)
            assert search(s, s) == 0
            s = generate_random_string(100)
            assert search(s, s) == 0
        # wiki example
        assert boyer_moore_search('abeccaabadbabbad', 'abbad') == 11
        # misc
        haystack = 'abcdefghijklmnopqrstuvwxyz'
        assert search('', 'a') == -1
        assert search(haystack, '') == -1
        assert search('ab', 'ab') == 0
        assert search('abc', 'abc') == 0
        assert search('abcabc', 'abcabc') == 0
        assert search(haystack, haystack) == 0
        assert search(haystack*2, haystack*2) == 0
        assert search('a', 'aa') == -1
        assert search(haystack, haystack*2) == -1
        assert search(haystack, 'a') == 0
        assert search(haystack, 'abcd') == 0
        assert search(haystack, 'abcdef') == 0
        assert search('******kolokol', 'kolokol') == 6
        assert search('****kkolokol*****', 'kolokol') == 5
        assert search(haystack, 'b') == 1
        assert search(haystack, 'bcde') == 1
        assert search(haystack, 'bcdefg') == 1
        assert search(haystack, 'z') == 25
        assert search(haystack, 'xyz') == 23
        assert search(haystack, 'ax') == -1
        assert search(haystack, 'xa') == -1
        #
        print 'find - E small'
        tt = 0
        conc = 0
        for _ in xrange(TIMES):
            ne = generate_random_string(NEEDLE_LEN)
            hs = generate_random_string(HAYSTACK_LEN, ne)
            #
            find_res = hs.find(ne)
            if find_res >= 0:
                conc += 1
            #
            st = time.time()
            assert search(hs, ne) == find_res
            tt += time.time() - st
        print search.__name__, tt, conc
        #
        print 'find - E big - start'
        tt = 0
        conc = 0
        for _ in xrange(TIMES):
            ne = generate_random_string(NEEDLE_LEN)
            hs = generate_random_string(HAYSTACK_LEN) + \
                generate_random_string(HAYSTACK_LEN, ne)
            #
            find_res = hs.find(ne)
            if find_res >= 0:
                conc += 1
            #
            st = time.time()
            assert search(hs, ne) == find_res
            tt += time.time() - st
        print search.__name__, tt, conc
        #
        print 'find - E big - end'
        tt = 0
        conc = 0
        for _ in xrange(TIMES):
            ne = generate_random_string(NEEDLE_LEN)
            hs = generate_random_string(HAYSTACK_LEN, ne) + \
                generate_random_string(HAYSTACK_LEN)
            #
            find_res = hs.find(ne)
            if find_res >= 0:
                conc += 1
            #
            st = time.time()
            assert search(hs, ne) == find_res
            tt += time.time() - st
        print search.__name__, tt, conc
        #
        print 'find - E big - middle'
        tt = 0
        conc = 0
        for _ in xrange(TIMES):
            ne = generate_random_string(NEEDLE_LEN)
            hs = generate_random_string(HAYSTACK_LEN) + \
                generate_random_string(HAYSTACK_LEN, ne) + \
                generate_random_string(HAYSTACK_LEN)
            #
            find_res = hs.find(ne)
            if find_res >= 0:
                conc += 1
            #
            st = time.time()
            assert search(hs, ne) == find_res
            tt += time.time() - st
        print search.__name__, tt, conc
