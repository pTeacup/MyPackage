from MyPackage import myModule

def test_top_n():
    '''
    Make sure top_n works correctly
    '''

    assert myModule.top_n([1,2,3,7,8], 4) == [8,7,3,2], 'incorrect'
    assert myModule.top_n([6,3,4,2,9], 2) == [9,6], 'incorrect'
    assert myModule.top_n([1,2,2,3,3,7,5], 5) == [7,5,3,3,2], 'incorrect'