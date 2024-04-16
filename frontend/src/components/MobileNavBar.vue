<template>
    <nav class="bg-off-black text-white text-center fixed inset-x-0 bottom-0 pb-3 pt-2 px-6">
        <div class="max-w-lg mx-auto">
            <div class="flex justify-between font-montserrat text-xs">
                <RouterLink to="/">
                    <div class="flex flex-col items-center pb-2" :class="{ 'text-orange-500': $route.name == 'home' }">
                        <v-icon name="io-send" />
                        <p class="pt-1">Update</p>
                    </div>
                </RouterLink>
                <RouterLink to="/map">
                    <div class="flex flex-col items-center pb-2" :class="{ 'text-orange-500': $route.name == 'map' }">
                        <v-icon name="fa-map-marker-alt" />
                        <p class="pt-1">Maps</p>
                    </div>
                </RouterLink>
                <RouterLink to="/profile">
                    <div class="flex flex-col items-center pb-2"
                        :class="{ 'text-orange-500': $route.name == 'profile' }">
                        <v-icon name="fa-user-alt" />
                        <p class="pt-1">Profile</p>
                    </div>
                </RouterLink>
            </div>
        </div>
    </nav>
</template>


<script>
export default {
    data() {
        return {
        }
    },

}
</script>

<style lang="scss" scoped></style>