import pytest


def always_returns_true():
    print("uh what is this, why is this false?")
    return False


def test_always_returns_true():
    assert always_returns_true()
