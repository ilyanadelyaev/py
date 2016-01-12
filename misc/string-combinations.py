"""
O(N!)

ab = ab ba
abc = abc acb cab bac bca cba
abcd = abcd abdc adbc dabc acbd...
"""

def combine(data):
    if len(data) < 2:
        return data
    variants = set((data[0],))
    for ch in data[1:]:
        temp = set()
        for var in variants:
            for i in xrange(len(var)):
                temp.add(var[:i] + ch + var[i:])
            temp.add(var + ch)
        variants = temp
    return sorted(variants), len(variants)

print 'a =', combine('a')
print 'ab =', combine('ab')
print 'abc =', combine('abc')
print 'abcd =', combine('abcd')
print 'abcde =', combine('abcde')
print 'abcdef =', combine('abcdef')
