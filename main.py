import pytest
def addition(num1: int, num2: int) -> int:
  return num1 + num2

def greeting(name: str) -> str:
  return 'Hello, ' + name



def test_addition():
  assert addition(1, 2) == 3

def test_addtion_minus():
  assert addition(1, -1) == 0

def test_greeting():
  assert greeting('aika') == 'Hello, aika'
