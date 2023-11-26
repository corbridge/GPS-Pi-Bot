var main_marker;
var main_map;
var lineCoords = [];

function initialize(){

  var cord = {lat:lat, lng:lng};
  main_map = new google.maps.Map(
    document.getElementById('map'),
    {zoom:20,
    center:cord
    }
  );

   main_marker = new google.maps.Marker({
    icon:'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    position:cord,
    map: main_map
  })

  const topControl = document.createElement("div");
  const destination_created = createDestination(main_map);

  topControl.appendChild(destination_created);
  main_map.controls[google.maps.ControlPosition.TOP_CENTER].push(topControl);

  const bottomControl = document.createElement("div");
  const destination_erased = eraseDestination(main_map, destination_created);

  bottomControl.appendChild(destination_erased);
  main_map.controls[google.maps.ControlPosition.BOTTOM_CENTER].push(bottomControl);

  google.maps.event.addListener(main_map, "click", (event) => {
    addListing(event.latLng, main_map, destination_created);
  });  

}

function addMarker(location, map) {
  marker = new google.maps.Marker({
    position: location,
    label: 'D',
    map: map,
    draggable: true
  });
return marker;
}


var i=0
function addListing(location, map, controller) {
  var iMax=1;

  if(i<iMax) {
    marker = addMarker(location, map);
    i++;
    console.log('count: ',i);
  }

controller.addEventListener("click", () => {
var dest_lat = marker.getPosition().lat();
var dest_lng = marker.getPosition().lng();

console.log("Latitud destino: ",dest_lat);
console.log("Longitud destino: ",dest_lng);

});
}


function createDestination(map) {
  const controlButton = document.createElement("button");

  // Set CSS for the control.
  controlButton.style.backgroundColor = "#fff";
  controlButton.style.border = "2px solid #fff";
  controlButton.style.borderRadius = "3px";
  controlButton.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
  controlButton.style.color = "rgb(25,25,25)";
  controlButton.style.cursor = "pointer";
  controlButton.style.fontFamily = "Roboto,Arial,sans-serif";
  controlButton.style.fontSize = "16px";
  controlButton.style.lineHeight = "38px";
  controlButton.style.margin = "8px 0 22px";
  controlButton.style.padding = "0 5px";
  controlButton.style.textAlign = "center";
  controlButton.textContent = "Set Destination";
  controlButton.title = "Click to recenter the map";
  controlButton.type = "button";
  // Setup the click event listeners: simply set the map to Chicago.
  controlButton.addEventListener("click", () => {
    controlButton.style.backgroundColor = '#6DC813';
    controlButton.textContent = 'Destination ready!';
    controlButton.style.border = "2px solid #6DC813";
  });
return controlButton;
}


function eraseDestination(map, destination_button) {
  const controlButton = document.createElement("button");

  // Set CSS for the control.
  controlButton.style.backgroundColor = "#fff";
  controlButton.style.border = "2px solid #fff";
  controlButton.style.borderRadius = "3px";
  controlButton.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
  controlButton.style.color = "rgb(25,25,25)";
  controlButton.style.cursor = "pointer";
  controlButton.style.fontFamily = "Roboto,Arial,sans-serif";
  controlButton.style.fontSize = "16px";
  controlButton.style.lineHeight = "38px";
  controlButton.style.margin = "8px 0 22px";
  controlButton.style.padding = "0 5px";
  controlButton.style.textAlign = "center";
  controlButton.textContent = "Clear Destination";
  controlButton.title = "Click to recenter the map";
  controlButton.type = "button";
  // Setup the click event listeners: simply set the map to Chicago.
  controlButton.addEventListener("click", () => {
    destination_button.style.backgroundColor = '#FFF';
    destination_button.textContent = 'Set Destination';
    destination_button.style.border = "2px solid #FFF";
  });
return controlButton;
}
window.lat = 25.73408
window.lng = -100.29968


const firebaseConfig = {
    apiKey: "AIzaSyCndLrX1QvxSug-lwX5-LfV1pTs_IegH3s",
    authDomain: "gps-pi-bot.firebaseapp.com",
    databaseURL: "https://gps-pi-bot-default-rtdb.firebaseio.com",
    projectId: "gps-pi-bot",
    storageBucket: "gps-pi-bot.appspot.com",
    messagingSenderId: "237945598717",
    appId: "1:237945598717:web:3143f5d47f0f8a8fb84494"
  };

window.initialize = initialize;

firebase.initializeApp(firebaseConfig );

var ref = firebase.database().ref();

ref.on('value', function(snapshot) {
  var gps = snapshot.val();
  console.log(typeof gps.latitude);
  console.log(typeof gps.longitude);
  lat = gps.latitude;
  lng = gps.longitude;

  main_marker.setPosition({lat:lat, lng:lng, alt:0});
  
  lineCoords.push(new google.maps.LatLng(lat, lng));

  var lineCoordinatesPath = new google.maps.Polyline({
    path: lineCoords,
    geodesic: true,
    strokeColor: '#2E10FF'
  });
  
  lineCoordinatesPath.setMap(main_map);
});
