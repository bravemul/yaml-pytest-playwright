import pytest
import yaml
from app import login_api   # 引入被测函数

# 从 YAML 文件读取测试数据
with open("cases.yaml", "r", encoding="utf-8") as f:
    cases = yaml.safe_load(f)

@pytest.mark.parametrize("case", cases["login_cases"])
def test_login(case):
    result = login_api(case["username"], case["password"])
    assert result == case["expected"]
