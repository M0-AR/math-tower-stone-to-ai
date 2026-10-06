"""Floor 4-5: algebra balance (al-Khwarizmi ~820), functions (Descartes 1637)."""
def solve_x_plus_3_eq_7():
    # balance: subtract 3 both sides
    lhs, rhs = "x+3", 7
    # undo +3 on both sides
    x = 7-3
    assert x+3 == 7
    return {"x": x}

def test_function_machine():
    f = lambda n: 2*n+1
    pairs = [(1,3),(2,5),(3,7)]
    for inp, out in pairs:
        assert f(inp) == out
    # Descartes points (input, output)
    points = [(x, f(x)) for x in range(5)]
    assert points[0] == (0,1)
    # parabola g(x)=x^2 bends
    g = lambda x: x*x
    assert [g(x) for x in range(4)] == [0,1,4,9]
    # straight line check: f slope constant 2
    assert f(2)-f(1) == f(3)-f(2) == 2
    # parabola second differences constant
    vals = [g(x) for x in range(5)]
    first = [vals[i+1]-vals[i] for i in range(4)]
    second = [first[i+1]-first[i] for i in range(3)]
    assert second == [2,2,2]
    return {"points": points, "parabola": vals}

if __name__ == "__main__":
    print(solve_x_plus_3_eq_7(), test_function_machine())
