# coding=utf-8
# author=uliontse

'''MIT License

Copyright (c) 2019 UlionTse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. You may obtain a copy of the
License at

    https://github.com/shinalone/ALG/blob/master/LICENSE

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import bisect
from heapq import merge


def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L


def comb_sort(L):
    gap = len(L)
    swap = True
    while gap > 1 or swap:
        gap = max(1,int(gap / 1.25))
        swap = False
        for i in range(len(L)-gap):
            j = i + gap
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
                swap = True
    return L


def heap_sort(L):
    def siftdown(L,begin,end):
        root = begin
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and L[child] < L[child+1]:
                child += 1
            if L[root] < L[child]:
                L[root],L[child] = L[child],L[root]
                root = child
            else:
                break

    for begin in range((len(L)-2)//2,-1,-1):
        siftdown(L,begin,len(L)-1)
    for end in range(len(L)-1,0,-1):
        L[end],L[0] = L[0],L[end]
        siftdown(L,0,end-1)
    return L


def insert_sort(L,method='auto'):
    if method == 'auto':
        for i in range(1, len(L)):
            x = L[i]
            j = i
            while j > 0 and L[j - 1] > x:
                L[j] = L[j - 1]
                j -= 1
            L[j] = x
        return L
    elif method == 'binSearch':
        for i in range(1, len(L)):
            key = L[i]
            low, up = 0, i
            while up > low:
                middle = (low + up) // 2  # binSearch
                if L[middle] < key:
                    low = middle + 1
                else:
                    up = middle
            # print(L[:low],[key],L[low:i], L[i+1:])
            L = L[:low] + [key] + L[low:i] + L[i + 1:]
        return L
    elif method == 'bisect':
        for i in range(1, len(L)):
            bisect.insort(L, L.pop(i), 0, i) # import bisect
        return L
    else:
        raise('[method] is error!')


def merge_sort(L):
    if len(L) > 1:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return list(merge(left,right)) # from heapq import merge
    return L


def quick_sort(L):
    if len(L) > 1:
        k = L[0]
        less = quick_sort([elem for elem in L if elem < k])
        more = quick_sort([elem for elem in L if elem > k])
        return less + [k] * L.count(k) + more
    return L


def radix_sort(L,base=10): # bucket_sort
    def list_to_bucket(L,base,iteration):
        bucket = [[] for _ in range(base)]
        for num in L:
            digit = (num // (base ** iteration)) % base # 最低位优先(Least Significant Digit first)法，简称LSD法
            bucket[digit].append(num)
        # print(bucket)
        return bucket

    def bucket_to_list(bucket):
        nums = []
        for bkt in bucket:
            for e in bkt:
                nums.append(e)
        return nums

    it = 0
    while base ** it <= max(L):
        L = bucket_to_list(list_to_bucket(L,base,it))
        it += 1
    return L


def select_sort(L):
    for i,e in enumerate(L):
        mn = min(range(i,len(L)), key=L.__getitem__) # 获得`索引i`之后切片的最小值的`索引mn`。
        L[i],L[mn] = L[mn],e
    return L


def shell_sort(L):
    middle = len(L) // 2
    while middle:
        for i,e in enumerate(L):
            while i > middle and L[i-middle] > e:
                L[i] = L[i-middle]
                i -= e
            L[i] = e
        middle = 1 if middle == 2 else int(middle * 5/11)
    return L


# TODO
# print(算法：时间复杂度，空间复杂度)


