

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

# ******************************
# Make your Code
# ******************************
count = numbers.count(delval)
print(count)
for i in range(count):
    numbers.remove(delval)

else:
     exit
   
print (numbers)
