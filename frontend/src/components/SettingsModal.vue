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
                <div class="mt-6 space-y-4">
                    <h1>Show own location</h1>
                    <h1>Select categories to show</h1>
                    <h1>Set timeframe</h1>
                    <h1>Set search radius</h1>
                    <h1>Sumbit Button</h1>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    emits: ['toggleModalVisibility'],
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
        };
    },
    methods: {
        toggleModal() {
            this.$emit('toggleModalVisibility')
        },
    },
};
</script>

<style>
/* Add your styles here */
</style>
