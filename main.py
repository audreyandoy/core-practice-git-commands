import pytest


def always_returns_true():
    print("yay this works now thanks Trenisha!!")
    return True


def test_always_returns_true():
    assert always_returns_true()
