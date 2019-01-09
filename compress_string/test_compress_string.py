from compress_string import scan_for_outter_parts, return_reps

def test_scan_for_outter_parts():
    x, y= scan_for_outter_parts('a3[b]c')
    assert x == [2]
    assert y == [4]

def test_scan_for_outter_parts():
    x, y, = scan_for_outter_parts('a13[b]c')
    assert x == [3]
    assert y == [5]

def test_scan_for_outter_parts_multiple_opens():
    x, y = scan_for_outter_parts('a3[b]c3[sdf]dsf')
    assert x == [2, 7]
    assert y == [4, 11]


def test_scan_for_outter_parts_multiple_opens():
    x, y = scan_for_outter_parts('a3[b]c3[s[d]f]dsf')
    assert x == [2, 7]
    assert y == [4, 13]


def test_return_reps():
    z = return_reps('a3[b]c', [2])
    assert z == ['3']

def test_return_reps_2digits():
    z = return_reps('a13[b]c', [3])
    assert z == ['13']

def test_return_reps_4digits():
    z = return_reps('a1213[b]c', [5])
    assert z == ['1213']
