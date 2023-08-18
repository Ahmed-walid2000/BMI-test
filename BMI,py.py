print ('please enter your name ')                  # ask for name 
name = input()                                     # input for the name 
print ('please enter your age ')                   # ask for the age 
age = int(input())                                 # input forthe age
print ('please enter your height ')                 # ask for the height 
height =int(input())                                # input for the height 
print ('please enter your weight ')                # ask for the weight 
weight = float(input())                            # input fr the weight
def BMI (name , height , weight):                   # BMI function
    bmi = weight / ((height/100) **2)
    print ('bmi:  ')
    if bmi <= 25:
        print (name +' is not oveweigth ')
    elif bmi < 18:
        print (name +' is underweight ')
    else:
        print(name + ' is overweight ')
    return bmi    
print (BMI (name,height,weight))                  # result for BMI 

