import os ,time
x=('adb devices')
m=os.popen(x)
# print(m)
pp=[]
for lie in m.readlines():
    if "devices"not in lie:
        l=lie.split('device')[0]
        pp.append(l)
# print(pp)


for i in pp:
    print(i)
    pwd = os.getcwd()
    print(pwd)
    os.system('adb -s %s push %s/bbbs/4564 /sdcard/test/4564'%(i,pwd))
    os.system('adb -s %s push %s/ppppp/999+ /sdcard/test/999+' %(i,pwd))
