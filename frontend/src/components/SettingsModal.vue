<template>
    <div v-if="visible">
        <!-- Modal -->
        <div class="fixed inset-0 flex items-center justify-center z-20">
            <div
                class="bg-off-black text-white rounded-lg p-6 w-80 sm:w-96 max-w-full shadow-lg transform transition-all duration-300">
                <!-- Modal Header -->
                <div class="flex justify-between items-center border-b-2 pb-4">
                    <h2 class="text-2xl font-semibold">Map settings</h2>
                    <button @click="toggleModal" class="text-white focus:outline-none">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="feather feather-x">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>

                <!-- Modal Content -->
                <div class="mt-6 space-y-4 flex flex-col">
                    <div class="flex items-center">
                        <input v-model="ownLocation" id="checkbox-own-location" type="checkbox"
                            name="checkbox-own-location" class="w-4 h-4 rounded accent-orange-500">
                        <label for="checkbox-own-location"
                            class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Show own location
                            on map</label>
                    </div>
                    <div class="flex flex-col">
                        <h1>Categories</h1>
                        <div class="flex flex-col flex-wrap max-h-20">
                            <div v-for="(category, index) in categories" :key="index" class="flex">
                                <input v-model="selectedCategories[category]" :id="category" type="checkbox"
                                    :name="category" class="w-4 h-4 rounded accent-orange-500">
                                <label :for="category"
                                    class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{
                                        category }}</label>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col">
                        <h1>Set timeframe</h1>
                        <div class="flex space-x-4 items-center text-sm">
                            <div class="max-w-sm text-black">
                                <input type="date" id="from-date" name="from-date" class="rounded-sm  text-center"
                                    v-model="dateFrom">
                            </div>
                            <span>to</span>
                            <div class="max-w-sm text-black text-sm">
                                <input type="date" id="to-date" name="to-date" class="rounded-sm text-center"
                                    v-model="dateTo">
                            </div>
                        </div>
                    </div>
                    <div>
                        <label for="default-range" class="">Search Radius</label> <span>- {{ searchRadiusKm }}km</span>
                        <input id="default-range" type="range" min="0" max="12" value="6" v-model="searchRadiusKm"
                            class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700">
                    </div>
                    <div class="flex justify-center">
                        <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-1 px-6 rounded"
                            @click="saveSettings">Save
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    emits: ['toggleModalVisibility', 'saveSettings'],
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        user: {
            type: Object
        },
    },
    data() {
        return {
            categories:
                ["Infrastructure", "Medical", "Security", "Logistics", "Environment", "Health", "Communications"],
            ownLocation: false,
            selectedCategories: {},
            dateFrom: null,
            dateTo: null,
            searchRadiusKm: 6,
        };
    },
    created() {
        // Initialize dateFrom to a week ago and dateTo to today's date
        const today = new Date();
        const weekAgo = new Date(today);
        weekAgo.setDate(today.getDate() - 7);

        this.dateFrom = this.formatDate(weekAgo);
        this.dateTo = this.formatDate(today);
    },
    methods: {
        toggleModal() {
            this.$emit('toggleModalVisibility')
        },
        saveSettings() {
            const data = {}
            data["ownLocation"] = this.ownLocation
            data["categories"] = this.selectedCategories
            data["dateFrom"] = this.dateFrom
            data["dateTo"] = this.dateTo
            data["searchRadiusKm"] = parseInt(this.searchRadiusKm)
            this.$emit('saveSettings', data)
        },
        formatDate(date) {
            const year = date.getFullYear();
            let month = date.getMonth() + 1;
            let day = date.getDate();

            // Ensure month and day are two digits
            month = month < 10 ? '0' + month : month;
            day = day < 10 ? '0' + day : day;

            return `${year}-${month}-${day}`;
        }
    },
};
</script>

<style>
/* Add your styles here */
</style>
