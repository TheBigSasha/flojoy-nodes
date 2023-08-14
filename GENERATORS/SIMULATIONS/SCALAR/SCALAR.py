from flojoy import flojoy, Scalar


@flojoy
def SCALAR(
    value: float = 3.0,
) -> Scalar:
    """The SCALAR node returns a single Scalar value.

    Parameters
    ----------
    value: float
        The value set in Parameters

    Returns
    -------
    Scalar
        c: return the value being set in Parameters
    """

    return Scalar(c=value)
