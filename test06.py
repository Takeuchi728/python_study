import datetime


today = datetime.date.today()
todaydetail = datetime.datetime.today()

#今日の日付
print('-------------------')
print(today)
print(todaydetail)

# 今日に日付：各値
print('-------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

#日付のフォーマット
print('-------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))

print('-------------------')

#tomorrow time
print(todaydetail + datetime.timedelta(days=1))

newyear = datetime.datetime(2020, 1, 1)

print(newyear + datetime.timedelta(days=7))

#2020/1/1から今日までの日数
calc = todaydetail - newyear
#計算値の戻り値はtimedelta
print(calc.days)
