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

//*** Create the states outline and colors, styles

// Return a fillcolor if the state has been visited
function getColor(n) {
    var color;
    var visited = visited_states.includes(n);

    if (visited){
        color = "#46AA14";
    } else {
        color = "#DDDDDD";
    }
    return color;
}

// state styles
function getStyle(feature) {
    return {
        fillColor: getColor(feature.properties.name),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

L.geoJson(statesData, {style: getStyle}).addTo(map);

geojson = L.geoJson(statesData, {
    style: getStyle,
    onEachFeature: onEachFeature
}).addTo(map);

//*** Let's add US capital cities
var awesomeMarker;
var base_url = "https://capitals.leoandjen.com/"

for (var city in cities) {
    L.marker(
        [cities[city].latitude, cities[city].longitude],
        {
            // icon: awesomeMarker,
            icon: L.AwesomeMarkers.icon({icon: 'star', prefix: 'fa', markerColor: 'cadetblue', iconColor: '#fff'}),
            riseOnHover: true,
            title: cities[city].city_name + ', ' + cities[city].state_code
        }
    )
    .addTo(map)
    .bindPopup(cities[city].city_name + ', ' + cities[city].state_code + " [<a href=\"" + base_url + "#" + cities[city].state_code + "\">📸</a>]");
}

for (var capital in country_capitals) {
    L.marker(
        [country_capitals[capital].fields.lat, country_capitals[capital].fields.lon],
        {
            // icon: awesomeMarker,
            icon: L.AwesomeMarkers.icon({icon: 'star', prefix: 'fa', markerColor: 'red', iconColor: '#fff'}),
            riseOnHover: true,
            title: country_capitals[capital].fields.name
        }
    )
    .addTo(map)
    .bindPopup(country_capitals[capital].fields.name + " [<a href=\"" + base_url + "#" + country_capitals[capital].pk + "\">📸</a>]");

}