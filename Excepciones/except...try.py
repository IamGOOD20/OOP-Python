try:
    a, b = map(int, input().split())
    res = a / b



except ValueError:
    print('Must be int type')

except ZeroDivisionError:
    print('Divizion by zero')

except Exception: # I'm base class
    print('I am base class, I can see all exeptions')

except: # I can find all mistakes, only except:
    print('All mistakes')


print('The end')
#print(b)
#print(a)