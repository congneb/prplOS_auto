class LoginPage:
    def __init__(self, page, base_url):
        self.page = page
        self.url = f"{base_url}/"
        # selectors (tweak to actual UI)
        self.user_input = "input#username"
        self.pass_input = "input#password"
        self.login_btn = "button#login"
        self.error_banner = ".alert-danger"

    def goto(self):
        self.page.goto(self.url, timeout=30000)

    def login(self, username, password):
        self.page.fill(self.user_input, username)
        self.page.fill(self.pass_input, password)
        self.page.click(self.login_btn)
        # wait for navigation or dashboard element
        self.page.wait_for_selector("div#dashboard", timeout=10000)

    def is_error_visible(self):
        return self.page.is_visible(self.error_banner)
