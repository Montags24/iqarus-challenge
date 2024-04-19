<template>
    <div class="bg-off-black text-white py-3 fixed 
             inset-x-0 
             top-0">
        <div class="flex justify-between text-center items-center max-container mx-auto px-8">
            <div v-if="!onLine">
                <v-icon name="hi-solid-status-offline" class="text-orange-500" scale="1.5" />
            </div>
            <div v-else>
                <v-icon name="hi-solid-status-online" class="text-orange-500" scale="1.5" />
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