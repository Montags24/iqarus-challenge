<script setup>
import { GoogleMap, CustomMarker, Circle, InfoWindow } from 'vue3-google-map'

</script>

<template>
    <!-- Sets a dark overlay when modal is visible -->
    <div v-if="settingsModalVisibility" class="fixed inset-0 bg-black opacity-50 z-20"></div>
    <section v-if="onLine" class="mt-11 pt-3 relative">
        <SettingsModal :visible="settingsModalVisibility" @toggleModalVisibility="toggleSettingsModalVisibility"
            @saveSettings="saveSettings">
        </SettingsModal>

        <!-- GET OWN LOCATION BUTTON -->
        <div class="absolute top-6 right-32 z-10">
            <button class="bg-orange-500 hover:bg-orange-600  font-bold py-2 px-4 rounded absolute"
                @click="getMyLocation">
                <svg class="size-5 fill-current text-white" viewBox="0 0 24 24" fill="none"
                    xmlns="http://www.w3.org/2000/svg" stroke="#000000">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <path
                            d="M19 12C19 15.866 15.866 19 12 19M19 12C19 8.13401 15.866 5 12 5M19 12H21M12 19C8.13401 19 5 15.866 5 12M12 19V21M5 12C5 8.13401 8.13401 5 12 5M5 12H3M12 5V3M15 12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12C9 10.3431 10.3431 9 12 9C13.6569 9 15 10.3431 15 12Z"
                            stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    </g>
                </svg>
            </button>
        </div>
        <!-- SETTINGS MODAL BUTTON -->
        <div class="absolute top-6 right-16 z-10">
            <button class="bg-orange-500 hover:bg-orange-600  font-bold py-2 px-4 rounded absolute"
                @click="toggleSettingsModalVisibility"><svg class="h-5 w-5 fill-current text-white" viewBox="0 0 24 24"
                    fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M12.7848 0.449982C13.8239 0.449982 14.7167 1.16546 14.9122 2.15495L14.9991 2.59495C15.3408 4.32442 17.1859 5.35722 18.9016 4.7794L19.3383 4.63233C20.3199 4.30175 21.4054 4.69358 21.9249 5.56605L22.7097 6.88386C23.2293 7.75636 23.0365 8.86366 22.2504 9.52253L21.9008 9.81555C20.5267 10.9672 20.5267 13.0328 21.9008 14.1844L22.2504 14.4774C23.0365 15.1363 23.2293 16.2436 22.7097 17.1161L21.925 18.4339C21.4054 19.3064 20.3199 19.6982 19.3382 19.3676L18.9017 19.2205C17.1859 18.6426 15.3408 19.6754 14.9991 21.405L14.9122 21.845C14.7167 22.8345 13.8239 23.55 12.7848 23.55H11.2152C10.1761 23.55 9.28331 22.8345 9.08781 21.8451L9.00082 21.4048C8.65909 19.6754 6.81395 18.6426 5.09822 19.2205L4.66179 19.3675C3.68016 19.6982 2.59465 19.3063 2.07505 18.4338L1.2903 17.1161C0.770719 16.2436 0.963446 15.1363 1.74956 14.4774L2.09922 14.1844C3.47324 13.0327 3.47324 10.9672 2.09922 9.8156L1.74956 9.52254C0.963446 8.86366 0.77072 7.75638 1.2903 6.8839L2.07508 5.56608C2.59466 4.69359 3.68014 4.30176 4.66176 4.63236L5.09831 4.77939C6.81401 5.35722 8.65909 4.32449 9.00082 2.59506L9.0878 2.15487C9.28331 1.16542 10.176 0.449982 11.2152 0.449982H12.7848ZM12 15.3C13.8225 15.3 15.3 13.8225 15.3 12C15.3 10.1774 13.8225 8.69998 12 8.69998C10.1774 8.69998 8.69997 10.1774 8.69997 12C8.69997 13.8225 10.1774 15.3 12 15.3Z">
                        </path>
                    </g>
                </svg>
            </button>
        </div>
        <!-- SEARCH AREA BUTTON -->
        <div class="absolute bottom-4 left-0 right-0 z-10 flex justify-center">
            <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
                @click="searchArea">Search area
            </button>
        </div>
        <!-- START GOOGLE MAPS COMPONENT -->
        <GoogleMap class="h-[calc(100vh-128px)]" :api-key="googleMapsApiKey" style="width: 100%" :center="mapCenter"
            :zoom="mapZoom" :fullscreenControl="false" @click="handleMapClick">
            <!-- SEARCH AREA RADIUS CIRCLE -->
            <Circle :options="circleOptions" />
            <!-- OWN LOCATION MARKER -->
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
            <!-- SEARCH RESULTS CUSTOM MARKERS -->
            <div v-if="queryResults.length > 0">
                <div v-for="(data, index) in queryResults" :key="index">
                    <CustomMarker
                        :options="{ position: { lat: data.latitude, lng: data.longitude }, anchorPoint: 'BOTTOM_CENTER' }"
                        @click="infoWindow[index] = true">
                        <div style="text-align: center" class="hover:cursor-pointer">
                            <img :src="return_svg(data.category)" class="h-10 w-10" alt="">
                        </div>

                    </CustomMarker>
                    <div v-if="infoWindow[index]">
                        <InfoWindow :options="{ position: { lat: data.latitude, lng: data.longitude } }"
                            v-model="infoWindow[index]">
                            <template #default>
                                <div>
                                    <p>Username: {{ data.username }}</p>
                                    <p>Timestamp: {{ data.timestamp }}</p>
                                    <div v-for="(value, index) in Object.entries(data.form_data)" :key="index">
                                        <p>{{ value[0] }}: {{ value[1] ? value[1] : 'N/A' }}</p>
                                    </div>
                                </div>
                            </template>
                        </InfoWindow>
                    </div>
                </div>
            </div>
        </GoogleMap>
    </section>
