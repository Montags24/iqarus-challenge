<template>
    <div class="bg-off-black text-white py-3 fixed 
             inset-x-0 
             top-0">
        <div class="flex justify-between text-center items-center max-container mx-auto px-8">
            <div v-if="!onLine">
                <svg fill="#f97316" width="34px" height="34px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
                    stroke="#f97316" stroke-width="0.00024000000000000003">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <g data-name="Layer 2">
                            <g data-name="wifi-off">
                                <rect width="24" height="24" opacity="0"></rect>
                                <circle cx="12" cy="19" r="1"></circle>
                                <path
                                    d="M12.44 11l-1.9-1.89-2.46-2.44-1.55-1.55-1.82-1.83a1 1 0 0 0-1.42 1.42l1.38 1.37 1.46 1.46 2.23 2.24 1.55 1.54 2.74 2.74 2.79 2.8 3.85 3.85a1 1 0 0 0 1.42 0 1 1 0 0 0 0-1.42z">
                                </path>
                                <path
                                    d="M21.72 7.93A13.93 13.93 0 0 0 12 4a14.1 14.1 0 0 0-4.44.73l1.62 1.62a11.89 11.89 0 0 1 11.16 3 1 1 0 0 0 .69.28 1 1 0 0 0 .72-.31 1 1 0 0 0-.03-1.39z">
                                </path>
                                <path
                                    d="M3.82 6.65a14.32 14.32 0 0 0-1.54 1.28 1 1 0 0 0 1.38 1.44 13.09 13.09 0 0 1 1.6-1.29z">
                                </path>
                                <path
                                    d="M17 13.14a1 1 0 0 0 .71.3 1 1 0 0 0 .72-1.69A9 9 0 0 0 12 9h-.16l2.35 2.35A7 7 0 0 1 17 13.14z">
                                </path>
                                <path d="M7.43 10.26a8.8 8.8 0 0 0-1.9 1.49A1 1 0 0 0 7 13.14a7.3 7.3 0 0 1 2-1.41z">
                                </path>
                                <path
                                    d="M8.53 15.4a1 1 0 1 0 1.39 1.44 3.06 3.06 0 0 1 3.84-.25l-2.52-2.52a5 5 0 0 0-2.71 1.33z">
                                </path>
                            </g>
                        </g>
                    </g>
                </svg>
            </div>
            <div v-else>
                <svg width="34px" height="34px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                    stroke="#343236">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <circle cx="1" cy="1" r="1" transform="matrix(1 0 0 -1 11 19)" fill="#f97316"></circle>
                        <path
                            d="M20.1915 10.2642C19.2864 8.97153 18.0881 7.9114 16.6947 7.17053C15.3014 6.42965 13.7524 6.02907 12.1746 6.00152C10.5967 5.97398 9.03471 6.32026 7.61632 7.01206C6.19793 7.70385 4.9634 8.72152 4.01367 9.98185M17.7341 12.985C17.1005 12.0801 16.2617 11.338 15.2863 10.8194C14.311 10.3008 13.2267 10.0203 12.1222 10.0011C11.0177 9.98179 9.9243 10.2242 8.93143 10.7084C7.93856 11.1927 7.07439 11.9051 6.40958 12.7873M14.4575 15.2793C14.1859 14.8915 13.8265 14.5734 13.4084 14.3512C12.9904 14.1289 12.5257 14.0087 12.0524 14.0005C11.579 13.9922 11.1104 14.0961 10.6849 14.3036C10.2594 14.5112 9.88904 14.8165 9.60412 15.1946"
                            stroke="#f97316" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    </g>
                </svg>
            </div>
            <h1 class="flex font-montserrat font-semibold text-xl text-orange-500">[ ResQHub ]
            </h1>
            <div class="flex pt-1 sm:items-center sm:hidden" @click="toggleMobileMenu">
                <button class="flex flex-col gap-1 pb-1 h-5 justify-center hover:cursor-pointer">
                    <span class="w-6 h-[2px] bg-orange-500 transition transform duration-200"
                        :class="{ 'rotate-45 translate-y-[3px]': mobileMenuOpen }"></span>
                    <span class="w-6 h-[2px] bg-orange-500 transition transform"
                        :class="{ 'hidden': mobileMenuOpen }"></span>
                    <span class="w-6 h-[2px] bg-orange-500 transition transform duration-200"
                        :class="{ 'rotate-[-45deg] translate-y-[-3px]': mobileMenuOpen }"></span>
                </button>
            </div>
            <div class="hidden sm:block">
                navlinks
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        onLine: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            mobileMenuOpen: false,
        }
    },
    methods: {
        toggleMobileMenu() {
            this.mobileMenuOpen = !this.mobileMenuOpen
        },
    },

}
</script>

<style lang="scss" scoped></style>