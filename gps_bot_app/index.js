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

  const topControl = document.createElement("div");
  const destination_created = createDestination(map);

  topControl.appendChild(destination_created);
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(topControl);

  const bottomControl = document.createElement("div");
  const destination_erased = eraseDestination(map, destination_created);

  bottomControl.appendChild(destination_erased);
  map.controls[google.maps.ControlPosition.BOTTOM_CENTER].push(bottomControl);

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
function addListing(location, map) {
  var iMax=1;

  if(i<iMax) {
    marker = addMarker(location, map);
    i++;
    console.log('count: ',i);
  }
var dest_lat = marker.getPosition().lat();
var dest_lng = marker.getPosition().lng();

console.log("Latitud destino: ",dest_lat);
console.log("Longitud destino: ",dest_lng);

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
