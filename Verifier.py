from uiautomator import Device
from HTMLTestRunner import HTMLTestRunner
import unittest , os ,time
from time import sleep
d=Device('a4d9cedd')

#设备SN号，一般最后的设备需要修改为辅助机器，前面的为测试机
list=['a4d9cedd','ca42aa7e']
d(resourceId="com.android.launcher3:id/all_apps_handle").click()
d(text='CTS Verifier').click()
#异常处理函数单独写出来调用，以免重复书写
def except_deal():
    #如果有报停的 应该重启apk

    if d.exists(text='CTS Verifier has stopped') == True:
        d(text='Open app again').click()
    else:
        os.popen('adb -s %s shell am force-stop com.android.cts.verifier'% list[0])
class Verifier_test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        sleep(6)
        os.popen('adb -s %s shell am force-stop com.android.cts.verifier'% list[0])
        sleep(6)
        os.popen('adb -s %s shell am start -n com.android.cts.verifier/.CtsVerifierActivity'%list[0])
        sleep(3)
    #apk重启写一个函数
    #测试telephony模块第一条用例

    def test_A_telephony_001(self):
        try:
            d(scrollable=True).scroll.to(text="Dialer Receives Incoming Call")
            d(text='Dialer Receives Incoming Call').click()
            #d(text="This test verifies that the default dialer can receive incoming calls after it has been set.").click()
            #判断是否为首次进入
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            #点击SET CTS VERIFIER AS DEFUALT DIALER按钮
            d(text='SET CTS VERIFIER AS DEFAULT DIALER').click()
            d(text='SET DEFAULT').click()#"""暂时遗留，需要辅助机器配合"""
            # 可以更改代码，，，，把测试机号码写在外边d
            os.popen('adb -s %s shell am start -a android.intent.action.CALL -d tel:18682205039' % list[1])
            sleep(13)
            os.popen('adb -s %s shell input keyevent 6'%list[1])
            sleep(0.5)
            d(text='RESTORE THE DEFAULT DIALER').click()
            if d.exists(text="SET DEFAULT") == False:
                pass
            else:
                d(text='SET DEFAULT').click()
            if d(descriptionContains='Pass').enabled ==True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e:
            #如果报错，可以增加截图重启apk
            if d.exists(text='CTS Verifier has stopped')==True:
                d(text='Open app again').click()
            else:
                pass
            print(e)
    #测试phone模块第二条用例

    def test_A_telephony_002(self):
        try:
            d(scrollable=True).scroll.to(text="Dialer Shows HUN on Incoming Call")
            d(text="Dialer Shows HUN on Incoming Call").click()
            if d.exists(text="OK") == False:  # 判断是否为首次进入
                pass
            else:
                d(text='OK').click()
            d(text='SET CTS VERIFIER AS DEFAULT DIALER').click()
            # if d.exists(text="SET DEFAULT") == False:
            #     pass
            # else:
            #     d(text='SET DEFAULT').click()
            d(text='SET DEFAULT').click()
            # 可以更改代码，，，，把测试机号码写在外边
            os.popen('adb -s %s shell am start -a android.intent.action.CALL -d tel:18682205039'%list[1])
            sleep(11)
            # 判断通知栏是否符合用例要求
            if d.exists(text='CTS Incoming Call Notification') == True:
                d(text='HUN shown and meets criteria specified above.').click()
            else:
                d(descriptionContains='Fail').click()
            # 恢复到verifier界面
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
            os.popen('adb -s ca42aa7e shell input keyevent 6')
        #异常处理，如果有需求可以增加截图处理
        except Exception as e:
            except_deal()
            print(e)
    #测试phone模块第三条用例

    def test_A_telephony_003(self):
        sleep(5)
        try:
            d(scrollable=True).scroll.to(text="Hide settings in voicemail test")
            d(text="Hide settings in voicemail test").click()
            if d.exists(text="OK") == False:  #判断是否为首次进入
                pass
            else:
                d(text='OK').click()
            d(text='OPEN VOICEMAIL SETTINGS').click()
            if d.exists(text='RINGTONE SETTINGS') == False:
                os.popen('adb -s %s shell  input keyevent 4'%list[0])
                d(text='RINGTONE SETTINGS DOES NOT EXIST').click()
            else:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(text='RINGTONE SETTINGS EXISTS').click()
        except Exception as e:
            except_deal()
            print(e)
    #测试phone模块第四条用例

    def test_A_telephony_004(self):
        try:
            d(scrollable=True).scroll.to(text="Hide voicemail in call settings test")
            d(text="Hide voicemail in call settings test").click()
            if d.exists(text="OK") == False:  # 判断是否为首次进入
                pass
            else:
                d(text='OK').click()
            d(text='OPEN CALL SETTINGS').click()
            #检查是否存在voicemail
            if d.exists(text='Voicemail') == False:    # 进入通话设置中查看语音信箱缩写。。。
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(text='"VOICEMAIL" DOES NOT EXIST').click()
            else:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(text='"VOICEMAIL" EXISTS').click()
        except Exception as e:
            except_deal()
            print(e)
    #测试phone模块第五条用例

    def test_A_telephony_005(self):
        try:
            d(scrollable=True).scroll.to(text="System Implements Telecom Intents")
            d(text="System Implements Telecom Intents").click()
            if d.exists(text="OK") == False:  # 判断是否为首次进入
                pass
            else:
                d(text='OK').click()
            d(text="LAUNCH CALL SETTINGS").click()
            #判断是否进入到通话设置界面
            if d.exists(text="Call settings")==True:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(resourceId="com.android.cts.verifier:id/dialer_telecom_intents_call_settings_check_box").click()
            else:
                pass
            #第二步
            d(text="LAUNCH SHORT SMS ANSWER SETTINGS").click()
            # 判断是否进入到快速回复设置界面
            if d.exists(text="Edit quick responses") == True:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(resourceId="com.android.cts.verifier:id/dialer_telecom_intents_short_sms_check_box").click()
            else:
                pass
            #第三步
            d(text="LAUNCH CALLING ACCOUNTS SETTINGS").click()
            # 判断是否进入到通话账户设置界面
            if d.exists(text="Calling accounts") == True:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(resourceId="com.android.cts.verifier:id/dialer_telecom_intents_calling_accounts_check_box").click()
            else:
                pass
            #第四步
            sleep(2)
            d(scrollable=True).scroll.to(descriptionContains="Info" )
            d(text="LAUNCH ACCESSIBILITY SETTINGS").click()
            # 判断是否进入到通话辅助功能设置界面
            if d.exists(text="Accessibility") == True:
                os.popen('adb -s %s shell  input keyevent 4' % list[0])
                d(resourceId="com.android.cts.verifier:id/dialer_telecom_intents_accessibility_settings_check_box").click()
            else:
                pass
            #如果存在复选框未勾选的情况直接打fail
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e :
            except_deal()
            print(e)
    #跳过测试项第六、七条，因为需要插拔sim卡
    @unittest.skip('sim卡')
    def test_A_telephony_007(self):
        try:
            d(scrollable=True).scroll.to(text="Voicemail Broadcast Test")
            d(text='Voicemail Broadcast Test').click()
            if d.exists(text="OK") == False:  # 判断是否存在弹框
                pass
            else:
                d(text='OK').click()
            d(text='SET CTS VERIFIER AS DEFAULT DIALER').click()
        except Exception as e:
            pass
    """TELECOM---模块测试"""


    def test_B_telecom_001(self):
        try:
            d(scrollable=True).scroll.to(text="Incoming Self-Managed Connection Test")
            d(text='Incoming Self-Managed Connection Test').click()
            if d.exists(text="OK") == False:  # 判断是否存在弹框
                pass
            else:
                d(text='OK').click()
            d(text='REGISTER SELF-MANAGED CONNECTIONSERVICE').click()
            sleep(1)
            d(text='SHOW SYSTEM INCOMING UI').click()
            sleep(0.5)
            d(text='ANSWER').click()
            d(text='CONFIRM ANSWER').click()
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e :
            except_deal()
            print(e)

    def test_B_telecom_002(self):
        sleep(3)
        try:
            d(scrollable=True).scroll.to(text="Telecom Enable Phone Account Test")
            d(text='Telecom Enable Phone Account Test').click()
            if d.exists(text="OK") == False:  # 判断是否存在弹框
                pass
            else:
                d(text='OK').click()
            d(text='REGISTER PHONE ACCOUNT').click()
            #打开通话设置
            os.popen('adb -s %s shell am start -n com.android.dialer/.app.DialtactsActivity'%list[0])
            sleep(2)
            d(resourceId="com.android.dialer:id/dialtacts_options_menu_button").click()
            d(text="Settings").click()
            d(text="Calling accounts").click()
            d(text="All calling accounts").click()
            #激活ctsverifier
            d(text='CTS Verifier Test').click()
            #回退到verifier界面
            sleep(3)
            os.popen('adb -s %s shell input keyevent 4'%list[0])
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(2)
            d(text="CONFIRM").click()
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e :
            except_deal()
            print(e)

    def test_B_telecom_003(self):
        try:
            d(scrollable=True).scroll.to(text="Telecom Incoming Call Test")
            d(text='Telecom Incoming Call Test').click()
            if d.exists(text="OK") == False:  # 判断是否存在弹框
                pass
            else:
                d(text='OK').click()
            d(text='REGISTER AND ENABLE PHONE ACCOUNT').click()
            #进入通话设置
            d(text="All calling accounts").click()
            # 激活ctsverifier
            d(text='CTS Verifier Test').click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text='CONFIRM PHONE ACCOUNT').click()
            d(text='DIAL').click()
            d(text='ANSWER').click()
            sleep(3)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text='CONFIRM').click()
            #下拉屏幕到底部
            d(scrollable=True).scroll.to(descriptionContains="Info")
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

    def test_B_telecom_004(self):
        try:
            d(scrollable=True).scroll.to(text="Telecom Outgoing Call Test")
            d(text='Telecom Outgoing Call Test').click()
            if d.exists(text="OK") == False:  # 判断是否存在弹框
                pass
            else:
                d(text='OK').click()
            d(text='REGISTER AND ENABLE PHONE ACCOUNT').click()
            d(text="All calling accounts").click()
            # 激活ctsverifier,如果是激活状态则不做操作，，避免上一条用例失败后影响此用例
            if d(resourceId="android:id/switch_widget").text == "ON":
                pass
            else:
                d(resourceId="android:id/switch_widget").click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            #选择默认通话账户为verifier
            d(text='Make calls with').click()
            d(text="CTS Verifier Test").click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text='CONFIRM PHONE ACCOUNT').click()
            d(text='DIAL').click()
            sleep(2)
            d(resourceId="com.android.dialer:id/dialpad_floating_action_button").click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            d(text='CONFIRM').click()
            d(scrollable=True).scroll.to(descriptionContains="Info")
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    """SENSOR---模块测试"""
    # 测试sensor模块第一条用例
    def test_K_sensor_001(self):
        try:
            d(scrollable=True).scroll.to(text="Device Suspend Tests")
            sleep(2)
            d(text='6DoF Test').click()
        except Exception as e:
            except_deal()
            print(e)
    # 测试sensor模块第二条用例
    def test_K_sensor_002(self):
        try:
            d(scrollable=True).scroll.to(text="Device Suspend Tests")
            sleep(2)
            d(text='Accelerometer Measurement Tests').click()
            d(text="NEXT").click()
            # 如果飞行模式开关为激活状态则忽略，反之激活飞行模式
            if d(resourceId="android:id/switch_widget").text == 'OFF':
                d(resourceId='android:id/switch_widget').click()
            else:
                pass
            os.popen('adb -s %s shell input keyevent 4'%list[0])
            d(text="NEXT").click()
            d(scrollable=True).scroll.to(text="Auto-rotate screen")
            d(text="Auto-rotate screen").click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text="NEXT").click()
            sleep(1)
            d(text="Stay awake").click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text="NEXT").click()
            d(text="On").click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            d(text="NEXT").click()
            sleep(5)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
        except Exception as e:
            print(e)
    # 测试sensor模块第三条用例
    def test_K_sensor_003(self):
        try:
            d(scrollable=True).scroll.to(text="Device Suspend Tests")
            if d(text='Device Suspend Tests').exists:
                d(text='Device Suspend Tests').click()
            else:
                pass
            d(text="NEXT").click()
            if d(text="Activate this device admin app").exists:
                d(text="Activate this device admin app").click()
            else:
                pass
            d(text="NEXT").click()
            sleep(170)
            if d(text="FAIL").exists:
                d(text="FAIL").click()
            else:
                d(text='PASS').click()
        except Exception as e:
            except_deal()
            print(e)
    def test_K_sensor_004(self):
        try:
            d(scrollable=True).scroll.to(text="Dynamic Sensor Discovery Test")
            if d(text='Dynamic Sensor Discovery Test').exists:
                d(text='Dynamic Sensor Discovery Test').click()
            else:
                pass
            d(text="NEXT").click()
            if d(text="FAIL").exists:
                d(text="FAIL").click()
            else:
                d(text='PASS').click()
        except Exception as e:
            except_deal()
            print(e)
    #第五、六条测试用例需要旋转手机，，，跳过去
    @unittest.skip
    def test_K_sensor_007(self):
        d(scrollable=True).scroll.to(text="Off Body Sensor Tests")
        d(text="Off Body Sensor Tests").click()
        d(text="NEXT").click()
    #第八条open——cv不测
    def test_K_sensor_009(self):
        try:
            d(scrollable=True).scroll.to(text="Sensor Batching Manual Tests")
            d(text='Sensor Batching Manual Tests').click()
            d(text="NEXT").click()
            d(text="NEXT").click()
            sleep(15)
            d(text="NEXT").click()
            sleep(10)
            d(text="NEXT").click()
            sleep(40)
            d(text="NEXT").click()
            sleep(20)
            d(text="NEXT").click()
            sleep(40)
            d(text="NEXT").click()
            sleep(20)

            if d(text="FAIL").exists:
                d(text='FAIL').click()
            else:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
        except Exception as e:
                except_deal()
                print(e)
    #projection模块
    def test_C_projection_test_001(self):
        try:
            d(scrollable=True).scroll.to(text="Projection Cube Test")
            d(text='Projection Cube Test').click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            sleep(3)
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e:
            except_deal()
            print(e)
    def test_C_projection_test_003(self):
        try:
            d(scrollable=True).scroll.to(text="Projection Offscreen Activity")
            d(text='Projection Offscreen Activity').click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d.screen.off()
            sleep(6)
            d.screen.on()
            d(resourceId="com.android.systemui:id/lock_icon").click()
            if d(descriptionContains='Pass').enabled == True:
                d(descriptionContains='Pass').click()
            else:
                d(descriptionContains='Fail').click()
        except Exception as e:
            except_deal()
            print(e)
    def test_C_projection_test_004(self):
        try:
            d(scrollable=True).scroll.to(text="Projection Scrolling List Test")
            d(text='Projection Scrolling List Test').click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(scrollable=True).fling.toEnd()
            if d(resourceId='com.android.cts.verifier:id/pass_button').enabled == True:
                d(resourceId='com.android.cts.verifier:id/pass_button').click()
            else:
                d(resourceId='com.android.cts.verifier:id/fail_button').click()
        except Exception as e:
            except_deal()
            print(e)
    #nitification 模块
    def test_L_notifications_test_001(self):
        try:
            d(scrollable=True).scroll.to(text="CA Cert Notification Test")
            d(text='CA Cert Notification Test').click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="Use the CertInstaller to install the certificate MyCA.cer from device storage. When it opens, choose any name and tap Okay. If this button does nothing, pass the test and move on.").click()
            d(text="GO").click()
            sleep(1)
            d(descriptionContains="Show roots").click()
            sleep(1)
            # 进入到内部存储中寻找安装ca证书
            d(text="msm8953 for arm64").click()
            d(scrollable=True).scroll.toEnd()
            d(text="myCA.cer").click()
            d(resourceId="com.android.certinstaller:id/credential_name").set_text('test')
            sleep(1)
            d(text="OK").click()
            sleep(1)
            d(text="OK").click()
            # 选择不使用指纹锁
            d(text="Continue without fingerprint").click()
            d(text="PIN").click()
            d(text="YES").click()
            d(text="OK").click()
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            d(text="NEXT").click()
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            d(text="OK").click()
            d(text="DONE").click()
            d(text='PASS').click()
            sleep(1)
            # 第二条
            d(text="Visit the user-installed trusted credentials page and confirm that the Internet Widgits Pty Ltd cert appears in the list.").click()
            d(text="GO").click()
            sleep(6)
            if d(text="Internet Widgits Pty Ltd").exists == True:
                os.popen('adb -s %s shell input keyevent 4' % list[0])
                d(text='PASS').click()
            else:
                os.popen('adb -s %s shell input keyevent 4'%list[0])
                d(text='FAIL').click()
            # 第三条
            d(text="You may have been prompted to set a screen lock when installing the certificate. If so, remove it. If not, you may skip this step.").click()
            d(text="GO").click()
            sleep(1)
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            os.popen('adb -s %s shell input keyevent 66'%list[0])
            d(text="Continue without fingerprint").click()
            d(text="None").click()
            d(text="YES, REMOVE").click()
            d(text='PASS').click()
            # disitiao
            sleep(2)
            d(index="3").click()
            sleep(2)
            d(index='4').click()
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    @unittest.skip('重启后需要输入密码，，，，adb不能连接')
    def test_L_notifications_test_002(self):
        try:
            d(text="CA Cert Notification on Boot test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
                d(text="CHECK CREDENTIALS").click()
                sleep(1)
                if d(text="Internet Widgits Pty Ltd").exists:
                    os.popen('adb -s %s shell input keyevent 4' % list[0])
                    sleep(1)
                    os.popen('adb -s %s reboot' % list[0])
                    sleep()
                else:
                    os.popen('adb -s %s shell input keyevent 4' % list[0])
                    d(descriptionContains='Fail').click()
        except Exception as e:
            except_deal()
            print(e)
    def test_L_notifications_test_003(self):
        try:
            d(scrollable=True).scroll.to(text="Condition Provider test")
            d(text="Condition Provider test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="LAUNCH SETTINGS").click()
            d(text="CTS Verifier").click()
            sleep(1)
            d(text="ALLOW").click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            d(scrollable=True).scroll.toEnd()
            sleep(58)
            d(text="LAUNCH SETTINGS").click()
            d(text="CTS Verifier").click()
            sleep(1)
            d(text='OK').click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(12)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_L_notifications_test_004(self):
        try:
            d(scrollable=True).scroll.to(text="Notification Attention Management Test")
            d(text="Notification Attention Management Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="LAUNCH SETTINGS").click()
            d(text="CTS Verifier").click()
            sleep(1)
            d(text="ALLOW").click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            d(scrollable=True).scroll.toEnd()
            sleep(120)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

    def test_L_notifications_test_005(self):
        try:
            d(scrollable=True).scroll.to(text="Notification Listener Test")
            d(text="Notification Listener Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(scrollable=True).scroll.toEnd()
            sleep(150)
            d(text="LAUNCH SETTINGS").click()
            d(text="CTS Verifier").click()
            sleep(1)
            d(text="TURN OFF").click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(20)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

    def test_L_notifications_test_006(self):
        try:
            d(scrollable=True).scroll.to(text="Shortcut Reset Rate-limiting Test")
            d(text="Shortcut Reset Rate-limiting Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            sleep(20)
            d.open.notification()
            sleep(1)
            d(text="TYPE SOMETHING HERE AND PRESS SEND BUTTON").click()
            sleep(2)
            d(text="Type something here and press send button").set_text(1234)
            sleep(1)
            d(resourceId="com.android.systemui:id/remote_input_send").click()
            sleep(10)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    #location模块测试
    def test_L_location_test_001(self):
        try:
            d(scrollable=True).scroll.to(text="Location Mode Off Test")
            d(text="Location Mode Off Test").click()

            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            d(text="Location Mode Off Test").click()
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

    def test_L_location_test_002(self):
        try:
            d(scrollable=True).scroll.to(text="Battery Saving Mode Test")
            d(text="Battery Saving Mode Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(index="5").click()
            sleep(2)
            if d(resourceId="com.android.settings:id/switch_bar").text == 'Off':
                d(resourceId="com.android.settings:id/switch_bar").click()
            else:
                pass
            sleep(2)
            d(text="Mode").click()
            sleep(1)
            d(text="Battery saving").click()
            sleep(2)
            if d(text="AGREE").exists:
                d(text="AGREE").click()
            else:
                pass
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_L_location_test_003(self):
        try:
            d(scrollable=True).scroll.to(text="Device Only Mode Test")
            d(text="Device Only Mode Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(index="5").click()
            d(text="Mode").click()
            sleep(1)
            d(text="Device only").click()
            sleep(2)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_L_location_test_004(self):
        try:
            d(scrollable=True).scroll.to(text="High Accuracy Mode Test")
            d(text="High Accuracy Mode Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(index="5").click()
            d(text="Mode").click()
            sleep(1)
            d(text="High accuracy").click()
            sleep(2)
            if d(text="AGREE").exists:
                d(text="AGREE").click()
            else:
                pass
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_L_connectivity_test_005(self):
        try:
            d(scrollable=True).scroll.to(text="Connectivity Constraints")
            d(text="Connectivity Constraints").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="START TEST").click()
            sleep(20)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

    def test_M_device_adminstration_test_001(self):
        try:
            d(scrollable=True).scroll.to(text="Device Admin Tapjacking Test")
            d(text="Device Admin Tapjacking Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="ENABLE DEVICE ADMIN").click()
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            sleep(1)
            os.popen('adb -s %s shell input keyevent 4' % list[0])
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_M_device_adminstration_test_002(self):
        try:
            d(scrollable=True).scroll.to(text="Device Admin Uninstall Test")
            d(text="Device Admin Uninstall Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="ENABLE DEVICE ADMIN").click()
            d(scrollable=True).scroll.toEnd()
            d(text="Activate this device admin app" ).click()
            sleep(1)
            d(text="LAUNCH SETTINGS").click()
            d(text="UNINSTALL").click()
            sleep(1)
            d(scrollable=True).scroll.toEnd()
            sleep(1)
            d(resourceId="com.android.settings:id/action_button").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)


    def test_N_SECURITY_test_002(self):
        try:
            d(scrollable=True).scroll.to(text="KeyChain Storage Test")
            d(text="KeyChain Storage Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="NEXT").click()
            sleep(1)
            d(text="NEXT").click()
            sleep(1)
            d(text="NEXT").click()
            sleep(3)
            d(text='OK').click()
            sleep(1)
            d(text='OK').click()
            d(text="Continue without fingerprint").click()
            d(text="PIN").click()
            d(text="YES").click()
            d(text="OK").click()
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            d(text="NEXT").click()
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            d(text="OK").click()
            d(text="DONE").click()
            d(text="NEXT").click()
            sleep(2)
            d(text="NEXT").click()
            sleep(1)
            d(text="SELECT").click()
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_N_SECURITY_test_003(self):
        try:
            d(scrollable=True).scroll.to(text="Keyguard Password Verification")
            d(text="Keyguard Password Verification").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text="CHANGE PASSWORD").click()
            d(resourceId="com.android.settings:id/password_entry").set_text(1234)
            os.popen('adb -s %s shell input keyevent 66'%list[0])
            sleep(1)
            d(text="Continue without fingerprint").click()
            d(text="Password").click()
            d(text="YES").click()
            d(resourceId="com.android.settings:id/password_entry").set_text('testpassword')
            d(text="NEXT").click()
            d(resourceId="com.android.settings:id/password_entry").set_text('testpassword')
            d(text='OK').click()
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)
    def test_N_SECURITY_test_004(self):
        try:
            d(scrollable=True).scroll.to(text="Lock Bound Keys Test")
            d(text="Lock Bound Keys Test").click()
            if d.exists(text="OK") == False:
                pass
            else:
                d(text='OK').click()
            d(text='START TEST').click()
            sleep(3)
            d(resourceId="com.android.settings:id/password_entry").set_text('testpassword')
            os.popen('adb -s %s shell input keyevent 66' % list[0])
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled == True:
                d(resourceId="com.android.cts.verifier:id/pass_button").click()
            else:
                d(resourceId="com.android.cts.verifier:id/fail_button").click()
        except Exception as e:
            except_deal()
            print(e)

if __name__=="__main__":
    unittest.main()
    # suit =unittest.TestSuite()
    # suit.addTests(unittest.TestLoader().loadTestsFromTestCase(Verifier_test))
    # runner = unittest.TextTestRunner(verbosity=2)
    # with open('test.html','wb') as f :
    #     runner =HTMLTestRunner(stream=f,
    #                        title=u'测试报告',
    #                        description=u'测试用例执行情况',
    #                        verbosity=2
    #                                   )
    #     runner.run(suit)




