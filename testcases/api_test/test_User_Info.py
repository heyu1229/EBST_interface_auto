import pytest
import allure
from common.logger import logger


@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestGetUserInfo():
    """获取用户信息模块"""

    @allure.story("用例--获取全部用户信息")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    @allure.issue("https://www.jianshu.com/p/e664a319d677", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.jianshu.com/p/e664a319d677", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    def test_get_all_user_info(self):
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        assert 200 == 200

        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--获取某个用户信息")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.issue("https://www.jianshu.com/p/e664a319d677", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.jianshu.com/p/e664a319d677", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    def test_get_get_one_user_info(self):
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        assert 200 == 200

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_user_info.py"])