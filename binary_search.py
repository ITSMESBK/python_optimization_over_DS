# =========================================================================================
# !/usr/bin/env python3
# Filename: binary_search.py
# Description: search a numerical value 
# Author: Bharathkumar Sivakumar <BHARATH SBK @ITSMESBK>
# Python Environment - Python3
# Usage: Search a number from a array in more efficient way
# ===========================================================================================
def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    print("start:{},End:{}".format(start,end))
    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2
        print("Start:{},Mid:{},End:{}".format(start,mid,end))

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    #array = [1,1,2,2,3,3,6,7,7,11,11]
    #element = 6
    binary_search_iterative(array, element)
