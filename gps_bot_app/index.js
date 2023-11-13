
window.lat = 25.7;
window.lng = -100.3;

var map;
var mark;
var lineCoords = [];

var initialize = function() {
 map  = new google.maps.Map(document.getElementById('map'), {center:{lat:lat,lng:lng},zoom:20});
 mark = new google.maps.Marker({position:{lat:lat, lng:lng}, map:map});
};

window.initialize = initialize;
const spawner = require('child_process').spawn;

const data_pass = ['Send it'];

console.log('Data sent: ', data_pass);

const python_process = spawner('python', ['/home/picornelio/projects/GPS-Pi-Bot/gps_bot/main.py', JSON.stringify(data_pass)]);

python_process.stdout.on('data', (data) => {
  console.log('data received: ', JSON.parse(data)[1]);
});

map.setCenter({lat:JSON.parse(data)[1].latitude, lng:JSON.parse(data)[1].longitude, alt:0});
mark.setPosition({lat:JSON.parse(data)[1].latitude, lng:JSON.parse(data)[1].longitude, alt:0});

var lineCoordinatesPath = new google.maps.Polyline({
   path: lineCoords,
   geodesic: true,
   strokeColor: '#2E10FF'
 });

lineCoordinatesPath.setMap(map);
