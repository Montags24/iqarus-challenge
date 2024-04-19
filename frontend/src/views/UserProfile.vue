<template>
    <section v-if="!user.logged_in" class="mt-12 pt-6 ">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <label class="block uppercase text-white text-sm mb-2" for="username">Username</label>
            <input
                class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="username" type="text" v-model="username">
            <label class="block uppercase text-white text-sm mb-2" for="password">Password</label>
            <input
                class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="password" type="password" v-model="password">
            <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-1 px-4 rounded"
                @click="submitForm">Sign in</button>
        </div>
        <div
            class=" mt-5 max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <label class="block uppercase text-white text-sm mb-2" for="username">Not registered?</label>
            <RouterLink to="/register">
                <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-1 px-4 rounded w-full"
                    @click="submitForm">Create an account</button>
            </RouterLink>
        </div>
    </section>
</template>

<script>
export default {
    props: {
        user: {
            type: Object,
        },
        onLine: {
            type: Boolean
        }
    },
    components: {
    },
    data() {
        return {
        }
    },
    methods: {

    },


}
</script>

<style lang="scss" scoped></style>