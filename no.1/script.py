#author ssekitto abdul marvi
#project greetings and age calculator
#date-2024-28-10

#importing python module for working with dates
import datetime
#getting the current your 
year=datetime.datetime.now().year
year=int(year)
print(year)
#requesting for inputs of name from the user
name=input('ENTER YOUR NAME PLEASE \n')
#greeting message from the sytem
print('Hello '+ name +' you have a nice name')
#request for age
print('HOW OLD ARE YOU \n')
age=input()
#error handling to take in only numbers
try:
    number=int(age)
    db=year-number
    print('so your are born ' +str(db))
except ValueError:
        print('please enter only numbers')
        age=input()
        number=int(age)
        db=year-number
        while number!=int():
                print('please enter only numbers')
                age=input()
                number=int(age)
                db=year-number
                if number==int():
                    break
                print('so your are born ' +str(db))
                
#end of the program
fav=int(input('whats your favorite number \n'))
if fav%2:
    print('your favorite number '+ str(fav)+' is an odd number')
else:
    print('your favorite number '+ str(fav)+' is an even number')
if fav==10:
    print('and its equal to ten')
   
elif fav<10:
     print('and its less than  10')
else:
    print('and its greater than 10')
    
    
