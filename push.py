#coding=utf-8
import os ,time
import multiprocessing
from multiprocessing import Pool
x=('adb devices')
m=os.popen(x)
# print(m)
pp=[]
for lie in m.readlines():
    if "devices"not in lie:
        l=lie.split('device')[0]
        pp.append(l)
# print(pp)
def push_media(device_name):

        #print(i)
	pwd = os.getcwd()
        # print(pwd)
	os.system('adb -s %s push %s/images/canon_5d2.dng /sdcard/test/images/canon_5d2.dng'%(device_name,pwd))
	os.system('adb -s %s push %s/images/canon_g7x.cr2 /sdcard/test/images/canon_g7x.cr2' %(device_name,pwd))
	os.system('adb -s %s push %s/images/fuji_x20.raf /sdcard/test/images/fuji_x20.raf' %(device_name,pwd))
	os.system('adb -s %s push %s/images/nikon_1aw1.nef /sdcard/test/images/nikon_1aw1.nef' %(device_name,pwd))
	os.system('adb -s %s push %s/images/nikon_p330.nrw /sdcard/test/images/nikon_p330.nrw' %(device_name,pwd))
	os.system('adb -s %s push %s/images/olympus_e_pl3.orf /sdcard/test/images/olympus_e_pl3.orf' %(device_name,pwd))
	os.system('adb -s %s push %s/images/panasonic_gm5.rw2 /sdcard/test/images/panasonic_gm5.rw2' %(device_name,pwd))
	os.system('adb -s %s push %s/images/pentax_k5.pef /sdcard/test/images/pentax_k5.pef' %(device_name,pwd))
	os.system('adb -s %s push %s/images/sample_1mp.dng /sdcard/test/images/sample_1mp.dng' %(device_name,pwd))
	os.system('adb -s %s push %s/images/samsung_nx3000.srw /sdcard/test/images/samsung_nx3000.srw' %(device_name,pwd))
	os.system('adb -s %s push %s/images/sony_rx_100.arw /sdcard/test/images/sony_rx_100.arw' %(device_name,pwd))
	os.system('adb -s %s push %s/images/image_exif_byte_order_ii.jpg /sdcard/test/images/image_exif_byte_order_ii.jpg' %(device_name,pwd))
	os.system('adb -s %s push %s/images/image_exif_byte_order_mm.jpg /sdcard/test/images/image_exif_byte_order_mm.jpg' %(device_name,pwd))
	os.system('adb -s %s push %s/images/lg_g4_iso_800.dng /sdcard/test/images/lg_g4_iso_800.dng' %(device_name,pwd))
	os.system('adb -s %s push %s/images/volantis.jpg /sdcard/test/images/volantis.jpg' %(device_name,pwd))
	print("copying 1920x1080")
	os.system('adb -s %s push %s/bbb_short/1920x1080 /sdcard/test/bbb_short/1920x1080' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_full/1920x1080 /sdcard/test/bbb_full/1920x1080' %(device_name,pwd))
	print("copying 1280x720")
	os.system('adb -s %s push %s/bbb_short/1280x720 /sdcard/test/bbb_short/1280x720' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_full/1280x720 /sdcard/test/bbb_full/1280x720' %(device_name,pwd))
	print("copying 720x480")
	os.system('adb -s %s push %s/bbb_short/720x480 /sdcard/test/bbb_short/720x480' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_full/720x480 /sdcard/test/bbb_full/720x480' %(device_name,pwd))
	print( "copying all others")
	os.system('adb -s %s push %s/bbb_short/176x144 /sdcard/test/bbb_short/176x144' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_full/176x144 /sdcard/test/bbb_full/176x144' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_short/480x360 /sdcard/test/bbb_short/480x360' %(device_name,pwd))
	os.system('adb -s %s push %s/bbb_full/480x360 /sdcard/test/bbb_full/480x360' %(device_name,pwd))

if __name__ == "__main__":
    # 创建进程池为设备数量
    p = Pool(len(pp)-1)
    # for i in range(len(pp)-1):
    for m in pp[0:len(pp)-1]:
        p.apply_async(push_media, (m,))  # 增加新的进程
            # print('this is m %s'%m)
    p.close()  # 禁止在增加新的进程
    p.join()
print('\n'.join([''.join([('successful!'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

