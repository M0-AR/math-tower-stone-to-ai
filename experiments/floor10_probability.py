"""Floor 10: Galton board 10 rows -> 1024 paths, 1 far-left, 252 middle. Bell curve emerges."""
import math, random
from collections import Counter
def test_combinatorics():
    assert 2**10 == 1024
    assert math.comb(10,0) == 1
    assert math.comb(10,5) == 252
    assert sum(math.comb(10,k) for k in range(11)) == 1024
    return {"paths":1024,"far_left":1,"middle":252}

def simulate_galton(n_rows=10, n_balls=20000, seed=0):
    rng = random.Random(seed)
    counts = Counter()
    for _ in range(n_balls):
        k = sum(rng.random()<0.5 for _ in range(n_rows))
        # careful: sum of True=right? use right count; symmetric so same
        counts[k] += 1
    # empirical vs theory Binomial(10,0.5)
    chi = 0.0
    for k in range(n_rows+1):
        expected = n_balls*math.comb(n_rows,k)/2**n_rows
        chi += (counts[k]-expected)**2/expected
    # middle fills: bin5 largest
    top = counts.most_common(1)[0][0]
    assert top == 5, top
    assert counts[5] > counts[0]*50
    return {"counts":dict(sorted(counts.items())),"chi2":round(chi,2),"top_bin":top}

if __name__=="__main__":
    print(test_combinatorics())
    print(simulate_galton())
