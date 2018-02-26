from multiprocessing import Pool

import os ,time
x=('adb devices')
m=os.popen(x)
# print(m)
pp=[]
for lie in m.readlines():
    if "devices"not in lie:
        l=lie.split('device')[0]
        pp.append(l)
print(len(pp)-1)
def push_media(device):
    # for i in pp:
    #     # print(i)
    pwd = os.getcwd()
    # print(pwd)
    os.system('adb -s %s push %s/bbbs/4564 /sdcard/test/4564' % (device, pwd))
    os.system('adb -s %s push %s/jdk-8u151-linux-x64.tar.gz /sdcard/test/jdk-8u151-linux-x64.tar.gz' % (device, pwd))
    os.system('adb -s %s push %s/node-v9.4.0-linux-x64.tar.xz /sdcard/test/node-v9.4.0-linux-x64.tar.xz' % (device, pwd))
    os.system('adb -s %s push %s/Postman-linux-x64-5.5.0.tar.gz /sdcard/test/Postman-linux-x64-5.5.0.tar.gz' % (device, pwd))
    os.system('adb -s %s push %s/pycharm-professional-2017.3.2.tar.gz /sdcard/test/pycharm-professional-2017.3.2.tar.gz' % (device, pwd))
    print(666666666)



if __name__ == "__main__":
    print("Current process is %d" % (os.getpid()))
    p = Pool()
    # for i in range(len(pp)-1):
    for m in pp[0:len(pp)-1]:
        p.apply_async(push_media, (m,))  # 增加新的进程
            # print('this is m %s'%m)
    p.close()  # 禁止在增加新的进程
    p.join()
    print("pool process done")
