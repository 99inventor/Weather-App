from flask import Flask,render_template,request

import urllib.request
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        city = request.form['city']
    else:
        city = '' # enter the default city you want to show
    print(city)
    
    api = "" # enter open weather api key here
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
    print (url) 
    
    source = urllib.request.urlopen(url).read()
    print(source)

    list_of_data = json.loads(source)
    print(list_of_data)

    # Rounding of Data
    list_of_data['main']['temp'] = round(((list_of_data['main']['temp']) - 273.15))
    list_of_data['main']['feels_like'] = round(((list_of_data['main']['feels_like']) - 273.15))
    list_of_data['main']['temp_min'] = round(((list_of_data['main']['temp_min']) - 273.15))
    list_of_data['main']['temp_max'] = round(((list_of_data['main']['temp_max']) - 273.15))
    list_of_data['coord']['lat'] = round(list_of_data['coord']['lat'], 2)
    list_of_data['coord']['lon'] = round(list_of_data['coord']['lon'], 2)

    # Putting Data in a Dictionary
    data={
        "temp" : str(list_of_data['main']['temp']),
        "country_code" :str(list_of_data['sys']['country']),
        "feels_like" : str(list_of_data['main']['feels_like']),
        "temp_min" : str(list_of_data['main']['temp_min']),
        "temp_max" : str(list_of_data['main']['temp_max']),
        "pressure" : str(list_of_data['main']['pressure']),
        "humidity" : str(list_of_data['main']['humidity']),
        "lat" : str(list_of_data['coord']['lat']),
        "lon" : str(list_of_data['coord']['lon'])
    }
    return render_template('weather.html', data=data)
    
app.run(debug=True)