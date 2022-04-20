import os
import pandas as pd
import pickle
import numpy as np
from patsy import dmatrices
import joblib


def predictDwell(df):
    times = pd.to_datetime(df["Full_Date"])
    dow = times.dt.dayofweek
    df["Month"] = times.dt.month
    df["Year"] = times.dt.year % 2000
    # add summer variable
    df["is_summer"] = np.where((df["Month"].isin([6, 7, 8])), 1, 0)

    # one hot encoding for DOW
    df["Tuesday"] = 0
    df["Wednesday"] = 0
    df["Thursday"] = 0
    df["Friday"] = 0
    df["Saturday"] = 0
    df["Sunday"] = 0

    for i in df.index:
        if dow[i] == 6:
            df.loc[i, "Sunday"] = 1
        elif dow[i] == 1:
            df.loc[i, "Tuesday"] = 1
        elif dow[i] == 2:
            df.loc[i, "Wednesday"] = 1
        elif dow[i] == 3:
            df.loc[i, "Thursday"] = 1
        elif dow[i] == 4:
            df.loc[i, "Friday"] = 1
        elif dow[i] == 5:
            df.loc[i, "Saturday"] = 1
    df = df.drop(columns=["Full_Date"])
    loaded_model = joblib.load("RF_5_16.joblib")
    result = loaded_model.predict(df)
    return result


df = pd.read_csv("test_data.csv")
dwellDf = df.drop(
    columns=["snow_1h", "federal_holiday_flag", "school_holiday_flag"])
print(predictDwell(dwellDf))
