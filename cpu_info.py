#coding=utf-8
import os,time,csv


class Laun_app():
    def __init__(self):
        self.mems=''
    def launch_app(self):
        now_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cmd=os.popen('adb shell dumpsys cpuinfo | grep com.huawei.camera')
        for line in cmd.readlines():
            with open('cpu.csv', 'a+', newline='')as f:
                if 'com.huawei.camera' in line:
                    sx=line.split('%')
                    print(sx[0])
                    writer = csv.writer(f)
                    writer.writerow([now_time,sx[0]])


if __name__ == "__main__":
    test=Laun_app()
    for i in range(0,11,1):
        test.launch_app()
        # test.stop_app()
        time.sleep(5)