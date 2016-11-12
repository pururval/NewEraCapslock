var map;

function initialize() {
  var mapProp = {
    center:new google.maps.LatLng(39.75, -95),
    zoom:5,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
google.maps.event.addDomListener(window, 'load', initialize);
initialize();
