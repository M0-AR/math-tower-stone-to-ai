"""Floor 1-2: counting, place value, add/mult/powers. Verified, no hand-waving."""
def test_floor1_place_value():
    assert 4*10+7 == 47
    assert 2*100+3*10+5 == 235
    assert 2*100+0*10+5 == 205  # zero as empty place
    # rod=flat logic: 10 stones=1 rod, 10 rods=1 flat, 10 flats=1 cube
    stones = 235
    flats, rem = divmod(stones, 100)
    rods, s = divmod(rem, 10)
    assert (flats, rods, s) == (2, 3, 5)
    # 47 grouping
    assert divmod(47, 10) == (4, 7)
    return {"47": [4, 7], "235": [2, 3, 5], "205_zero_placeholder": True}

def test_floor2_add_mult_powers():
    # 3 rows x 4 = 12, 4 rows x 3 = 12 (commutativity seen)
    grid1 = sum(4 for _ in range(3))
    grid2 = sum(3 for _ in range(4))
    assert grid1 == grid2 == 12
    assert 3*4 == 4*3
    assert 3*3 == 9  # square
    assert 3*3*3 == 27  # cube
    x = 1
    for _ in range(10):
        x *= 2
    assert x == 1024 == 2**10
    return {"3x4": 12, "4x3": 12, "2^10": 1024}

if __name__ == "__main__":
    print(test_floor1_place_value())
    print(test_floor2_add_mult_powers())
