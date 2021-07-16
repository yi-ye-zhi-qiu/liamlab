'''
Longest increasing subsequence of an array. Given an array L return the length of the longest increasing subsequence. L = [1,2,3,2,5] --> return 3, as [1,2,3] longer than [2,5]; [1,1,1,1,1] --> return 1, as [1] is the longest increasing subsequence; [1,0,1,0,1,0] --> return 2, as len([0,1]) is 2.
'''

def longest_sub(L) -> int:
    '''Sliding window algorithm'''

    anchor = 0
    result = 0

    for i in range(len(L)):

        if i>0 and L[i-1] >= L[i]: anchor = i

        result = max(result, i-anchor+1)

    return result;
