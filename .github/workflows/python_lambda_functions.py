list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]

#lambda

add_num = lambda x , y : x + y
a = 10
b = 10
print(add_num(a,b))

#map

add_list = list(map(add_num,list1, list2))
print (add_list)

#reduce

import functools

reduce_list = functools.reduce(add_num, list1)
print(reduce_list)

#filter

seq = [1,2,3,5,6,8,9]
filter_odd_num = lambda x : x % 2 != 0
result_filter = list(filter(filter_odd_num, seq))
print(result_filter)

# list comprehension

list_random_num = [1,2,8,9,12,15,18,20]
list_str = ['hi', 'hello', 'bye', 'good morning']
result_comprehension = [ x for x in list_random_num if x % 2 == 0 ]
print(result_comprehension)

result_comprehension1 = [ x.upper() for x in list_str ]
print(result_comprehension1)

list_123 = [1,-1,2,-5,9,10,-6]
pos_num = [ x for x in list_123 if x > 0 ]
neg_num = [ x for x in list_123 if x < 0 ]

print(pos_num+neg_num)
