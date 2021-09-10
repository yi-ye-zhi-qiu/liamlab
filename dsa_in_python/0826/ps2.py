import sys; print(sys.version)

'''
Remove all adjacent duplicates. Given a string S
of lowercase letters, a duplicated removal consists
of choosing two adjacent and equal letters
and removing them.
'''

def f(s: str) -> str:

    l = []
    for i in range(len(s)):

        if i<len(s)-1 and s[i] == s[i+1]:
            #optimize removal of i<len(s)-1
            l.pop()
        else:
            l.append(s[i])

    return ''.join(l)


'''
Given a string S of lower and upper case letters,
return a good string, defined as not having:

s[i] is a lower-case letter and s[i+1] is the same
letter as upper-case or vice versa.
'''

def g(s: str) -> str:


    l = []
    for i in range(len(s)-1):
        #detect iI or Ii ... i == I.lower(), i.upper() == I
        #do not detect gi, gI, ff, II, if I==I or f==f w/ no upper/lower
        l.append(s[i])

        if s[i] != s[i+1] and s[i].lower() == s[i+1] or s[i].upper() == s[i+1]:
            prev =l.copy()
            l.pop()
            print(f'{s[i]} is in violation to {s[i+1]}, popped {prev} to {l}')

    l.append(s[-1])
    return ''.join(l);


def h(target: list, n: int) -> list:

    l = []
    for i in range(1,n+2):
        print(i)
        if i in target:
            l.append('Push')
        if l.count('Push')-l.count('Pop') != len(target) and i not in target:
            l.append('Push')
            l.append('Pop')

    return target,n,l

def o(nums1: list, nums2: list) -> list:

    l = []
    '''
    for i in range(len(nums1)):

        val = nums1[i]
        index = nums2.index(val)
        subset = nums2[index:]
        print(subset)

        m = val

        for j in range(len(subset)):
            if subset[j] > m:
                l.append(subset[j])
                m = subset[j]
                break;

        if m == val:
            l.append(-1)

    '''
    k = nums1
    for i in range(len(nums2)):
        if nums2[i] in k:
            slice = max(nums2[i:])
            if slice > i

    print(l)
    return l

if __name__ == "__main__":
    print(f('leEeetcode'),'\n')
    print(g('giIiraffEe'),'\n')
    print(h([2,3,4],4),'\n')
    print(o([4,1,2],[1,3,4,2]))
