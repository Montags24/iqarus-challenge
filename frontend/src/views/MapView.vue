<script setup>
import { GoogleMap, CustomMarker } from 'vue3-google-map'

</script>

<template>
    <section v-if="onLine" class="mt-12 pt-3">
        <div class="flex flex-col sm:flex-row">
            <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
                @click="getMyLocation">Get my location</button>
            <div class="mx-auto relative mb-6 w-10/12 sm:w-2/3">
                <label for="labels-range-input" class="sr-only">Labels range</label>
                <input v-model="searchRadius" id="labels-range-input" type="range" value="50" min="0" max="100"
                    class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700">
                <span class="text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6">0km</span>
                <span
                    class="text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6">25km</span>
                <span
                    class="text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6">50km</span>
                <span class="text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6">100km</span>
            </div>

        </div>
        <GoogleMap :api-key="googleMapsApiKey" style="width: 100%; height: 75vh" :center="mapCenter" :zoom="mapZoom"
            @click="handleMapClick">
            <div v-if="ownLocationRequested">
                <CustomMarker :options="markerOptions">
                    <div style="text-align: center" class="hover:cursor-pointer">
                        <svg class="h-8 w-8 fill-current text-red-500" version="1.0" id="Layer_1"
                            xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                            viewBox="0 0 64 64" enable-background="new 0 0 64 64" xml:space="preserve">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                            <g id="SVGRepo_iconCarrier">
                                <path
                                    d="M32,0C18.746,0,8,10.746,8,24c0,5.219,1.711,10.008,4.555,13.93c0.051,0.094,0.059,0.199,0.117,0.289l16,24 C29.414,63.332,30.664,64,32,64s2.586-0.668,3.328-1.781l16-24c0.059-0.09,0.066-0.195,0.117-0.289C54.289,34.008,56,29.219,56,24 C56,10.746,45.254,0,32,0z M32,32c-4.418,0-8-3.582-8-8s3.582-8,8-8s8,3.582,8,8S36.418,32,32,32z">
                                </path>
                            </g>
                        </svg>
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
            selectedLocation: false,
            searchRadius: 50,
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