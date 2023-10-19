
def average(x,y):
    sum=x+y 
    # calculating the average
    result=sum/2
    print(f'The average ={result}')

average(4,6)    




test2.py 
number1=input('Enter firstnumber: ')
number2=input('Enternumber1: ')
number3=input('Enter number3: ')

if(number1<number2 and number1<number3):
        print(f"The minimum number is {number1}")
elif(number2<number1 and number2<number3):
          print(f"The minimum number is {number2}")
else:
           print(f"The minimum number is {number3}")
# calling the function  

