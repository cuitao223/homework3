def cale(a,b): # a,b为形参
    return a + b

if __name__ == '__main__':
    a = cale(10,20) # 10,20 是实参
    print(a)
    b = cale(b=100,a=10) 
    print(b)
