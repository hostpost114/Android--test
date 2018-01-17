#coding=utf-8
import os,time,csv


class Laun_app():
    def __init__(self):
        self.mems=''
    def launch_app(self):
        cmd=os.popen('adb shell am start -W -n com.huawei.camera/com.huawei.camera')

        #退出後臺操作
        #cmd = os.popen('adb shell am force-stop com.huawei.camera')


        for line in cmd.readlines():
            with open('app-start.csv', 'a+', newline='')as f:
                if 'ThisTime' in line:
                    sx=line.split(":")
                    print(sx[0:2])
                    writer = csv.writer(f)
                    writer.writerow(sx[0:2])
    #返回app
    def stop_app(self):
        os.popen('adb shell input keyevent 3')
if __name__ == "__main__":
    test=Laun_app()
    for i in range(0,11,1):
        test.launch_app()
        test.stop_app()
        time.sleep(5)