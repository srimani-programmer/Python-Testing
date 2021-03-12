from nose.tools import raises
class SampleTestClass:
    @raises(TypeError)
    def test_sample1(self):
        pow(2, '4')
    @raises(Exception)    
    def test_sample2(self):        
        max([7, 8, '4'])
    
    @raises(Exception)
    def test_sample3(self):
        int('hello')