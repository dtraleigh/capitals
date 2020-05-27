//*** Create the Map
// Map start
var mapboxAccessToken = 'pk.eyJ1IjoiY29waGVhZDU2NyIsImEiOiJjanF2MGg5c3gwcTVwNDNuM2FoemcyZHExIn0.w4xEV2KZ7kGEhlfoWpE_wg';
var map = L.map('map', {fullscreenControl: true}).setView([37.8, -96], 3);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + mapboxAccessToken, {
    id: 'mapbox.light'
}).addTo(map);

L.geoJson(statesData).addTo(map);
//*** Map create end

//*** Control elements
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = (props ? '<b>' + props.name + '</b><br />'
        : 'Hover over a state');
};

info.addTo(map);
//*** end control

//*** Stuff that happens when you hover a mouse over the state
// Mouse in
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }

    info.update(layer.feature.properties);
}

var geojson;

// Mouse out
function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

geojson = L.geoJson(statesData, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);

//*** Let's add capital cities
var awesomeMarker;

for (var city in cities) {
    L.marker(
            [cities[city].latitude, cities[city].longitude],
            {
                // icon: awesomeMarker,
                icon: L.AwesomeMarkers.icon({icon: 'star', prefix: 'fa', markerColor: 'cadetblue', iconColor: '#fff'}),
                riseOnHover: true,
                title: cities[city].city_name + ', ' + cities[city].state_name
            }
        )
        .addTo(map)
        .on('click', function(e) {
            gotoLocation(this.getLatLng().lat, this.getLatLng().lng, 7);
        })
        .bindPopup(cities[city].city_name + ', ' + cities[city].state_name);
}