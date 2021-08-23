#https://www.codecademy.com/courses/learn-python-3/projects/python-sals-shipping
#Magic 8-Ball
#####################################################
#random_number = random.randint(1,9)#從1至9中產生隨機數
#print(name + " asks: " + question)
#print(f"Random number: {random_number}")#f-string
# int(string) 将字符串转换成 int 类型；
# float(string) 将字符串转换成 float 类型；
# bool(string) 将字符串转换成 bool 类型。
######################################################
import sys

weight = 0#lb
Ground_shipping_cost = 0 
Ground_shipping_premium_cost = 0
Drone_shipping_cost = 0
Total_shipping_cost = Ground_shipping_cost + Ground_shipping_premium_cost + Drone_shipping_cost

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~Wellcome~!~~~~~~~~~~~~~~~~~~~~~")
print("The biggest shipping company in the tri-county area!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------------------Ground Shipping-------------------")
#weight = int(input("""Ground Shipping:
#How many weight(lb) of Ground Shipping?
#"""))#int()
userInput = input("""Ground Shipping:
How many weight(lb) of Ground Shipping?
""")
#轉換用戶輸入為數字float/int
weight = float(userInput)
# if isinstance(userInput, int):
#     weight = int(userInput)
# else:
#     print("Error!")
#not use
if weight <=2:
    Ground_shipping_cost = (weight * 1.5) + 20
    Ground_shipping_cost_weight = "* $1.50(lb) + Flat Charge:$20"
elif weight <=6:
    Ground_shipping_cost = (weight * 3) + 20
    Ground_shipping_cost_weight = "* $3(lb) + Flat Charge:$20"
elif weight <=10:
    Ground_shipping_cost = (weight * 4) + 20
    Ground_shipping_cost_weight = "* $4(lb) + Flat Charge:$20"
elif weight >=10:
    Ground_shipping_cost = (weight * 4.75) + 20
    Ground_shipping_cost_weight = "* $4.75(lb) + Flat Charge:$20"
else:
    print("Error!")
    sys.exit("Error!Please input Num.")
print(f"- Ground Shipping Cost: ${Ground_shipping_cost}")

userInput = input("""Ground Shipping:
Do your Ground Shipping need Premium service?
Please input Yes or No.
""")
if userInput == "Yes":
    Ground_shipping_premium_cost = 125
elif userInput == "Y":
    Ground_shipping_premium_cost = 125
elif userInput == "yes":
    Ground_shipping_premium_cost = 125
elif userInput == "y":
    Ground_shipping_premium_cost = 125
elif userInput == "No":
    Ground_shipping_premium_cost = 0
elif userInput == "N":
    Ground_shipping_premium_cost = 0
elif userInput == "no":
    Ground_shipping_premium_cost = 0
elif userInput == "n":
    Ground_shipping_premium_cost = 0
else:
    sys.exit("Error!Please input Yes or No.")
Ground_shipping_premium_cost = float(Ground_shipping_premium_cost)
print("----------------------------------------------")
print(f"- Ground Shipping Cost: {weight}lb {Ground_shipping_cost_weight} = ${Ground_shipping_cost}")
print(f"- Premium: ${Ground_shipping_premium_cost}")
print("----------------------------------------------")
Ground_shipping_total = Ground_shipping_cost + Ground_shipping_premium_cost
print(f"*****Ground Shipping Total Cost: ${Ground_shipping_total} *****")
print("----------------------------------------------")

userInput = input("""Drone Shipping:
How many weight(lb) of Drone Shipping?
""")
weight_d = float(userInput)
if weight_d <=2:
    Drone_shipping_cost = (weight_d * 4.5)
    Drone_shipping_cost_weight_d = "* $4.50(lb) + Flat Charge:$0"
elif weight_d <=6:
    Drone_shipping_cost = (weight_d * 9)
    Drone_shipping_cost_weight_d = "* $9(lb) + Flat Charge:$0"
elif weight_d <=10:
    Drone_shipping_cost = (weight * 12)
    Drone_shipping_cost_weight_d = "* $12(lb) + Flat Charge:$0"
elif weight_d >=10:
    Drone_shipping_cost = (weight * 14.25)
    Drone_shipping_cost_weight_d = "* $4.75(lb) + Flat Charge:$0"
else:
    print("Error!")
    sys.exit("Error!Please input Num.")
    
print("----------------------------------------------")
print(f"- Ground Shipping Cost: {weight}lb {Ground_shipping_cost_weight} = ${Ground_shipping_cost}")
print(f"- Premium: ${Ground_shipping_premium_cost}")
print("----------------------------------------------")
Ground_shipping_total = Ground_shipping_cost + Ground_shipping_premium_cost
print(f"*****Ground Shipping Total Cost: ${Ground_shipping_total} *****")
print("----------------------------------------------")
print(f"- Drone Shipping Cost: {weight_d}lb {Drone_shipping_cost_weight_d} = ${Drone_shipping_cost}")
print("----------------------------------------------")
print(f"*****Drone Shipping Total Cost: ${Drone_shipping_cost} *****")
print("----------------------------------------------")
Total_shipping_cost = Ground_shipping_cost + Ground_shipping_premium_cost + Drone_shipping_cost
print(f"""*****Ground Shipping: ${Ground_shipping_total}*****
****+Drone Shipping:  ${Drone_shipping_cost}*****""")
print("----------------------------------------------")
print(f"*****Total Cost:      ${Total_shipping_cost} *****")
print("----------------------------------------------")

# Sal's Shipping
# Sonny Li

# weight = 80

# #Ground Shipping 🚚

# if weight <= 2:
#   cost_ground = weight * 1.5 + 20
# elif weight <= 6:
#   cost_ground = weight * 3.00 + 20
# elif weight <= 10:
#   cost_ground = weight * 4.00 + 20
# else:
#   cost_ground = weight * 4.75 + 20

# print("Ground Shipping $", cost_ground)
      
# # Ground Shipping Premimum 🚚💨

# cost_ground_premium = 125.00

# print("Ground Shipping Premimium $", cost_ground_premium)

# # Drone Shipping 🛸

# if weight <= 2:
#   cost_drone = weight * 4.5
# elif weight <= 6:
#   cost_drone = weight * 9.00
# elif weight <= 10:
#   cost_drone = weight * 12.00
# else:
#   cost_drone = weight * 14.25

# print("Drone Shipping: $", cost_drone)