with open('example.txt', 'r') as file:
    content = file.read()  # 读取整个文件内容
    print(content)

with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # 写入内容到文件