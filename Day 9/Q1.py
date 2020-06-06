#1.Write a function to compute divide by zero and use try/except to catch the exceptions.

def div(a,b):
    try:
        c=a/b
        print(c)
    except Exception as e:
        print('Exception:',e)

div(7,0)
div(7,1)
div(0,1)
