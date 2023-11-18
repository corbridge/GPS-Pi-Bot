function initialize(){

  var cord = {lat:latitude, lng:longitude};
  var map = new google.maps.Map(
    document.getElementById('map'),
    {zoom:20,
    center:cord
    }
  );

  var marker = new google.maps.Marker({
    position:cord,
    map: map
  })

}