<template>
    <div v-if="visible">
        <!-- Modal -->
        <div class="fixed inset-0 flex items-center justify-center z-20">
            <div
                class="bg-white rounded-lg p-6 w-80 sm:w-96 max-w-full shadow-lg transform transition-all duration-300">
                <!-- Modal Header -->
                <div class="flex justify-between items-center border-b-2 border-gray-200 pb-4">
                    <h2 class="text-2xl font-semibold">Rewards</h2>
                    <button @click="toggleModal" class="text-gray-500 hover:text-gray-700 focus:outline-none">
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
                    <h1>Modal content</h1>
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
