#coding=utf-8
from uiautomator import Device
import os,csv,time
from time import sleep
# os.popen('python -m uiautomator2 initpython ')
d = Device('00994724')
print(d.info)
phone_number=input('请输入被测试号码: ')
tonghua_time=input('请输入通话时间: ')
jiange_time=input('请输入间隔时间: ')
test_count=input('请输入测试次数: ')
def phone_talk():
    assert_phone=''
    i=0
    while i<int(test_count):
        now_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        try:
            os.popen('adb shell am start -a android.intent.action.CALL -d tel:%s'%phone_number)
            sleep(int(tonghua_time) + 5)
            if phone_number == '10010' or phone_number == '10086':
                if d(resourceId='com.android.dialer:id/holdButton').exists:
                    assert_phone='通话成功'
                else:
                    assert_phone='通话失败'
            else:
                print('测试结果请查看辅助机')
            os.popen('adb shell input keyevent 6')
            i +=1
            #如果 电话号码为运营商号码则写入excel文件
            if phone_number=='10010' or phone_number=='10086':
                with open('autophone.csv', 'a+', newline='')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([i,now_time, assert_phone])
            else:
                pass
            print('正在测试第 %s 次'%i)
            #通话间隔时间
            sleep(int(jiange_time))
            continue
        except Exception as e:
            d.screenshot('test_fail_'+now_time+'.png')
phone_talk()






