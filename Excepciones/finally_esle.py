# try:
#     a, b = map(int, input().split())
#     res = a / b
#
# except ValueError as k:
#     print(k)
#
# except ZeroDivisionError as k:
#     print(k) # >>> division by zero
#
# # is no mistakes blok esle will worked
# else:
#     print('finished')
#
# # always work, even if no bugs
# finally:
#     print('Finally program is finished')


#         f = open('file.txt')
#         f.write('!!!')
#
# except FileNotFoundError as k:
#     print(k)
#
# except:
#     print('Another mistake')
#
# finally:
#     if f:
#         f.close()
#         print('file closed')
#


def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as k:
        print(k)
        return 0, 0

    finally:
        print('I work before return')

x, y = get_values()
print(x, y)