# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 15:49
# @Author  : derrick
# @Email   : luotaibin@gmail.com
import allure


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments1(1, 'abc')


@allure.step
def nested_step_with_arguments1(arg1, arg2):
    pass


@allure.step('Test case execution steps')
def nested_step_with_arguments(arg):
    pass


@allure.description('description')
def nested_step_with_description(arg):
    pass


@allure.story('story')
def nested_step_with_story(arg):
    pass
