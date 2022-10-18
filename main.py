

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

# ******************************
# Make your Code
# ******************************
count = numbers.count(delval)
for i in range(count):
    numbers.remove(delval)

else:
     numbers.clear()
   
print (numbers)
