
from operator import truediv


def product_or_sum(n1, n2):
    
    if(n1 * n2 <= 1000):
        return n1 * n2
    else:
        return n1 + n2
    
def remove_chars(word, count):
    return word[count:]
    
def same_digits_list(list):
    if list[0] == list[-1]:
        return True
    else:
        return False
    

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]  

n1 = 20
n2 =20

print("The result is", product_or_sum(n1, n2))
print("The result is", product_or_sum(40, 30))

prev = 0

for i in range(1, 11):
    sum = i + prev
    print("Current", i, "Prev", prev, " Sum: ", sum)
    prev = i

wort = input("Enter word:")

length = len(wort)

for i in range (0, length -1, 2):
    print(wort[i])
    
print(remove_chars(wort, 4))

print(same_digits_list(numbers_x))
print(same_digits_list(numbers_y))

div_five_list = [10, 20, 33, 46, 55]

for i in div_five_list:
    if i % 5 == 0:
        print(i)
        
str_x = "Emma is good developer. Emma is a writer"

print(str_x.count("Emma"))

for j in range(6):
    for i in range(j):
        print(j, end=" ")
    print()
    

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
    
for i in range(5, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print(" ")

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)


