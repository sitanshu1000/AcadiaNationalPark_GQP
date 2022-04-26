import os
from flask import Flask, flash, request, redirect, url_for, send_file
import pandas as pd
import pickle
import numpy as np
from patsy import dmatrices
import joblib
import json

UPLOAD_FOLDER = '.\\UploadedData'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predictVolume(data_import):
    all_years_test = data_import
    all_years_test.set_index('Full_Date', inplace=True)
    all_years_test.index = pd.to_datetime(all_years_test.index)
    ds = all_years_test.index.to_series()
    all_years_test['YEAR'] = ds.dt.year
    all_years_test['MONTH'] = ds.dt.month
    all_years_test['DAY_OF_WEEK'] = ds.dt.dayofweek
    all_years_test['DAY'] = ds.dt.day
    all_years_test.drop(columns=['snow_1h'], inplace=True)
    all_years_test["federal_holiday_flag"] = all_years_test["federal_holiday_flag"].astype(
        int)
    all_years_test["school_holiday_flag"] = all_years_test["school_holiday_flag"].astype(
        int)
    all_years_test['wind_gust'].fillna(
        (all_years_test['wind_gust'].mean()), inplace=True)
    df_test = all_years_test
    df_test["value"] = [0 for _ in range(len(df_test))]
    print('Testing data set length='+str(len(df_test)))
    expr = """value ~ DAY  + DAY_OF_WEEK + MONTH + YEAR + temp + temp_min + temp_max + pressure + humidity + wind_speed + wind_gust + rain_1h + federal_holiday_flag + school_holiday_flag"""
    y_test, X_test = dmatrices(expr, df_test, return_type='dataframe')

    loaded_model = pickle.load(open("volume_prediction.sav", 'rb'))
    nb2_predictions = loaded_model.get_prediction(X_test)
    result = nb2_predictions.summary_frame()["mean"]
    return result


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
            volumeDf = df.drop(columns=["Average of feels_like"])
            volumeResult = predictVolume(volumeDf)
            volumeJson = volumeResult.to_json(orient="split")
            dwellDf = df.drop(
                columns=["snow_1h", "federal_holiday_flag", "school_holiday_flag"])
            dwellResult = predictDwell(dwellDf)
            dwellJson = json.dumps(dwellResult.tolist())
            result = {
                "Date": volumeResult.index,
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


app.run(debug=True)
