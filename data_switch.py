
from uiautomator import Device
import os,csv,time
from time import sleep
# os.popen('python -m uiautomator2 initpython ')
d = Device('00994724')
count = input('请输入测试次数 : ')
jiange_time=input('请输入间隔时间 : ')
d(descriptionContains='Apps').click()
d(scrollable=True).scroll.vert.to(text="Settings")
d(descriptionContains='Settings' ).click()
d(text='Data usage').click()
time.sleep(2)
def data_use():
    test=0
    while test<int(count):
        global csv_result
        try:
            now_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
            d(resourceId='android:id/switch_widget').click()
            result=(d(resourceId='android:id/switch_widget').text)
            if result=='OFF':
                csv_result = '测试成功'
                print('第%s次测试成功'%test)
            else:
                csv_result = '测试失败'
                print('第%s次测试失败'%test)
            test +=1
            with open('E:\\unittest\\ui_test\\data_use.csv', 'a+', newline='')as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([test, now_time, csv_result])
            time.sleep(int(jiange_time))
            d(resourceId='android:id/switch_widget').click()
            result=(d(resourceId='android:id/switch_widget').text)
            if result=='ON':
                csv_result='测试成功'
                print('第%s次测试成功' % test )
            else:
                csv_result = '测试失败'
                print('第%s次测试失败' % test )
            test += 1
            time.sleep(int(jiange_time))
            with open('E:\\unittest\\ui_test\\data_use.csv', 'a+', newline='')as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([test, now_time, csv_result])
        except Exception as e:
            d.screenshot(test.png)
        continue
if __name__=='__main__':
    data_use()



