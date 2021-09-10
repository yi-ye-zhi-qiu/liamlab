#Problem 2
def nonrepeatinglen(s):
    anchor, result =0,0
    l = []
    for i in range(len(s)):
        if s[i] in l:
            #check for repeats
            l = []
            print(f'Dragging anchor from {anchor} to {i}')
            anchor = i
        l.append(s[i])
        print(f'l is {l}')
        result = max(result, i-anchor+1)
    return result

print(nonrepeatinglen("abcdefffffffff"))


#Problem 3
def longest_sub(L) -> int:
    '''Sliding window algorithm'''

    anchor = 0
    result = 0

    for i in range(len(L)):

        if i>0 and L[i-1] >= L[i]: anchor = i

        result = max(result, i-anchor+1)

    return result;


S, k = "abcbb", 3

#Problem 4
def sub_distinct(S) -> int:

    d = ''
    anchor = 0
    res = 0

    for i in range(len(S)):

        if S[i] in d:
            anchor = i
            d = ''
        d += S[i]

        res = max(res, i-anchor+1)

    print(res)
    return res


#Problem 5
def sub_k_distinct(S, k) -> str:

    d = ''
    anchor, res = 0, ''

    for i in range(len(S)):

        d += S[i]

        print(f'{d=}')

        if i<len(S)-1 and len(set(d + S[i+1])) > k: #If adding next character more than k unique
            anchor = i
            print(f'Next char len {set(d + S[i+1])} represented by {d + S[i+1]} is > {k} reset d to val at index {anchor} ({S[i-1]}) and anchor to {anchor}')
            d = S[i]

        if len(d) > len(res) and len(set(d)) == k:
            res = d

    return res

print(sub_k_distinct('abgggge', 2))


#Problem 6

from collections import defaultdict

def sub_arrays(L, k) -> int:

    def f(L, k):

        n, ans, i, d = len(L), 0, 0, defaultdict(int)

        for idx in range(n):

            d[L[idx]] += 1

            while len(d)>k:

                #print(f'Chopping down {d} to be {len(d)} == {k}')

                d[L[i]] -= 1

                if d[L[i]] == 0:
                    #print(f'{d}: Count of {L[i]} is 0, deleting {L[i]}')
                    del d[L[i]]

                i += 1

            print(f'Adding to result array of len {len(L[i:idx+1])} : {L[i:idx+1]} as it has <={k} distinct integers and is subarray of {L}')
            ans += (idx - i +1)
            #By counting the window sizes, we count the number of ALL WINDOWS
            #whose number of digits <= k , s.t. f(L,k) - f(L, k-1) is the number of windows
            #whose size is EXACTLY k.

        print(f'Total # of <={k} distinct int. for given L: {ans}')
        return ans

    return f(L, k) - f(L, k-1)
