document.addEventListener('DOMContentLoaded', function() {
    function getParkingValue() {
        var uiparking = document.getElementsByName("uiparking");
        for (var i = 0; i < uiparking.length; i++) {
          if (uiparking[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }
    
    function getGarageValue() {
        var uigarage = document.getElementsByName("uigarage");
        for (var i = 0; i < uigarage.length; i++) {
          if (uigarage[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }
    
    function getGarageSpcValue() {
        var uigaragespc = document.getElementsByName("uigaragespc");
        for (var i = 0; i < uigaragespc.length; i++) {
          if (uigaragespc[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }
    
    function getPoolValue() {
        var uipool = document.getElementsByName("uipool");
        for (var i = 0; i < uipool.length; i++) {
          if (uipool[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }
    
    function getSpaValue() {
        var uispa = document.getElementsByName("uispa");
        for (var i = 0; i < uispa.length; i++) {
          if (uispa[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }
    
    function getConstructionValue() {
        var uiconstruction = document.getElementsByName("uiconstruction");
        for (var i = 0; i < uiconstruction.length; i++) {
          if (uiconstruction[i].checked) {
            return parseInt(i) + 1;
          }
        }
        return -1; // Invalid Value
      }

    function onClickedEstimatePrice() {
        console.log("Estimate price button clicked");
    
        // Get input values
        var sqft = parseFloat(document.getElementById("uiSqft").value);
        var yearbuilt = parseInt(document.getElementById("uiyrbuilt").value);
        var livingareavalue = parseFloat(document.getElementById("uilivingarea").value);
        var buildingarea = parseFloat(document.getElementById("uibuildingarea").value);
        var bathrooms = parseInt(document.getElementById("uibathrooms").value);
        var bedrooms = parseInt(document.getElementById("uibedrooms").value);
    
        // Get radio button values
        var parking = getParkingValue();
        var spa = getSpaValue();
        var garagespc = getGarageSpcValue();
        var garage = getGarageValue();
        var pool = getPoolValue();
        var construction = getConstructionValue();
    
        // Get dropdown values
        var city = document.getElementById("uicity").value;
        var county = document.getElementById("uicounty").value;
        var levels = document.getElementById("uilevels").value;
        var hometype = document.getElementById("uihometype").value;
    
        var estPrice = document.getElementById("uiEstimatedPrice");
    
        // Make sure all required values are valid
        if (isNaN(sqft) || isNaN(yearbuilt) || isNaN(livingareavalue) || isNaN(buildingarea) ||
            isNaN(bathrooms) || isNaN(bedrooms) || isNaN(parking) || isNaN(spa) || isNaN(garagespc) ||
            isNaN(garage) || isNaN(pool) || isNaN(construction) || city === "" || county === "" ||
            levels === "" || hometype === "") {
            console.error("Invalid input. Please fill in all required fields with valid numbers.");
            return;
        }
    
        var url = "http://127.0.0.1:5000/predict_home_price";
    
        $.post(url, {
            pricePerSquareFoot: sqft,
            yearBuilt: yearbuilt,
            livingAreaValue: livingareavalue,
            buildingArea: buildingarea,
            bedrooms: bedrooms,
            bathrooms: bathrooms,
            parking: parking,
            pool: pool,
            spa: spa,
            hasGarage: garage,
            isNewConstruction: construction,
            garageSpaces: garagespc,
            city: city,
            county: county,
            homeType: hometype,
            levels: levels
        })
        .done(function(data, status) {
            console.log(data.estimated_price);
            estPrice.innerHTML = "<h2>" + "$" + data.estimated_price.toString() + "</h2>";
            console.log(status);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            console.error("AJAX request failed:", textStatus, errorThrown);
            // Handle the failure, e.g., show an error message to the user
        });
    }

  function onPageLoad() {
    console.log("document loaded");

    var urlCity = "http://127.0.0.1:5000/get_city_names";
    $.get(urlCity, function (data, status) {
        console.log("got response for get_city_names request");
        try {
            if (data && data.city) {
                var city = data.city;
                var uicity = document.getElementById("uicity");

                if (uicity) {
                    $('#uicity').empty();
                    for (var i in city) {
                        var opt = new Option(city[i]);
                        $('#uicity').append(opt);
                    }
                } else {
                    console.error("Element with ID 'uicity' not found in the DOM.");
                }
            } else {
                console.error("Invalid or missing data in the server response.");
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });

    var urlCounty = "http://127.0.0.1:5000/get_county_names";
    $.get(urlCounty, function (data, status) {
        console.log("got response for get_county_names request");
        try {
            if (data && data.county) {
                var county = data.county;
                var uicounty = document.getElementById("uicounty");

                if (uicounty) {
                    $('#uicounty').empty();
                    for (var i in county) {
                        var opt = new Option(county[i]);
                        $('#uicounty').append(opt);
                    }
                } else {
                    console.error("Element with ID 'uicounty' not found in the DOM.");
                }
            } else {
                console.error("Invalid or missing data in the server response.");
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });

    var urlLevels = "http://127.0.0.1:5000/get_levels_names";
    $.get(urlLevels, function (data, status) {
        console.log("got response for fetch_levels_names request");
        try {
            if (data && data.levels) {
                var levels = data.levels;
                var uilevels = document.getElementById("uilevels");

                if (uilevels) {
                    $('#uilevels').empty();
                    for (var i in levels) {
                        var opt = new Option(levels[i]);
                        $('#uilevels').append(opt);
                    }
                } else {
                    console.error("Element with ID 'uilevels' not found in the DOM.");
                }
            } else {
                console.error("Invalid or missing data in the server response.");
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });

    var urlHomeTypes = "http://127.0.0.1:5000/get_homeType_names";
    $.get(urlHomeTypes, function (data, status) {
        console.log("got response for get_homeType_names request");
        try {
            if (data && data.homeType) {
                var homeType = data.homeType;
                var uihometype = document.getElementById("uihometype");

                if (uihometype) {
                    $('#uihometype').empty();
                    for (var i in homeType) {
                        var opt = new Option(homeType[i]);
                        $('#uihometype').append(opt);
                    }
                } else {
                    console.error("Element with ID 'uihometype' not found in the DOM.");
                }
            } else {
                console.error("Invalid or missing data in the server response.");
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });
}

window.onload = onPageLoad;})