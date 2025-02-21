import random
n = random.randint(1, 100)
a = -1
gusses = 0
while(a != n):
     gusses =1
     a = int(input("guess a number :"))
     if (a>n):
          print("Lower number please")
          gusses +=1
     elif(a<n):
          print("higher number please")
          gusses +=1

print(f"you have a gussed the number {n} correctly in {gusses} attempted")          



