#single line code for making a list of our own length
n=int(input())
inputs = [input().split(" ") for _ in range(n)]
print(inputs)

kk = list(input().split(" ") for i in range(3))
print(kk)

#nested list printing each element using recursion
movies = [32,43,[232,[23,7],[45]]]
def print_lol(a_list):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(movies)



current_value_size = int(input())
current_value = [int(input()) for _ in range(current_value_size)]
future_value_size = int(input())
future_value = [int(input()) for _ in range(future_value_size)]

#it is to capitalise the name in list
capitalized_class_names = [name.title() for name in class_names]



#-------------------------------------------
nums = [1, 2, 3]
vals = nums 
del vals[1:]

print(vals)
print(nums)



print(dir("pandas"))