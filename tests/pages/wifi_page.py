class WifiPage:
    def __init__(self, page):
        self.page = page
        self.menu_wifi = "a#menu-wifi"
        self.ssid_input = "input#ssid"
        self.save_btn = "button#save-wifi"
        self.success_toast = ".toast-success"

    def open(self):
        self.page.click(self.menu_wifi)
        self.page.wait_for_selector(self.ssid_input, timeout=5000)

    def set_ssid(self, ssid):
        self.page.fill(self.ssid_input, ssid)
        self.page.click(self.save_btn)
        self.page.wait_for_selector(self.success_toast, timeout=10000)
