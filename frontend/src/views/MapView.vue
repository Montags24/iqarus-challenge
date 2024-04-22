<script setup>
import { GoogleMap, CustomMarker } from 'vue3-google-map'

</script>

<template>
    <GoogleMap :api-key="googleMapsApiKey" style="width: 100%; height: 90vh" :center="userPosition" :zoom="10">
        <CustomMarker :options="markerOptions">
            <div style="text-align: center" class="hover:cursor-pointer">
                <v-icon name="fa-map-marker-alt" scale="2" fill="red" />
            </div>
        </CustomMarker>
    </GoogleMap>
</template>

<script>
import { checkLocationPermission } from '@/stores/geoLocation';
export default {
    async created() {
        try {
            const userPosition = await checkLocationPermission();
            this.latitude = userPosition.coords.latitude
            this.longitude = userPosition.coords.longitude
            this.userPosition = { lat: this.latitude, lng: this.longitude }
            this.markerOptions = { position: this.userPosition, label: 'U', title: 'Current Location' }
        } catch (error) {
            console.error('Error getting location:', error);
            // Handle error
        }
    },
    data() {
        return {
            googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
            latitude: '',
            longitude: '',
            userPosition: {},
            markerOptions: {}
        }
    },


}
</script>

<style lang="scss" scoped></style>