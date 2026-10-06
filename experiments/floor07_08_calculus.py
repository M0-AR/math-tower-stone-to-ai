"""Floor 7-8: derivative (zoom -> slope 2x for x^2) + integral (Riemann bars) + FTC."""
def deriv_numerical(f, x, h=1e-7):
    return (f(x+h)-f(x-h))/(2*h)

def test_derivative():
    f = lambda x: x*x
    for x in [0.0,1.0,2.5,-3.0]:
        assert abs(deriv_numerical(f,x)-2*x) < 1e-4, (x, deriv_numerical(f,x))
    # speedometer analogy: position t^2 -> velocity 2t
    return {"d/dx x^2 = 2x": True}

def riemann_sum(f, a, b, n):
    dx = (b-a)/n
    return sum(f(a+(i+0.5)*dx)*dx for i in range(n))

def test_integral():
    import math
    # integral of speed = distance; integral x^2 from 0 to 3 = 9
    for n in [10,100,1000]:
        approx = riemann_sum(lambda x: x*x, 0, 3, n)
        if n==1000:
            assert abs(approx-9.0) < 0.01
    # area under curve; FTC: integral and derivative undo
    # D(Integral_0^x t^2 dt) = x^2
    F = lambda x: x**3/3
    assert abs(deriv_numerical(F,2.0)-4.0) < 1e-4
    assert abs((F(3)-F(0))-9.0) < 1e-12
    return {"int_0^3 x^2": 9.0, "FTC": True}

if __name__ == "__main__":
    print(test_derivative(), test_integral())
