from typing import TypedDict
from flojoy import flojoy, DataFrame
from sklearn.model_selection import train_test_split


class TrainTestSplitOutput(TypedDict):
    train: DataFrame
    test: DataFrame


@flojoy(deps={"scikit-learn": "1.2.2"})
def TRAIN_TEST_SPLIT(
    default: DataFrame, test_size: float = 0.2
) -> TrainTestSplitOutput:
    """The TRAIN_TEST_SPLIT node is used to split the data into test and training according to a size specified before any ML tasks.

    Parameters
    ----------
    test_size : float
        The size of testing data specified.

    Returns
    -------
    train: DataFrame
        A dataframe of training data.
    test: DataFrame
        A dataframe of test data.
    """

    df = default.m
    train, test = train_test_split(df, test_size=test_size)
    return TrainTestSplitOutput(train=DataFrame(df=train), test=DataFrame(df=test))
