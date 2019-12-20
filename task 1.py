#write a function to compute 5/0 and use try/Except to catch exception
def MyException():
    try:
        5/0
    except:
        print('ZeroDivisionError')
MyException()

