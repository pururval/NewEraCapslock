function fixedPoints(){
  
}
var map;

function initialize() {
  var mapProp = {
    center:new google.maps.LatLng(39.8282, -98.5795),
    zoom:4,
    mapTypeId:google.maps.MapTypeId.ROADMAP,
    var styledMapType = new google.maps.StyledMapType([{"featureType":"water","elementType":"geometry","stylers":[{"color":"#e9e9e9"},{"lightness":17}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffffff"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#ffffff"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":16}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#dedede"},{"lightness":21}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#ffffff"},{"lightness":16}]},{"elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#333333"},{"lightness":40}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#f2f2f2"},{"lightness":19}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#fefefe"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#fefefe"},{"lightness":17},{"weight":1.2}]}]
  };
  map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
google.maps.event.addDomListener(window, 'load', initialize);
initialize();

function myMap(){
  var mapCanvas = document.getElementById("map");
  //NE HQ Buffalo:
  var mapCenter = new google.maps.LatLng(42.889238,-78.877981);
  //NE Sao Paulo
  var mapSP = new google.maps.LatLng(-23.26051,-45.88896);

  var mapOptions = {
    center: mapCenter,
    zoom: 3,
    //mapTypeId: google.maps.MapTypeId.HYBRID
  };
  var map = new google.maps.Map(mapCanvas, mapOptions);

  //input
  var locations = [mapCenter, mapSP];
  var location_length = locations.length;
  var markers = Array();
  var marker, i;

  for(i=0;i<location_length;i++){
    marker = new google.maps.Marker({
      position:locations[i],
      //icon:path_to_icon_image
      map:map
    });
    markers.push(marker);
    markers[i].setMap(map);
  }
}
