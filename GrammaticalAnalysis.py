#str转list测试
a=open('./OutFile','r')

c=a.readlines()

b=c.strip('[').strip(']').split(',')

print(b)

a.close()
