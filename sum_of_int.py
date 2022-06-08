def add_it_up(num):
  "This function will give the sum of the integers from zero to the input parameter"
  sum = 0
  if (num>0):
      count=0
      while(count<=num):
          sum=sum+num
          num=num-1
      return sum
  else:
      return sum
num = int(input("Please enter the integer: "))
sum = add_it_up(num)
print("sum is : ",sum)
