from functools import wraps
from unittest.mock import patch

import numpy as np
import pandas as pd
from flojoy import DataFrame
from prophet import Prophet
from prophet.serialize import model_from_json


def test_PROPHET_PREDICT(mock_flojoy_decorator):
    import PROPHET_PREDICT

    # Generate random time series data
    start_date = pd.Timestamp("2023-01-01")
    end_date = pd.Timestamp("2023-07-20")
    num_days = (end_date - start_date).days + 1
    timestamps = pd.date_range(start=start_date, end=end_date, freq="D")
    data = np.random.randn(num_days)  # Random data points

    df = pd.DataFrame({"Timestamp": timestamps, "Data": data})
    dc = DataFrame(df=df)

    # node under test
    res = PROPHET_PREDICT.PROPHET_PREDICT(default=dc, run_forecast=True, periods=365)

    # Should get back a dataframe
    assert isinstance(res["dataframe"].m, pd.DataFrame)
    # Should get back extra with the model is json form and the original df
    extra = res["prophet_data"].extra
    assert extra["run_forecast"] is True
    assert isinstance(extra["original"], pd.DataFrame)
    # This should be identical to the original df, all columns, all rows
    assert (
        (extra["original"] == df.rename(columns={"Timestamp": "ds", "Data": "y"}))
        .all()
        .all()
    )
    assert extra["prophet"] is not None
    assert isinstance(model_from_json(extra["prophet"]), Prophet)
