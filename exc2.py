from mock_data import catalog


def print_catalog_total():
    total = 0 
    # for product in catalog:
        # print(product["price"])
    for product in catalog:
        total = total + product["price"]

        # print(total)
        print(f"The total of the catalog is {round(total,2)}")




print_catalog_total()




def say_hello():
    print("Hello there!")

def print_the_sum(a,b):
    print(a+b)

def print_the_division(a,b):
    if b == 0:
        print("Error: division by zero is not allowed ")
    else:
        print(a/b)

def print_the_cheaper(a,b):
    if type(a) not in [int, float]:
        print("Error, num1 is not valid")
        return # return means "stop" do not continue this function  
    if type(b) not in [int, float]:
        print("Error, num1 is not valid")
        return
    if a < b:
        print (a)
    elif a == b:
        print ("the same number")
    else:
        print (b)

def print_all_numbers ():
    nums= [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    for i in nums:
        print(i)

def print_the_sum ():
    nums= [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    #this will not work for our project 
    # total = sum(nums)
    # print(total)

    total = 0
    for n in nums:
        total +=n 
        # total = total + n ( the above is the short cut ) 
        print(total)

def nums_greater_than_40():
    nums= [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    total = 0 
    for n in nums :
        if n > 40:
            total +=n
    print(total)


def nums_lower_than_50():
    nums= [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    count = 0 
    for n in nums :
        if n <= 50:
            count = count +1
    print(count)


# say_hello()
# print_the_sum (21,21)
# print_the_division(10,4)

# print_the_division(10,0)

# print_the_cheaper(34,10)
# print_the_cheaper(3,100)
# print_the_cheaper(100,100)
# print_the_cheaper("a",100)
# print_the_cheaper(100,"b")

# print_all_numbers()

# print_the_sum()

# nums_greater_than_40()

# nums_lower_than_50()