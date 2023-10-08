from flojoy import flojoy, TextBlob, DataFrame
from typing import Optional
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_KEYFRAMES(
        ip_address: TextBlob,
        keyframes: DataFrame,
) -> TextBlob:
    """
    The MOVE_KEYFRAMES node linearly moves the robot's tool according to a set of 3d animation style keyframes.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.
    keyframes: DataFrame
        A dataframe containing the keyframes to move to. The dataframe must have the following columns:
        x, y, z, alpha, beta, gamma, duration. The duration column is the time in seconds to move to the next keyframe.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)

    # Data validation
    required_columns = ["x", "y", "z", "alpha", "beta", "gamma", "duration"]
    for column in required_columns:
        if column not in keyframes.columns:
            raise ValueError(f"Keyframes dataframe must have a {column} column")
    # check that all values are numeric
    for column in keyframes.columns:
        if keyframes[column].dtype != "float64":
            raise ValueError(f"Keyframes dataframe column {column} must be numeric")

    # Move execution
    for index, row in keyframes.iterrows():
        robot.MoveJoints(row["x"], row["y"], row["z"], row["alpha"], row["beta"], row["gamma"])
        robot.WaitIdle(row["duration"]) #TODO: What is the best way to configure velocities here per axis?
    return ip_address
