from flask import Flask, request, jsonify
from waitress import serve
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return 'hi ddd'


@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    response = jsonify({
        'city': util.fetch_city_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_county_names', methods=['GET'])
def get_county_names():
    response = jsonify({
        'county': util.fetch_county_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_homeType_names', methods=['GET'])
def get_homeType_names():
    response = jsonify({
        'homeType': util.fetch_home_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_levels_names', methods=['GET'])
def get_levels_names():
    response = jsonify({
        'levels': util.fetch_levels_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        pricePerSquareFoot = float(request.form['pricePerSquareFoot'])
        city = request.form['city']
        yearBuilt = int(request.form['yearBuilt'])
        bathrooms = int(request.form['bathrooms'])
        bedrooms = int(request.form['bedrooms'])
        livingAreaValue = float(request.form['livingAreaValue'])
        buildingArea = float(request.form['buildingArea'])
        garageSpaces = int(request.form['garageSpaces'])
        county = request.form['county']
        homeType = request.form['homeType']
        levels = request.form['levels']
        parking = int(request.form['parking'])
        hasGarage = int(request.form['hasGarage'])
        pool = int(request.form['pool'])
        spa = int(request.form['spa'])
        isNewConstruction = int(request.form['isNewConstruction'])

        # Call the utility function to get the estimated price
        estimated_price = util.get_estimated_price(
            pricePerSquareFoot, city, yearBuilt, bathrooms, bedrooms,
            livingAreaValue, buildingArea, garageSpaces, homeType, levels,
            parking, hasGarage, pool, spa, isNewConstruction, county
        )

        # Round the estimated price to two decimal places
        rounded_estimated_price = round(estimated_price, 3)

        response = jsonify({'estimated_price': rounded_estimated_price})

    except Exception as e:
        # Handle exceptions and return an error message
        response = jsonify({'error': str(e)})

    # Add CORS headers
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == "__main__":
    # Load artifacts before starting the server
    util.load_saved_artifacts()

    # Start the Flask app
    print("Starting Python Flask Server For Home Price Prediction...")
    print(util.fetch_city_names())
    print(util.fetch_county_names())
    print(util.fetch_levels_names())
    print(util.fetch_home_names())
    print(predict_home_price)
    serve(app, host='127.0.0.1', port=5000)
