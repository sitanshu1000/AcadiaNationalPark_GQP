import os
from flask import Flask, flash, request, redirect, url_for, send_file
import pandas as pd
import pickle
import numpy as np
from patsy import dmatrices
import joblib
import json
from pandas.tseries.holiday import USFederalHolidayCalendar


UPLOAD_FOLDER = '.\\UploadedData'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predictVolume(data_import):
    cal = USFederalHolidayCalendar()
    holidays = cal.holidays(start='2014-01-01', end='2026-12-31')
    all_years_test = data_import
    all_years_test.set_index('Full_Date', inplace=True)
    all_years_test.index = pd.to_datetime(all_years_test.index)
    ds = all_years_test.index.to_series()
    all_years_test['YEAR'] = ds.dt.year
    all_years_test['MONTH'] = ds.dt.month
    all_years_test['DAY_OF_WEEK'] = ds.dt.dayofweek
    all_years_test['DAY'] = ds.dt.day
    all_years_test['federal_holiday_flag'] = all_years_test.index.isin(holidays)

    all_years_test['school_holiday_flag'] = all_years_test.index.isin(all_years_test.index[(all_years_test.index.month >= 6) & (all_years_test.index.month <= 8)])
    all_years_test["federal_holiday_flag"] = all_years_test["federal_holiday_flag"].astype(int)
    all_years_test["school_holiday_flag"] = all_years_test["school_holiday_flag"].astype(int)
    X = all_years_test[['temp', 'humidity', 'wind_speed', 'rain_1h', 'federal_holiday_flag', 'school_holiday_flag', 'MONTH', 'DAY_OF_WEEK', 'DAY']]
    loaded_model = pickle.load(open("volume_prediction.sav", 'rb'))
    out_of_sample_pred = loaded_model.predict(X)
    return out_of_sample_pred, X.index


def predictDwell(df):
    times = pd.to_datetime(df["Full_Date"])
    dow = times.dt.dayofweek
    df["Month"] = times.dt.month
    df["Year"] = times.dt.year % 2000
    # add summer variable
    df["is_summer"] = np.where((df["Month"].isin([6, 7, 8])), 1, 0)

    # one hot encoding for DOW
    df["Monday"] = 0
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
        else:
            df.loc[i,"Monday"] = 1
    df = df.drop(columns=["Full_Date"])
    loaded_model = joblib.load("RF.joblib")
    result = loaded_model.predict(df)
    return result

@app.route("/")
def hello():
    return "Hello World"

@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            # save file to temp directory
            fname = file.filename
            file.save(fname)
            # read file
            df = pd.read_csv(fname)
            # df contains the following columns:
            # Full_Date,
            # temp,
            # temp_min,
            # temp_max,
            # pressure,
            # humidity,
            # wind_speed,
            # wind_gust,
            # rain_1h,
            # snow_1h,
            # federal_holiday_flag,
            # school_holiday_flag,
            # Average of feels_like
            resultPath = "Result.csv"
            if os.path.exists(resultPath):
                os.remove(resultPath)
            volumeDf = df[["Full_Date","temp","humidity","wind_speed","rain_1h"]]
            volumeResult, dates = predictVolume(volumeDf)
            volumeJson = json.dumps(volumeResult.tolist())
            dwellDf = df
            dwellResult = predictDwell(dwellDf)
            dwellJson = json.dumps(dwellResult.tolist())
            result = {
                "Date": dates,
                "Volume": volumeResult,
                "Dwell Time": dwellResult,
            }
            result = pd.DataFrame(result)
            result.to_csv(resultPath, index=False)
            # calculate
            # get the result
            # remove file from temp directory
            os.remove(fname)
            return {
                "msg": "Success",
                "date":dates.to_list(),
                "volume": volumeJson,
                "dwell": dwellJson,
            }
    return {"msg": "Load"}


@app.route('/downloadresult')
def downloadResult():
    return send_file('Result.csv',
                     mimetype='text/csv',
                     attachment_filename='Result.csv',
                     as_attachment=True)


app.run(debug=True,host="0.0.0.0",ssl_context='adhoc')
