import pytest
import yaml
from playwright.sync_api import sync_playwright

# 1️⃣ 读取 YAML 数据
with open("login_data.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

locators = data["login_page"]    # 页面元素定位
cases = data["test_cases"]       # 测试用例数据

# 2️⃣ 使用 pytest 的 parametrize 做数据驱动
@pytest.mark.parametrize("case", cases)
def test_login_ui(case):
    # 3️⃣ 直接使用 HTML 文件绝对路径
    html_url = "file:///C:/Users/linxiumei/PycharmProjects/yaml/yaml_playwright/login.html"

    # 4️⃣ 启动 Playwright 浏览器
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False 可看到浏览器操作
        page = browser.new_page()
        page.goto(html_url)  # 打开本地登录页面

        # 5️⃣ 填写用户名和密码，点击登录
        page.fill(locators["username_input"], case["username"])
        page.fill(locators["password_input"], case["password"])
        page.click(locators["login_button"])

        # 6️⃣ 根据测试用例预期文本断言结果
        page.wait_for_selector(f"text={case['expected_text']}")  # 等待文本出现
        assert page.inner_text(f"text={case['expected_text']}") == case["expected_text"]

        # 7️⃣ 关闭浏览器
        browser.close()



# import pytest
# import yaml
# from playwright.sync_api import sync_playwright
#
# # 读取 YAML 里的定位信息
# with open("locators.yaml", "r", encoding="utf-8") as f:
#     locators = yaml.safe_load(f)
#
# def test_login_ui():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # 设置 headless=True 可无界面运行
#         page = browser.new_page()
#         page.goto("file:///C:/Users/linxiumei/PycharmProjects/yaml/yaml_playwright/login.html")#本地路径
#
#         # 使用 YAML 中的定位器
#         page.fill(locators["login_page"]["username_input"], "admin")
#         page.fill(locators["login_page"]["password_input"], "123456")
#         page.click(locators["login_page"]["login_button"])
#
#         # 断言
#         page.wait_for_selector(locators["login_page"]["success_text"])
#         assert page.inner_text(locators["login_page"]["success_text"]) == "Welcome"
#
#         browser.close()
