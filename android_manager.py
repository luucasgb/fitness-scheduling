from appium import webdriver
import constants

class AndroidManager:
    def __init__(self, apk_path) -> None:
        self.app_data = {}
        self.driver = None;
        self.apk_path = apk_path

    def setup(self):
        self.app_data['app'] = self.apk_path
        self.app_data['automationName'] = "UiAutomator2"
        self.app_data['appPackage'] = "br.com.mufitness.station.aluno"
        self.app_data['appActivity'] = ".MainActivity"
        self.app_data['platformName'] = 'Android'
        self.app_data['deviceName'] = 'Pixel_4_API_33:5544'
        self.driver = webdriver.Remote("http://{ip}:{port}/wd/hub".format(ip=constants.Constants.APPIUM_IP, port=constants.Constants.APPIUM_PORT), self.app_data)