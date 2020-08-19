# Ex. 10-16
# Ex, 5
# page 68-69


# # 10.
# A = input('Enter: ')
# print(A)
# B = A[::-1]
# print(f'reversed A is {B}')
#
# for x in B:
#     print(x)


# 11.
# A = input('Enter: ')
# for x in A:
#     print(x)


# 12.
# input_number = str(float(input('Enter a number: ')))
# input_number_to_list = input_number.split('.')
# decimal_part = (input_number_to_list[1])
# count = 0
#
# for digit in decimal_part:
#     if int(digit) % 2 == 0:
#         count += 1
#
# print(count)


# 13.

# a = (input('Enter a number: '))
# b = a.split('.')
# c = (b[1])
# counter = 0
# for digit in c:
#     if int(digit) == 1:
#         counter += 1
# x = c.count('1') +
# print(counter)


# 14.

# a = (input('Enter a number: '))
# b = a.split('.')
# c = b[1]
# print(c)
# # print(max(c)) +
# max_number = 0
# for digit in c:
#     if int(digit) > max_number:
#         max_number = int(digit)
# print(max_number)

# 15.

# a = (input('Enter a number: '))
# b = a.split('.')
# c = b[1]
# '13927316238912163' => 20

# for index, item in enumerate(c):
#     if index != len(c) - 1:
#         if c[index] == c[index + 1]:
#             print('Got it')
#             break

# index = 0
# while index < len(c) - 1:
#     if c[index] == c[index + 1]:
#         print('Got it')
#         break
#     index += 1

# prev = None
# for digit in c:
#     if prev is not None:
#         if digit == prev:
#             print('Got it')
#             break
#     prev = digit

# 16.
#
a = (input('Enter a number: '))
b = a.split('.')
c = b[1]

standard = c[0]

for digit in c:
    if standard != digit:
        print('Полундра!')
        break


# Ex.5


# 1.    2, 3.....Count will be +1 in total
# 2.    Once
# 3.    Yes