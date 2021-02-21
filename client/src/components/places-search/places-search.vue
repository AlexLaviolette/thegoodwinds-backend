<template>
  <!-- <div>
    <input type="text" name="places-query">
  </div> -->
  <div class="holder">
    <input id="pac-input" class="controls" type="text" placeholder="Search Box" />
    <div id="map"></div>
    <div id="get-weather">
      <router-link :to="{ name: 'home', query: { lat: coords.lat, lon: coords.lon, units: units}}" tag="button">Get Weather</router-link>
    </div>
  </div>
</template>


<script>
import init from '../../utils/gplaces';

export default {
  name: 'App',
  data() {
    return {
      coords: {
          'lat': 43.6425662,
          'lon': -79.3892455
      },
      units: 'metric'
    };
  },
  async mounted() {
    this.$nextTick(async function () {
      const google = await init();
      const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 43.6425662, lng: -79.3892455 },
        zoom: 13,
        mapTypeId: "roadmap",
      });
      // Create the search box and link it to the UI element.
      const input = document.getElementById("pac-input");
      const searchBox = new google.maps.places.SearchBox(input);
      map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
      // Bias the SearchBox results towards current map's viewport.
      map.addListener("bounds_changed", () => {
        searchBox.setBounds(map.getBounds());
      });
      let markers = [];
      // Listen for the event fired when the user selects a prediction and retrieve
      // more details for that place.
      searchBox.addListener("places_changed", () => {
        const places = searchBox.getPlaces();

        if (places.length == 0) {
          return;
        } else {
          this.coords = {
            'lat': places[0].geometry.location.lat(),
            'lon': places[0].geometry.location.lng()
          };
          let country = places[0].address_components.find(function(x) {return x.types[0] == "country";})
          if (country && country.short_name == "US") {
            this.units = 'imperial';
          }
        }

        // Clear out the old markers.
        markers.forEach((marker) => {
          marker.setMap(null);
        });
        markers = [];
        // For each place, get the icon, name and location.
        const bounds = new google.maps.LatLngBounds();
        places.forEach((place) => {
          if (!place.geometry || !place.geometry.location) {
            console.log("Returned place contains no geometry");
            return;
          }
          const icon = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25),
          };
          // Create a marker for each place.
          markers.push(
            new google.maps.Marker({
              map,
              icon,
              title: place.name,
              position: place.geometry.location,
            })
          );

          if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        });
        map.fitBounds(bounds);
      });
    })
  },

};
</script>


<style src="./places-search.styl" lang="stylus"></style>