</template>

<script>
import { checkLocationPermission } from '@/stores/geoLocation';
import SettingsModal from '../components/SettingsModal.vue'
import { infrastructureSVG, communicationsSVG, securitySVG } from '@/assets/svg';
export default {
    props: {
        user: {
            type: Object,
        },
        maps: {
            type: Object,
        },
        onLine: {
            type: Boolean,
        },
    },
    components: {
        SettingsModal,
    },
    data() {
        return {
            googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
            mapZoom: 2,
            mapCenter: { lat: 33, lng: 44 },
            userSelectedLat: '',
            userSelectedLong: '',
            userPosition: {},
            markerOptions: {},
            ownLocationRequested: false,
            selectedLocationMarkerOptions: {},
            selectedLocationCenter: { lat: 0, lng: 0 },
            selectedLocation: false,
            settingsModalVisibility: false,
            // payload contains settings from modal
            payload: '',
            queryResults: [],
            infrastructureSVG: infrastructureSVG,
            securitySVG: securitySVG,
            communicationsSVG: communicationsSVG,
            circleOptions: {
                center: { lat: 0, lng: 0 },
                radius: 6000,
                strokeColor: '#FF0000',
                strokeOpacity: 0.4,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.15,
            },
            infoWindow: {},
        }
    },
    methods: {
        clickIcon() {
            this.$toast.success("hello")
        },
        async getMyLocation() {
            try {
                const userPosition = await checkLocationPermission();
                this.userPosition = { lat: userPosition.coords.latitude, lng: userPosition.coords.longitude }
                this.markerOptions = { position: this.userPosition }
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
            this.circleOptions = {
                ...this.circleOptions,
                center: { lat: lat, lng: lng }
            };


            this.selectedLocationCenter = { lat: lat, lng: lng }
            this.selectedLocation = true
            this.selectedLocationMarkerOptions = { position: this.selectedLocationCenter }
            this.mapCenter = this.selectedLocationCenter
            this.userSelectedLat = lat
            this.userSelectedLong = lng
        },
        toggleSettingsModalVisibility() {
            this.settingsModalVisibility = !this.settingsModalVisibility
        },
        saveSettings(payload) {
            this.payload = payload

            this.circleOptions = {
                ...this.circleOptions,
                radius: payload.searchRadiusKm * 1000
            };

            if (payload.ownLocation) {
                this.getMyLocation()
            } else {
                this.ownLocationRequested = false
            }
            this.toggleSettingsModalVisibility()
        },
        return_svg(category) {
            switch (category) {
                case "security":
                    return securitySVG
                case "communications":
                    return communicationsSVG
                case "infrastructure":
                    return infrastructureSVG
                default:
                //
            }
        },
        async searchArea() {
            if (this.payload == '') {
                this.$toast.error("Please update map settings first")
            } else if (this.userSelectedLat == '' || this.userSelectedLong == '') {
                this.$toast.error("Please click on the map to set search location")
            } else if (this.payload.dateTo == '' || this.payload.dateFrom == '') {
                this.$toast.error("Please select a date range")
            }
            else {
                try {
                    this.queryResults = ''
                    this.payload["latitude"] = this.userSelectedLat
                    this.payload["longitude"] = this.userSelectedLong
                    const results = await this.maps.apiGetMapsSearchRequest(this.payload)
                    console.log(results)
                    this.queryResults = results
                    this.$toast.success('Results successful')
                    // initialise info windows to false
                    this.infoWindow = []
                    const len_query_results = this.queryResults.length
                    for (let i = 0; i < len_query_results; i++) {
                        this.infoWindow[i] = false
                    }
                } catch (error) {
                    console.log(error.status)
                    if (error.status === 409) {
                        // enter error codes
                    } else {
                        // Handle other errors
                        console.log("Other error:", error);
                    }
                }
            }
        },
    },
}
</script>

<style lang="scss" scoped></style>