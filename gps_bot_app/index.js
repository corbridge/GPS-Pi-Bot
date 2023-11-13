
window.lat = 25.7;
window.lng = -100.3;

var map;
var mark;
var lineCoords = [];

var initialize = function() {
 map  = new google.maps.Map(document.getElementById('map'), {center:{lat:latitude,lng:longitude},zoom:20});
 mark = new google.maps.Marker({position:{lat:latitude, lng:longitude}, map:map});
};

window.initialize = initialize;

console.log(latitude);
console.log(longitude);

map.setCenter({lat:latitude, lng:longitude, alt:0});
mark.setPosition({lat:latitude, lng:longitude, alt:0});

var lineCoordinatesPath = new google.maps.Polyline({
   path: lineCoords,
   geodesic: true,
   strokeColor: '#2E10FF'
 });

lineCoordinatesPath.setMap(map);

