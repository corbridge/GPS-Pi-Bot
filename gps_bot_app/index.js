window.lat = 26.5;
window.lng = -100.5;

var map;
var mark;
var lineCoords = [];
  
var initialize = function() {
  map  = new google.maps.Map(document.getElementById('map-canvas'), {center:{lat:lat,lng:lng},zoom:12});
  mark = new google.maps.Marker({position:{lat:lat, lng:lng}, map:map});
};

const firebaseConfig = {
    apiKey: "AIzaSyCndLrX1QvxSug-lwX5-LfV1pTs_IegH3s",
    authDomain: "gps-pi-bot.firebaseapp.com",
    projectId: "https://gps-pi-bot-default-rtdb.firebaseio.com",
    storageBucket: "gps-pi-bot",
    messagingSenderId: "gps-pi-bot.appspot.com",
    appId: "237945598717",
    measurementId: "1:237945598717:web:3143f5d47f0f8a8fb84494"
    };

window.initialize = initialize;

firebase.initializeApp(firebaseConfig );

var ref = firebase.database().ref();

ref.on("value", function(snapshot) {
  var gps = snapshot.val();
  console.log(gps.latitude);
  console.log(gps.longitude);
  lat = gps.latitude;
  lng = gps.longitude;

  map.setCenter({lat:lat, lng:lng, alt:0});
  mark.setPosition({lat:lat, lng:lng, alt:0});
  
  lineCoords.push(new google.maps.LatLng(lat, lng));

  var lineCoordinatesPath = new google.maps.Polyline({
    path: lineCoords,
    geodesic: true,
    strokeColor: '#2E10FF'
  });
  
  lineCoordinatesPath.setMap(map);
}, function (error) {
  console.log("Error: " + error.code);
});