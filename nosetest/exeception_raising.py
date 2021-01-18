from nose.tools import raises, eq_

@raises(TypeError)
def test_using_raises():
    eq_(2+'3', 5)