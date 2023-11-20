function initialize(){

  var cord = {lat:25.73404, lng:-100.2996872};
  var map = new google.maps.Map(
    document.getElementById('map'),
    {zoom:20,
    center:cord
    }
  );

  var marker = new google.maps.Marker({
    icon:'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    position:cord,
    map: map
  })


  google.maps.event.addListener(map, "click", (event) => {
    addListing(event.latLng, map);
  });
}

function addMarker(location, map) {
  new google.maps.Marker({
    position: location,
    label: 'D',
    map: map,
    draggable: true
  });
}


var i=0
function addListing(location, map) {
  var iMax=1;

  if(i<iMax) {
    addMarker(location, map);
    i++;
    console.log('count: ',i);
  }
}
