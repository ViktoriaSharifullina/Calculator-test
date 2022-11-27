from behave import given, when, then
from Calculator import *


@given('I have entered {number1:d} into the calculator')
def enter_number1(context, number1):
    context.number1 = number1


@given('I have entered {number1:f} into the calculator')
def enter_number1(context, number1):
    context.number1 = number1


@given('I have also entered {number2:d} into the calculator')
def enter_number2(context, number2):
    context.number2 = number2


@given('I have also entered {number2:f} into the calculator')
def enter_number2(context, number2):
    context.number2 = number2


@when('I press {action:w}')
def press_action(context, action):
    context.action = action
    if action == "plus":
        context.result = addition(context.number1, context.number2)
    elif action == "minus":
        context.result = difference(context.number1, context.number2)
    elif action == "multiply":
        context.result = multiplication(context.number1, context.number2)
    elif action == "division":
        context.result = division(context.number1, context.number2)


@then('the {result:d} should be on the screen')
def check_result(context, result):
    assert context.result == result


@then('the {result:f} should be on the screen')
def check_result(context, result):
    assert context.result == result
