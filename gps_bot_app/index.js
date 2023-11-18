
//hi
window.lat = 25.7;
window.lng = -100.3;

var map;
var mark;
var lineCoords = [];

function updateVariables(){

var lat = latitude;
var long = longitude;
console.log(lat);
console.log(long);

}

var initialize = function() {
 var lat = latitude;
 var long = longitude;

 map  = new google.maps.Map(document.getElementById('map'), {center:{lat:lat,lng:long},zoom:20});
 mark = new google.maps.Marker({position:{lat:lat, lng:long}, map:map});

};

window.initialize = initialize;

map.setCenter({lat:lat, lng:long, alt:0});
mark.setPosition({lat:lat, lng:long, alt:0});

var lineCoordinatesPath = new google.maps.Polyline({
   path: lineCoords,
   geodesic: true,
   strokeColor: '#2E10FF'
 });

lineCoordinatesPath.setMap(map);

