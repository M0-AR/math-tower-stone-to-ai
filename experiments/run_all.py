"""Run all floors sequentially. Fails loudly on any broken claim."""
from floor01_02_counting import test_floor1_place_value, test_floor2_add_mult_powers
from floor03_undo_numbers import test_negatives, test_fractions, test_sqrt2_irrational
from floor04_05_algebra_functions import solve_x_plus_3_eq_7, test_function_machine
from floor06_geometry import test_pythagoras, test_sine
from floor07_08_calculus import test_derivative, test_integral
from floor09_linear_algebra import test_vectors_matrices
from floor10_probability import test_combinatorics, simulate_galton
from floor10b_live_market import main as live_main
import json

def main():
    out = {}
    out["f1"] = test_floor1_place_value()
    out["f2"] = test_floor2_add_mult_powers()
    out["f3a"] = test_negatives(); out["f3b"] = test_fractions(); out["f3c"] = test_sqrt2_irrational()
    out["f4"] = solve_x_plus_3_eq_7(); out["f5"] = test_function_machine()
    out["f6a"] = test_pythagoras(); out["f6b"] = test_sine()
    out["f7"] = test_derivative(); out["f8"] = test_integral()
    out["f9"] = test_vectors_matrices()
    out["f10a"] = test_combinatorics(); out["f10sim"] = simulate_galton()
    out["live"] = live_main()
    print("ALL FLOORS VERIFIED")
    return out

if __name__ == "__main__":
    main()
