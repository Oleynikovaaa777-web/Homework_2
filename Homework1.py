# page 60:
     
# 12
# a = input('Enter a number')
# if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
#     print('Yes')

# 13
# a = input('Enter a number')
# if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
#     print('Yes')

# 14
# a = input('Enter a number')
# b = input('Enter a number')
# c = input('Enter a number')
#
# if len(a) == 3:
#     print('a = True')
# if len(b) == 3:
#     print('b = True')
# if len(c) == 3:
#     print('c = True')


# 15
# a = input('Enter a number')
# b = input('Enter a number')
# c = input('Enter a number')
#
# if len(a) == 2 and len(b) == 2 and len(c) == 2:
#     print('True')

# 16
# month = int(input('Enter a month in number'))
#
# if month == 12 or month == 1 or month == 2:
#     print('Winter')
# if month == 3 or month == 4 or month == 5:
#         print('Spring')
# if month == 6 or month == 7 or month == 8:
#         print('Summer')
# if month == 9 or month == 10 or month == 11:
#         print('Autumn')
# if month >=13:
#     print('Error')

# 17
# month = int(input('Enter a month in number'))
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print('31 Days')
# if month == 2:
#     print('29 Days')
# if month == 4 or month == 6 or month == 9 or month == 11:
#     print('30 Days')
# if month >=13:
#     print('Error')


# 18
# month = int(input('Enter a month in number'))
# day_of_month = int(input('Enter a day'))
# k = 0
# a = 0
#
#
# if month == 1:
#     k = 364
#
# if month == 3:
#     k = 304
# if month == 5:
#     k = 243
# if month == 7:
#     k = 183
# if month == 8:
#     k = 152
# if month == 10:
#     k = 91
# if month == 12:
#     k = 31
# if month == 2:
#     k = 333
# if month == 4:
#     k = 273
# if month == 6:
#     k = 213
# if month == 9:
#     k = 121
# if month == 11:
#     k = 61
#
# a = k - day_of_month
# print('Before new year days = 'a )


# 18.
# To find month:

# a = 0
# b = 0
# New_year = 366 - 1
# day = 0
#
# month = int(input('Enter a month in number'))
# day_of_month = int(input('Enter a day'))
# month_before_NY = int(12 - month)
#
# if month:
#     day = 31
# if month == 3:
#     day = 31
# if month == 5:
#     day = 31
# if month == 7:
#     day == 31
# if month == 8:
#     day = 31
# if month == 10:
#     day = 31
# if month == 12:
#     day = 31
#
# if month == 2:
#     day = 29
# if month == 4 or month == 6 or month == 9 or month == 11:
#     day = 30
#
# if day_of_month >= 1 and day_of_month <= 31:
#     a = int(day - day_of_month)
# print(a)
# print(month_before_NY)
#
#
# if day_of_month >= 1 and day_of_month <=31:
#     a = int(day - day_of_month)
# print(a)
# print(month_before_NY)


# 19

# player_1_vertical = int(input(put step))
# player_1_horisontal = int(input(put step))
# player_2_vertical = int(input(put step))
# player_2_horisontal = int(input(put step))


# 23
# x = int(input('Enter a number'))
# a = int(input('Ener a number'))
# b = int(input('Enter a number'))
#
# if a <= x <=b:
#     print('Molodec')


# 24
# a * x = b
# a = int(input('Ener a number'))
# b = int(input('Enter a number'))
# x = b//a
#
# if b > 0 and a > 0:
#     print(x)
#
# # Page 53  Ex: 8
#
# if a > b:
#     a = b and a =c  (a = c)
# Answer: Finally a = c. If a < b we will se 'None'
#
#
# if a > b:
#     a = b or a = c (a = b or a = c)
# Answer: If a > b we will see that 'a =b '  but if a < or a = b we will see that 'a = c'

# Absolutely different examples
     