def average(array):
    # your code goes here
    set_heights = set(array)
    sum_heights = 0
    distinct_heights = 0
    for i in array:
        sum_heights += i
        distinct_heights += 1
    return sum_heights / distinct_heights

if __name__ == '__main__':