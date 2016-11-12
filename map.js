function fixedPoints(){
  
}

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
