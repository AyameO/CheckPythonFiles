# pandasのインポート
import pandas as pd

# データの読み込み
df = pd.read_csv("booking_data.csv", parse_dates=["予約受付日","宿泊日"])

# 月・曜日データの作成
df["宿泊月"] = df["宿泊日"].apply(lambda x: x.strftime('%m'))
df["宿泊曜日"] = df["宿泊日"].apply(lambda x: x.strftime('%a'))
df["予約受付曜日"] = df["予約受付日"].apply(lambda x: x.strftime('%a'))

# datetimeのインポート
import datetime as dt

# 宿泊日の指定
str_date1 = "2019-08-25"
str_date2 = "2019-04-27"
str_date3 = "2019-11-11"

# 宿泊日の日時型オブジェクトの作成
dt_date1 = pd.Timestamp(str_date1)
dt_date2 = pd.Timestamp(str_date2)
dt_date3 = pd.Timestamp(str_date3)
 
# 予約受付開始日から宿泊日前日までの連続する日付の作成
new_index1 = pd.date_range(start=dt_date1 - dt.timedelta(days=30), end=dt_date1 - dt.timedelta(days=1), freq='D')
new_index2 = pd.date_range(start=dt_date2 - dt.timedelta(days=30), end=dt_date2 - dt.timedelta(days=1), freq='D')
new_index3 = pd.date_range(start=dt_date3 - dt.timedelta(days=30), end=dt_date3 - dt.timedelta(days=1), freq='D')

# 累計の予約数の作成
vcc1 = df[df["宿泊日"] == dt_date1]["予約受付日"].value_counts().reindex(new_index1, fill_value=0).sort_index().cumsum().reset_index(drop=True)
vcc2 = df[df["宿泊日"] == dt_date2]["予約受付日"].value_counts().reindex(new_index2, fill_value=0).sort_index().cumsum().reset_index(drop=True)
vcc3 = df[df["宿泊日"] == dt_date3]["予約受付日"].value_counts().reindex(new_index3, fill_value=0).sort_index().cumsum().reset_index(drop=True)

# グラフの作成
import matplotlib.pyplot as plt
vcc1.plot(label=str_date1)
vcc2.plot(label=str_date2)
vcc3.plot(label=str_date3)
plt.title("ブッキングカーブ")
plt.xlabel("予約受付開始からの経過日数")
plt.ylabel("予約された部屋の数")
plt.legend()
plt.grid()
plt.show()
