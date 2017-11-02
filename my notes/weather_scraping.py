#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup


url = "http://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.WftcLRNSyRs"
req  = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
#^ devtools is better




#find info for this afternoon:

period = soup.find(class_="period-name") #find only gets the first instance
short_desc = soup.find(class_="short-desc").get_text()
temp = soup.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)




##################### now we can use lists to get this info for all the time periods
'''
period_tags = soup.select(".period-name") #select gets all instances and returns a list
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in soup.select(".short-desc")] #list comp version
print(short_descs)

temps = [t.get_text() for t in soup.select(".temp")]
print(temps)
'''



#then we could put this in a pandas dataframe, write to csv, etc.
'''
import pandas as pd
weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
    })
'''
