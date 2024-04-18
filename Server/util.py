import pickle
import json
import numpy as np

__cityCsv = None
__city = None
__countyCsv = None
__county = None
__homeTypeCsv = None
__homeType = None
__levelsCsv = None
__levels = None
__data_columns = None
__model = None


def get_estimated_price(pricePerSquareFoot,city,yearBuilt,bathrooms,bedrooms,livingAreaValue,buildingArea,garageSpaces,homeType,levels,parking,hasGarage,pool,spa,isNewConstruction,county):

        feature_vector = np.zeros(len(__model.coef_))

        city_encoder = {city_name: label for label, city_name in enumerate(__city)}

        if city in city_encoder:
            encoded_city = city_encoder[city]
            feature_vector[12] = encoded_city  # Set the label-encoded city feature
        else:
            print(f"Warning: City '{city}' not found in label encoder.")

        county_encoder = {county_name: label for label, county_name in enumerate(__county)}

        if county in county_encoder:
            encoded_county = county_encoder[county]
            feature_vector[13] = encoded_county  # Set the label-encoded city feature
        else:
            print(f"Warning: County '{county}' not found in label encoder.")

        homeType_encoder = {homeType_name: label for label, homeType_name in enumerate(__homeType)}
        if homeType in homeType_encoder:
            encoded_homeType = homeType_encoder[homeType]
            feature_vector[14] = encoded_homeType  # Set the label-encoded city feature
        else:
            print(f"Warning: County '{homeType}' not found in label encoder.")

        levels_encoder = {levels_name: label for label, levels_name in enumerate(__levels)}
        if levels in levels_encoder:
            encoded_levels = levels_encoder[levels]
            feature_vector[15] = encoded_levels  # Set the label-encoded city feature
        else:
            print(f"Warning: County '{levels}' not found in label encoder.")

        feature_vector[0] = pricePerSquareFoot
        feature_vector[1] = yearBuilt
        feature_vector[2] = livingAreaValue
        feature_vector[3] = bathrooms
        feature_vector[4] = bedrooms
        feature_vector[5] = buildingArea
        feature_vector[6] = parking
        feature_vector[7] = garageSpaces
        feature_vector[8] = hasGarage
        feature_vector[9] = pool
        feature_vector[10] = spa
        feature_vector[11] = isNewConstruction

          # Use a different index for the original city string

    # Make prediction
        return __model.predict(np.array([feature_vector]))[0]


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __cityCsv
    global __city

    with open("./artifacts/unique_values_city.json", "r") as f:
        __cityCsv = json.load(f)['unique_values_in_specific_column']
        __city = __cityCsv[:]

    global __countyCsv
    global __county

    with open("./artifacts/unique_values_county.json", "r") as f:
        __countyCsv = json.load(f)['unique_values_in_specific_column']
        __county = __countyCsv[:]

    global __levelsCsv
    global __levels

    with open("./artifacts/unique_values_levels.json", "r") as f:
        __levelsCsv = json.load(f)['unique_values_in_specific_column']
        __levels = __levelsCsv[:]

    global __homeTypeCsv
    global __homeType

    with open("./artifacts/unique_values_homeType.json", "r") as f:
        __homeTypeCsv = json.load(f)['unique_values_in_specific_column']
        __homeType = __homeTypeCsv[:]

    global __data_columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    global __model
    if __model is None:
        with open('./artifacts/Georgia_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def fetch_city_names():
    return __city


def fetch_county_names():
    return __county


def fetch_home_names():
    return __homeType


def fetch_levels_names():
    return __levels


def fetch_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(fetch_city_names())
    print(fetch_county_names())
    print(fetch_levels_names())
    print(fetch_home_names())
    print(get_estimated_price(150,'acworth', 2005, 2, 3, 8000.00, 1800, 1,'single_family','two', 1, 1, 0, 0, 0, 'cobb county'))



