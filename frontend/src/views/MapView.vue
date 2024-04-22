<script setup>
import { GoogleMap, CustomMarker } from 'vue3-google-map'

</script>

<template>
    <section v-if="onLine">
        <button class="mt-12 px-2 py-2 rounded-sm border border-red-400 bg-slate-50" @click="getMyLocation">My
            location</button>
        <GoogleMap :api-key="googleMapsApiKey" style="width: 100%; height: 75vh" :center="mapCenter" :zoom="mapZoom"
            @click="handleMapClick">
            <div v-if="ownLocationRequested">
                <CustomMarker :options="markerOptions">
                    <div style="text-align: center" class="hover:cursor-pointer">
                        <v-icon name="fa-map-marker-alt" scale="2" fill="red" />
                    </div>
                </CustomMarker>
            </div>
            <div v-if="selectedLocation">
                <CustomMarker :options="selectedLocationMarkerOptions">
                    <div style="text-align: center" class="hover:cursor-pointer">
                        <v-icon name="fa-map-marker-alt" scale="2" fill="orange" />
                    </div>
                </CustomMarker>
            </div>
        </GoogleMap>
    </section>
</template>

<script>
import { checkLocationPermission } from '@/stores/geoLocation';
export default {
    props: {
        user: {
            type: Object,
        },
        onLine: {
            type: Boolean,
        },
    },
    data() {
        return {
            googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
            mapZoom: 2,
            mapCenter: { lat: 33, lng: 44 },
            latitude: '',
            longitude: '',
            userPosition: {},
            markerOptions: {},
            ownLocationRequested: false,
            selectedLocationMarkerOptions: {},
            selectedLocationCenter: { lat: 0, lng: 0 },
            selectedLocation: false
        }
    },
    methods: {
        async getMyLocation() {
            try {
                const userPosition = await checkLocationPermission();
                this.latitude = userPosition.coords.latitude
                this.longitude = userPosition.coords.longitude
                this.userPosition = { lat: this.latitude, lng: this.longitude }
                this.markerOptions = { position: this.userPosition, label: 'U', title: 'Current Location' }
                this.mapCenter = this.userPosition
                this.mapZoom = 12
                this.ownLocationRequested = true
            } catch (error) {
                console.error('Error getting location:', error);
                // Handle error
            }
        },
        handleMapClick(event) {
            // Get the latitude and longitude of the clicked point
            const clickedLatLng = event.latLng;
            const lat = clickedLatLng.lat();
            const lng = clickedLatLng.lng();

            this.selectedLocationCenter = { lat: lat, lng: lng }
            this.selectedLocation = true
            this.selectedLocationMarkerOptions = { position: this.selectedLocationCenter }
            this.mapCenter = this.selectedLocationCenter
        }
    },


}
</script>

<style lang="scss" scoped></style>