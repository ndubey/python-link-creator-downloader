from datetime import datetime, date, timedelta as td

#d1 = date(2015, 8, 15)
d1 = date(2015, 1, 1)
d2 = date(2016, 5, 24)

delta = d2 - d1

url_prefix = "https://epaper.thehindu.com/pdf/"
url_suffix = "3A.zip"
#https://epaper.thehindu.com/pdf/2015/01/01/201501013A.zip

for i in range(delta.days + 1):
    date = d1 + td(days=i)
    dayformat = datetime.strftime(date, "%Y/%m/%d/")
    filename = datetime.strftime(date, "%Y%m%d")
    exact_url = url_prefix + dayformat + filename+url_suffix;
    print (exact_url)
