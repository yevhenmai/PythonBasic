import sys




# user_input = int(input( " Enter 4 digits number"))
# print(user_input)
# print(type(user_input))
# user_1000 = user_input // 1000
# print(user_1000)
# user_200 = user_input // 580
# print(user_200)
# user_3 = user_input // 400
# print(user_3)
# user_4 = user_input // 300
# print(user_4)
# 2 DZ
user_input = int(input( " Enter 5 digits number"))
user_num1 = (user_input // 10000) % 10
print(user_num1)
user_num2 = (user_input // 1000) % 10
print(user_num2)
user_num3 = (user_input // 100) % 10
print(user_num3)
user_num4 = (user_input // 10) % 10
print(user_num4)
user_num5 = (user_input // 1) % 10
print(user_num5)

all_num = user_num5 * 10000 + (user_num4 *1000) + (user_num3 * 100) + (user_num2 * 10) +(user_num1 * 1)
print(all_num)