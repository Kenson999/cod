#https://www.codecademy.com/courses/learn-python-3/projects/python-magic-8-ball
#Magic 8-Ball
#####################################################
#random_number = random.randint(1,9)#從1至9中產生隨機數
#print(name + " asks: " + question)
#print(f"Random number: {random_number}")#f-string
######################################################
import random#加入工具

name = "Kenson"
question = "Eat SUSHI?"
answer = ""

random_number = random.randint(1,9)#從1至9中產生隨機數
print(f"Random number: {random_number}")
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so." 
elif random_number == 3:
    answer = "Without a doubt." 
elif random_number == 4:
    answer = "Reply hazy, try again." 
elif random_number == 5:
    answer = "Ask again later." 
elif random_number == 6:
    answer = "Better not tell you now." 
elif random_number == 7:
    answer = "My sources say no." 
elif random_number == 8:
    answer = "Outlook not so good." 
elif random_number == 9:
    answer = "Very doubtful." 
else:
    answer = "Error!"
    
print(name + " asks: " + question)
print(f"Random number: {random_number}")#f-string
print("Random number:",random_number)
print("Magic 8-Ball's answer:" + answer)
