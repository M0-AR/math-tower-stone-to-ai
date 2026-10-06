"""Floor 6: Pythagoras 3-4-5 (9+16=25) + sine wave unit wheel."""
import math
def test_pythagoras():
    assert 3**2+4**2 == 5**2 == 25
    # holds generally: check 5-12-13, 8-15-17
    for a,b,c in [(5,12,13),(8,15,17),(6,8,10)]:
        assert a*a+b*b == c*c
    # distance formula = Pythagoras repeated
    assert math.hypot(3,4) == 5.0
    return {"3-4-5": True}

def test_sine():
    # unit wheel: height = sin(theta)
    for deg, expected in [(0,0.0),(90,1.0),(180,0.0),(270,-1.0)]:
        assert abs(math.sin(math.radians(deg))-expected) < 1e-9
    # wave period 2pi
    assert abs(math.sin(0)-math.sin(2*math.pi)) < 1e-12
    # sample 8 points
    wave = [round(math.sin(2*math.pi*i/8),6) for i in range(8)]
    return {"wave8": wave}

if __name__ == "__main__":
    print(test_pythagoras(), test_sine())
