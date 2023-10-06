#Modules
import random
import time

#Welcome text

print("Welcome to the national lottery")
print("Your numbers are:")
print("=================")

#Balls

ball1 = 0
ball2 = 0
ball3 = 0
ball4 = 0
ball5 = 0
ball6 = 0

#Ball code
#Ball results are random with 2 sec delay before next ball given

ball1 = random.randint(1,59)
time.sleep(2)
print ("Ball 1 =", ball1)

ball2 = random.randint(1,59)
while ball2 == ball1: 
    ball2= random.randint(1,59)
time.sleep(2)
print ("Ball 2 =", ball2)

ball3 = random.randint(1,59)
while ball3 == ball2 or ball3 == ball1 :
    ball3= random.randint(1,59)
time.sleep(2)
print ("Ball 3 =", ball3)

ball4 = random.randint(1,59)
while ball4 == ball1 or ball4 == ball2 or ball4 == ball3 :
    ball4= random.randint(1,59)
time.sleep(2)
print ("Ball 4 =", ball4)

ball5 = random.randint(1,59)
while ball5 == ball1 or ball5 == ball2 or ball5 == ball3 or ball5 == ball4 :
    ball5= random.randint(1,59)
time.sleep(2)
print ("Ball 5 =", ball5)

ball6 = random.randint(1,59)
while ball6 == ball1 or ball6 == ball2 or ball5 == ball3 or ball6 == ball4 or ball6 == ball5 :
    ball6= random.randint(1,59)
time.sleep(2)
print ("Ball 6 =", ball6)