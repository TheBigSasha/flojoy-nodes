import numpy as np
from flojoy import Vector, Scalar


def test_VECTOR_INDEXING(mock_flojoy_decorator):
    import VECTOR_INDEXING

    x = np.ones(5)
    x[0] = 5

    element = Vector(v=x)
    res = VECTOR_INDEXING.VECTOR_INDEXING(element)

    assert np.array_equal(res.c, 5)
