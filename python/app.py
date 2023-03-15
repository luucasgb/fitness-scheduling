from appium import webdriver
import constants
import subprocess, constants

class AppiumManager:
    def __init__(self) -> None:
        self.appium_args = "appium -a {appium_ip} -p {appium_port}".format(appium_ip=constants.Constants.APPIUM_IP, appium_port=constants.Constants.APPIUM_PORT)

class AndroidManager:
    def __init__(self, apk_path) -> None:
        self.app_data = {}
        self.driver = None
        self.apk_path = apk_path

class App:
    def __init__(self, appium_manager, android_manager) -> None:
        self.appium_manager = appium_manager
        self.android_manager = android_manager
        
    def setupAppium(self):
        return AppiumManager()
    
    def setupAndroid(self):
        return AndroidManager(constants.Constants.APK_PATH)

    def startAppium(self):
        p = ['cmd', '/k', 'echo Y | powershell Start-Process cmd -Verb RunAs -ArgumentList \' /c {}\''.format(self.appium_manager.appium_args)]
        subprocess.run(p)

    def startAndroid(self):
        self.android_manager.app_data['app'] = self.android_manager.apk_path
        self.android_manager.app_data['automationName'] = "UiAutomator2"
        self.android_manager.app_data['appPackage'] = "br.com.mufitness.station.aluno"
        self.android_manager.app_data['appActivity'] = ".MainActivity"
        self.android_manager.app_data['platformName'] = 'Android'
        self.android_manager.app_data['deviceName'] = 'Pixel_4_API_33:5544'
        self.android_manager.driver = webdriver.Remote("http://{ip}:{port}/wd/hub".format(ip=constants.Constants.APPIUM_IP, port=constants.Constants.APPIUM_PORT), self.app_data)

    def run_appium(self):
        self.startAppium()

    def run_android(self):
        self.startAndroid()

    def main(self):
        self.run_appium()

appium_manager = AppiumManager() 
android_manager = AndroidManager(constants.Constants.APK_PATH)
app = App(appium_manager, android_manager)
app.main()