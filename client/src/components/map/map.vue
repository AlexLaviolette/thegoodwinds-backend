<template>
  <div>
    <h2 class="title">Set Your Location</h2>
    <input ref="pac" :model="pac" id="pac-input" class="controls" type="text" placeholder="Search Box" />
    <div class="map-holder">
      <div ref="map" id="map"></div>
    </div>
    <div id="get-weather">
      <button @click="setLocation" tag="button">Set Location</button>
    </div>
  </div>
</template>

<script>
import init from '@/utils/gplaces';

export default {
  name: 'map-component',
  data() {
    return {
      map: undefined,
      pac: '',
      google: null,
      markers: [],
      searchbox: null
    };
  },
  mounted: function () {
    this.initGMaps()
  },
  methods: {
    initGMaps: async function () {
      this.google = await init();
      this.map = new this.google.maps.Map(this.$refs.map, {
        center: { lat: 43.6425662, lng: -79.3892455 },
        zoom: 13,
        mapTypeId: "roadmap",
      });
      // Create the search box and link it to the UI element.
      const input = this.$refs.pac;
      this.searchBox = new this.google.maps.places.SearchBox(input);
      // this.map.controls[this.google.maps.ControlPosition.TOP_LEFT].push(input);
      // Bias the SearchBox results towards current map's viewport.
      this.map.addListener("bounds_changed", () => {
        this.searchBox.setBounds(this.map.getBounds());
      });
      // Listen for the event fired when the user selects a prediction and retrieve
      // more details for that place.
      this.searchBox.addListener("places_changed", this.placesChangeHandler)
    },
    placesChangeHandler: function () {
      const places = this.searchBox.getPlaces();
      if (places.length == 0) return
      this.saveLocation(places[0])

      // Clear out the old markers.
      this.markers.forEach((marker) => marker.setMap(null));
      this.markers = [];
      // For each place, get the icon, name and location.
      const bounds = new this.google.maps.LatLngBounds();
      places.forEach((place) => {
        if (!place.geometry || !place.geometry.location) {
          console.log("Returned place contains no geometry");
          return;
        }
        const icon = {
          url: place.icon,
          size: new this.google.maps.Size(71, 71),
          origin: new this.google.maps.Point(0, 0),
          anchor: new this.google.maps.Point(17, 34),
          scaledSize: new this.google.maps.Size(25, 25),
        };
        // Create a marker for each place.
        let map = this.map
        this.markers.push(
          new this.google.maps.Marker({
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
      this.map.fitBounds(bounds);
    },
    saveLocation: function (places) {
      localStorage.lat = places.geometry.location.lat();
      localStorage.lon = places.geometry.location.lng();
      let country = places.address_components.find((x) => x.types[0] == "country")
      if (country && country.short_name == "US") {
        localStorage.units = 'imperial';
      } else {
        localStorage.units = 'metric';
      }
    },
    setLocation: function () {
      this.$emit('setLocation')
      this.$router.push({name: 'home'})
    }
  },
  beforeDestroy: function () {
    this.google.maps.event.clearListeners(this.map, 'bounds_changed');
  }

};
</script>


<style scoped src="./map.styl" lang="stylus"></style>