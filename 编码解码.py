# 字符串的编码解码
s = '系统开发工具基础'
# 编码
print(s.encode(encoding='GBK')) # 一个中文字符，两个字节
print(s.encode(encoding='UTF-8')) # 一个中文字符，三个字节

# 解码
byte = b'\xb4\xf3\xba\xd3\xcf\xf2\xb6\xab\xc1\xf7'

print(byte.decode(encoding='GBK'))

byte = b'\xe5\xa4\xa7\xe6\xb2\xb3\xe5\x90\x91\xe4\xb8\x9c\xe6\xb5\x81'
print(byte.decode(encoding='UTF-8'))

