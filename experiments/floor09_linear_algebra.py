"""Floor 9: vectors + matrices move all of space. Columns = where basis arrows land."""
import numpy as np
def test_vectors_matrices():
    # arrow needs [across, up]
    v = np.array([3.0,4.0])
    assert np.linalg.norm(v) == 5.0  # Pythagoras again
    # matrix columns = images of e1,e2
    M = np.array([[2.0,0.0],[0.0,3.0]])
    assert np.allclose(M @ np.array([1,0]), [2,0])
    assert np.allclose(M @ np.array([0,1]), [0,3])
    # lines stay straight, grid evenly spaced: M(a+b)=Ma+Mb
    a = np.array([1.0,2.0]); b=np.array([3.0,-1.0])
    assert np.allclose(M@(a+b), M@a+M@b)
    # matrix multiplication = do one then another
    A = np.array([[1,2],[3,4]], float); B=np.array([[0,1],[-1,0]], float)
    x = np.array([5.0,6.0])
    assert np.allclose((A@B)@x, A@(B@x))
    # photo = grid of numbers; toy word vectors
    photo = np.arange(9).reshape(3,3)
    assert photo.shape == (3,3)
    words = {"king": np.array([0.9,0.1]), "queen": np.array([0.85,0.15])}
    sim = float(words["king"] @ words["queen"])
    assert sim > 0.7
    return {"norm_3_4": 5.0, "king_queen_sim": round(sim,4)}

if __name__ == "__main__":
    print(test_vectors_matrices())
