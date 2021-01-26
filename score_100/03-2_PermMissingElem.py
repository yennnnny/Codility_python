"""An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)],
which means that exactly one element is missing.

Your goal is to find that missing element.
Write a function:
def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)]."""

def solution(A):
    if A == [] or (len(A) == max(A)-1 and min(A) != 1):
        return 1
    elif max(A) == len(A):
        return max(A) + 1

    A.sort()
    i = 0
    k = min(A)

    while A[i] == k:
        i += 1
        k += 1

    return k