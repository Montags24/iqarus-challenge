<template>
    <section class="pb-4 max-w-lg mx-auto">
        <label class="px-3 block uppercase text-white text-md font-bold">
            Register
        </label>
        <div class="w-full px-4 mb-3">
            <label class="block uppercase text-white text-sm mb-2" for="name">
                Name
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="name" type="text" v-model="name">
            <label class="block uppercase text-white text-sm mb-2" for="username">
                Username
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="username" type="text" v-model="username">
            <label class="block uppercase text-white text-sm mb-2" for="password">
                Password
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="password" type="password" v-model="password">
            <label class="block uppercase text-white text-sm mb-2" for="password2">
                Re-enter Password
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="password2" type="password" v-model="password2">
            <span v-if="checkPassword()" class="text-red-500">[Passwords must match]</span>
        </div>

    </section>
    <section class="pb-10 flex justify-center">
        <button class="bg-orange-500 text-white font-bold py-2 px-4 rounded"
            :class="!checkDisabledButton() ? 'hover:bg-orange-600 hover:cursor-pointer' : 'opacity-50'"
            @click="submitForm" :disabled="checkDisabledButton()">Submit
            <v-icon name="io-send" /></button>
    </section>
</template>

<script>
export default {
    emits: ['submitRegistration'],
    data() {
        return {
            name: '',
            username: '',
            password: '',
            password2: '',
        }
    },
    methods: {
        submitForm() {
            const payload = {
                name: this.name,
                username: this.username,
                password: this.password
            }
            console.log("submit form")
            this.$emit('submitRegistration', payload)
        },
        checkDisabledButton() {
            return !this.name || !this.username || !this.password || !this.password2 || this.checkPassword()
        },
        checkPassword() {
            return !this.password2 || this.password != this.password2
        }
    },

}
</script>

<style lang="scss" scoped></style>