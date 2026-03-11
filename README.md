# Cấu trúc thư mục mẫu

```
tests/
  pages/
    base_page.py
    login_page.py
    wifi_page.py
  e2e/
    test_login.py
    test_wifi_change.py
  conftest.py
playwright.config.py
pytest.ini
requirements.txt
ci/
  .gitlab-ci.yml

```

# Settings

```
pip install -r requirements.txt
playwright install

```

# How to run

```
export GATEWAY_URL="http://192.168.1.1"
export GATEWAY_USER="admin"
export GATEWAY_PASS="admin"
pip install -r requirements.txt
playwright install
pytest -m e2e -q

```