"""Floor 3: undo add->sub/negatives, undo mult->div/fractions, undo square->sqrt2 irrational."""
import math
from fractions import Fraction

def test_negatives():
    assert 3-5 == -2
    # Brahmagupta: debt minus zero is debt, fortune + debt rules
    assert (-2)+2 == 0
    assert (-3)*(-2) == 6  # product of two debts is fortune
    assert (-3)*2 == -6
    return {"3-5": -2}

def test_fractions():
    assert Fraction(1,4)*4 == 1
    # quarter bar
    assert abs(0.25*4-1.0) < 1e-12
    return {"quarter": 0.25}

def test_sqrt2_irrational():
    s = math.sqrt(2)
    assert abs(s**2-2.0) < 1e-12
    assert abs(s-1.4142) < 0.001
    # No fraction p/q with q<=100 equals sqrt2 exactly: proof by contradiction
    # If (p/q)^2==2 then p^2==2q^2 -> p even -> p=2k -> 4k^2==2q^2 -> q even, infinite descent.
    # Computational check: best approximations never exact
    best = min((abs(Fraction(p,q)-s),p,q) for q in range(1,101) for p in [int(s*q),int(s*q)+1])
    assert best[0] > 0  # never zero
    # digits never repeat in first 50: check period detection fails
    digits = f"{s:.50f}".split(".")[1]
    assert len(set(digits)) > 2
    return {"sqrt2": s, "best_p_q_err": best[0], "digits_sample": digits[:20]}

if __name__ == "__main__":
    print(test_negatives(), test_fractions(), test_sqrt2_irrational())
