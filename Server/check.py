from flask import Flask, request, jsonify
import util
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return 'hi ddd'


@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    try:
        print("Handling /get_city_names request...")

        # Fetch city names
        city_names = util.fetch_city_names()

        # Log the retrieved city names
        print(f"Retrieved city names: {city_names}")

        # Create and return the response
        response = jsonify({'city': city_names})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        # Log the exception for debugging
        print(f"Error fetching city names: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/get_county_names', methods=['GET'])
def get_county_names():
    response = jsonify({
        'county': util.get_county_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_homeType_names', methods=['GET'])
def get_home_names():
    response = jsonify({
        'homeType': util.get_home_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_levels_names', methods=['GET'])
def get_levels_names():
    response = jsonify({
        'levels': util.get_levels_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        pricePerSquareFoot = float(request.form['pricePerSquareFoot'])
        city= request.form['city']
        yearBuilt = int(request.form['yearBuilt'])
        bathrooms = float(request.form['bathrooms'])
        bedrooms = float(request.form['bedrooms'])
        livingAreaValue = float(request.form['livingAreaValue'])
        buildingArea = float(request.form['buildingArea'])
        garageSpaces = float(request.form['garageSpaces'])
        county = request.form['county']
        homeType = request.form['homeType']
        levels = request.form['levels']
        parking = int(request.form['parking'])
        hasGarage= int(request.form['hasGarage'])
        pool = int(request.form['pool'])
        spa = int(request.form['spa'])
        isNewConstruction = int(request.form['isNewConstruction'])


        response = jsonify({
            'estimated_price': util.get_estimated_price(pricePerSquareFoot,city,yearBuilt,bathrooms,bedrooms,livingAreaValue,buildingArea,garageSpaces,homeType,levels,parking,hasGarage,pool,spa,isNewConstruction,county)
        })
    except Exception as e:
        response = jsonify({
            'error': str(e)
        })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    # Use Waitress to serve the Flask app
    serve(app, host='127.0.0.1', port=5000)
    print (util.fetch_city_names())
    # Load artifacts before starting the server
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()