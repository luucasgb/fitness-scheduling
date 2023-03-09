import android_manager, appium_manager, constants

class App:    
    def __init__(self) -> None:
        self.android_manager = android_manager.AndroidManager(constants.Constants.APK_PATH)
        self.appium_manager = appium_manager.AppiumManager()

    def run_appium(self):
        self.appium_manager.startAppium()

    def run_android(self):
        self.android_manager.setup()

    def main_run(self):
        self.run_appium()

app = App()
app.main_run