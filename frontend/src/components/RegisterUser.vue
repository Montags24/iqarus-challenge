<template>
    <section class="pt-3">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <label class="block uppercase text-white font-semibold mb-2">
                Register
            </label>
            <div class="w-full mb-3">
                <label class="block uppercase text-white text-sm mb-2" for="name">
                    Name
                </label>
                <input
                    class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                    id="name" type="text" v-model="name">
                <label class="block uppercase text-white text-sm mb-2" for="username">
                    Username
                </label>
                <input
                    class="sshadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                    :class="{ 'mb-3': !usernameInUse }" id="username" type="text" v-model="username">
                <span v-if="usernameInUse" class="text-red-500 mb-3">[Username already taken]</span>
                <label class="block uppercase text-white text-sm mb-2" for="password">
                    Password
                </label>
                <input
                    class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                    id="password" type="password" v-model="password">
                <label class="block uppercase text-white text-sm mb-2" for="password2">
                    Re-enter Password
                </label>
                <input
                    class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password2" type="password" v-model="password2">
                <span v-if="checkPassword()" class="text-red-500 text-sm">[Passwords must match]</span>
            </div>

            <button class="bg-orange-500 text-white font-bold py-1 px-4 rounded"
                :class="!checkDisabledButton() ? 'hover:bg-orange-600 hover:cursor-pointer' : 'opacity-50'"
                @click="submitForm" :disabled="checkDisabledButton()">Sign Up
            </button>
        </div>

    </section>
</template>

<script>
export default {
    emits: ['submitRegistration'],
    props: {
        usernameInUse: {
            type: Boolean,
        },
    },
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
            return this.password2 && this.password != this.password2
        }
    },

}
</script>

<style lang="scss" scoped></style>