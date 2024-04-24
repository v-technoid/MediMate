# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# # Define a route that fetches data from the API
# @app.route('/')
# def index():
    
#     url = "https://dietagram.p.rapidapi.com/apiFood.php"
#     querystring = {"name": "Jabłko", "lang": "en"}
#     headers = {
#         "X-RapidAPI-Key": "d0dfbe85fbmsh493e720bedef33cp1782f4jsn345493804b80",  # Replace with your RapidAPI key
#         "X-RapidAPI-Host": "dietagram.p.rapidapi.com"
#     }
    
#     # Make the API call
#     response = requests.get(url, headers=headers, params=querystring)

#     # Extract the JSON data
#     data = response.json()

#     # Extract dishes information
#     dishes = data.get('dishes', [])

#     # Pass the dishes data to the HTML template
#     return render_template('fact.html', dishes=dishes)

# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fact():
    result = None
    if request.method == 'POST':
        activity = request.form['activity']
        duration = request.form['duration']

        # Call the API to get calorie data
        url = "https://calories-burned-by-api-ninjas.p.rapidapi.com/v1/caloriesburned"
        querystring = {"activity": activity, "duration": duration}
        headers = {
            "X-RapidAPI-Key": "yd0dfbe85fbmsh493e720bedef33cp1782f4jsn345493804b80",  # Replace with your RapidAPI key
            "X-RapidAPI-Host": "calories-burned-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            result = response.json()
        else:
            result = {"error": "API request failed"}

    return render_template('fact.html', result=result)
