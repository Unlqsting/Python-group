# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/Calendar/')  # connects /stub/ URL to stub() function
def Calendar():
    return render_template("Calendar.html")

@app.route('/weatherapi/')  # connects /stub/ URL to stub() function
def weather():
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
    
    result = response.json().get('forecasts')
    for re in result:
    
        if re["day"] == date:
           return re
    # apidata = 'apidata.json'
    # with open(apidata, 'w') as wd:
    #     wd.writelines(response.json())

    # this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
