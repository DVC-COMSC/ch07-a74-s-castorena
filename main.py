

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

# ******************************
# Make your Code
# ******************************
count = numbers.count(delval)
for i in range(count):
    numbers.remove(delval)

if count == 0:
     numbers.clear()
   
print (numbers)
