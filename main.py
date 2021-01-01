import pytest
class test_util():
  def addition(self, num1: int, num2: int) -> int:
    return num1 + num2

  def greeting(self, name: str) -> str:
    return 'Hello, ' + name



def test_addition():
  target = test_util()
  assert target.addition(1, 2) == 3

def test_addtion_minus():
  target ; test_util()
  assert target.addition(1, -1) == 0

def test_greeting():
  target = test_util()
  assert target.greeting('aika') == 'Hello, aika'
