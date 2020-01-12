from collections import defaultdict

# Complete the freqQuery function below.
# Remember: Search in keys of map takes O(1) time and search in values of map takes O(n) time.

def freqQuery(queries):
    d = defaultdict(int)     # keeping track of freq of each elem
    freq_of_values_in_d = defaultdict(int)       # keeps track of freq of freq in d

    for op, val in queries:
        if (op == 1):       # Insert x in your data structure.
            freq_of_values_in_d[d[val]] -= 1    # decrement previous number's freq e.g. if d = {1:1} now means freq_of_values_in_d = {1:1},
#  after executing d[val]+=1 on next line d = {1:2} so freq_of_values_in_d = {1:0} first & then freq_of_values_in_d = {1:0, 2:1}
            d[val] += 1
            freq_of_values_in_d[d[val]] += 1
        elif (op == 2):    # Delete one occurence of y from your data structure, if present.
            if d[val] > 0:
                freq_of_values_in_d[d[val]] -= 1
                d[val] -= 1
                freq_of_values_in_d[d[val]] += 1
        elif (op == 3):
            if freq_of_values_in_d[val]>0:      # if value for any key in freq_of_values_in_d is >0, it means that freq exists in values of d
                print(1)
            else:
                print(0)


if __name__ == '__main__':

    # q = int(input().strip())
    #
    # queries = []
    #
    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    # ans = freqQuery([[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]])   # ans = 0 1 1
    # ans = freqQuery([[3, 4], [2, 1003], [1, 16], [3, 1]])   # ans = 0 1
    ans = freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]])  # ans = 0 1
    # ans = freqQuery([[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]])    #     ans = 0 1



# Algo works but time-out error on 4 test cases due to O(N) time complexity
# def freqQuery(queries):
#     d = {}      # keeping track of freq of each elem
#
#     for op, val in queries:
#         if (op == 1):       # Insert x in your data structure.
#             if val in d.keys():
#                 d[val] += 1
#             else:
#                 d[val] = 1
#         elif (op == 2):    # Delete one occurence of y from your data structure, if present.
#             if val in d.keys():
#                 if d[val] > 0:
#                     d[val] -= 1
#         elif (op == 3):
#             if val in d.values():
#                 print(1)
#             else:
#                 print(0)



# Algo works but time-out error due to O(N^2) time complexity

# def freqQuery(queries):
#     my_arr = []
#     for i in range(len(queries)):
#         if (queries[i][0] == 1):       # Insert x in your data structure.
#             my_arr.append(queries[i][1])
#         elif (queries[i][0] == 2):    # Delete one occurence of y from your data structure, if present.
#             if queries[i][1] in my_arr:
#                 my_arr.remove(queries[i][1])
#         else :
#             c = Counter(my_arr)
#             if (not c):         # checking if dict is empty
#                 print(0)
#             else:
#                 if queries[i][1] in c.values():
#                     print(1)
#                 else:
#                     print(0)