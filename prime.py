slrange = input('Set the lower boundary ')
try:
    ilrange=int(slrange)
except:
    while True:
        try:
            ilrange = int(input('Please enter the positive number '))
        except:
            print('Sorry, It is not a number ')
            continue
        if ilrange < 0:
            print('Sorry, Please enter the positive number ')
            continue
        else:
            break

surange = input('Set the upper boundary ')
try:
    iurange=int(surange)
except:
    while True:
        try:
            iurange = int(input('Please enter the positive number '))
        except:
            print('Sorry, It is not a number ')
            continue
        if iurange < 0:
            print('Sorry, Please enter the positive number ')
            continue
        else:
            break

def prime_funct (i,j):
    for number in range(i,j):
        count=0
        for k in range(2,number//2):
            if(number%k==0):
                count=count+1
                break

        if(count==0 and number!=1):
            print(number)

prime_funct(ilrange,iurange)
