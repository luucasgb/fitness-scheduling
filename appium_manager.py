import subprocess, constants

class AppiumManager:
    def __init__(self) -> None:
        self.appium_args = "appium -a {appium_ip} -p {appium_port}".format(appium_ip=constants.Constants.APPIUM_IP, appium_port=constants.Constants.APPIUM_PORT)

    def startAppium(self):
        p = ['cmd', '/k', 'echo Y | powershell Start-Process cmd -Verb RunAs -ArgumentList \' /c {}\''.format(self.appium_args)]
        subprocess.run(p)
