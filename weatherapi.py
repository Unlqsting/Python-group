import datetime
# Create date variable with a random value
date = 1
# Create dateCalc to display the current time
dateCalc = datetime.datetime.now()
# If statements to change the value of date so then it can be used in the API. The day of the weeks for the API is three letter abbreviations.
if dateCalc.strftime("%A") == "Monday":
    date = "Mon"
if dateCalc.strftime("%A") == "Tuesday":
    date = "Tue"
if dateCalc.strftime("%A") == "Wednesday":
    date = "Wed"
if dateCalc.strftime("%A") == "Thursday":
    date = "Thu"
if dateCalc.strftime("%A") == "Friday":
    date = "Fri"
if dateCalc.strftime("%A") == "Saturday":
    date = "Sat"
if dateCalc.strftime("%A") == "Sunday":
    date = "Sun"
 
# Set count to 1 so the data only runs once, then this will only display the current day of this week and not next week.
count = 1
 
# Access the API
import requests
 
url = "https://yahoo-weather5.p.rapidapi.com/weather"
 
location = input()
 
querystring = {"location": str(location),"format":"json","u":"f"}
 
headers = {
    "X-RapidAPI-Key": "554c89336amsh69cd248886ad9ecp1390b5jsn24d7469d6aa0",
    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}
 
response = requests.request("GET", url, headers=headers, params=querystring)
 
# Uncomment this to access raw data
# print(response.text)
 
# Filter out the data to display only weather info today
print("Weather is in ◦F")
print("Forecast in", str(location), ":")
result = response.json().get('forecasts')
for re in result:
    if count == 1:
        if re["day"] == date:
            print(dateCalc.strftime("%A"))
            print("Low:", re["low"])
            print("High:", re["high"])
            print("Weather:", re["text"])
            count = count + 1
