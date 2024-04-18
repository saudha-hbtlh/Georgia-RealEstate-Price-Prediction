


function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
    var hasGarageValue = document.getElementById("uihasgarage").value;
    var hasGarageNumericValue = hasGarageValue === "Yes" ? 1 : 0;
    var hasParkingValue = document.getElementById("uiparking").value;
    var hasPoolValue = document.getElementById("uipool").value;
    var hasSpaValue = document.getElementById("uispa").value;
    var isNewConstructionValue = document.getElementById("uinewconstruction").value;
    var hasGarageSpacesValue = document.getElementById("uihasgaragespc").value;
    var sqft = document.getElementById("uiSqft").value;  // Fix here
    var levels = document.getElementById("uilevels").value;  // Fix here
    var bathrooms = document.getElementById("uibathrooms").value;
    var bedrooms = document.getElementById("uibedrooms").value;
    var city = document.getElementById("uicity").value;
    var county = document.getElementById("uicounty").value;
    var homeType = document.getElementById("uihmtype").value;
    var estPrice = document.getElementById("uiEstimatedPrice");
    var livingAreaValue = document.getElementById("uiliving").value;
    var buildingArea = document.getElementById("uibuildingarea").value;
    var yearBuilt = document.getElementById("uiyearbuilt").value;

  var url = "http://127.0.0.1:5000/predict_home_price"

  $.post(url, {
      hasGarage: hasGarageNumericValue,
        hasParking: hasParkingValue,
        hasPool: hasPoolValue,
        hasSpa: hasSpaValue,
        isNewConstruction: isNewConstructionValue,
        garageSpaces: hasGarageSpacesValue,
        pricePerSquareFoot: sqft,
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        city: city,
        county: county,
		levels:levels,
        homeType: homeType,
        livingAreaValue: livingAreaValue,
        buildingArea: buildingArea,
        yearBuilt: yearBuilt
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_city_names";
  $.get(url,function(data, status) {
      console.log("got response for get_city_names request")
	  console.log("Data:", data);
    console.log("Status:", status);;
      if(data) {
          var city = data.city;
          var uicity = document.getElementById("uicity");
          $('#uicity').empty();
          for(var i in city) {
              var opt = new Option(city[i]);
              $('#uicity').append(opt);
			  
			
    // Rest of your code...
});
          }
      }
  });
}

window.onload = onPageLoad;


