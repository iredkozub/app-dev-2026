from discount import calculate_discount

def test_regular_discount():
    assert calculate_discount(200) == 10

def test_boundary_discount():
    assert calculate_discount(100) == 5

def test_negative_total():
    try:
        calculate_discount(-100)
        assert False
    except ValueError:
        assert True