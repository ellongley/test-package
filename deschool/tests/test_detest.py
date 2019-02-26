from deschool import detest

# to run this test do pytest test_detest.py


def test_say_hi():
    assert type(detest.say_hi())==str
