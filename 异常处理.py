try:
    n1 = int(input('请输入一个整数：'))
    n2 = int(input('请输入另一个整数:'))
    result = n1 / n2
    print('结果为：',result)
except ZeroDivisionError:
    print('除数不可以为0')
except ValueError:
    print('值异常')

except BaseException as e:
    print(e)