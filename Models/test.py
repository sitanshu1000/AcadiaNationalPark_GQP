import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
import pickle

# read data
data_import = pd.read_csv('volumeTest.csv')

# data preprocessing
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

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# numerical_features = ['temp', 'humidity', 'wind_speed', 'rain_1h']
# cat_features = ['federal_holiday_flag', 'school_holiday_flag', 'MONTH', 'DAY_OF_WEEK','DAY']

# ct = ColumnTransformer([
#     ('numerical', StandardScaler(), numerical_features),
#     ('categorical', OneHotEncoder(sparse=False, handle_unknown='error', drop='if_binary'), cat_features)
# ])

# final_xgb_pip = Pipeline([
#     ('prep', ct),
#     ('reg', XGBRegressor(n_estimators= 500,
#                          max_depth=1,
#                          learning_rate=0.1,
#                          min_child_weight=3,
#                          booster='gbtree',
#                          # base_score=0.75,
#                          objective='count:poisson'))
# ])

# # train model
# final_xgb_pip.fit(X_train,y_train)
filename = "volume_prediction.sav"
# # output model
# pickle.dump(final_xgb_pip, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))

# # read in test
# out_of_sample_dataset = pd.read_csv('Data/out_of_sample.csv')
# out_of_sample_dataset.set_index('Full_Date', inplace=True)
# out_of_sample_dataset.index = pd.to_datetime(out_of_sample_dataset.index)
out_of_sample_pred = loaded_model.predict(X)
print(out_of_sample_pred)