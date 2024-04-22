<template>
    <section v-if="!user.loggedIn && onLine" class="mt-12 pt-6 ">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <label class="block uppercase text-white text-sm mb-2" for="username">Username</label>
            <input
                class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline mb-3"
                id="username" type="text" v-model="username">
            <label class="block uppercase text-white text-sm mb-2" for="password">Password</label>
            <input
                class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline"
                :class="{ 'mb-3': !incorrectCredentials }" id="password" type="password" v-model="password">
            <span v-if="incorrectCredentials" class="text-red-500 text-sm mb-3">[{{ errorMessage }}]</span>
            <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-1 px-4 rounded" @click="login">Sign
                in</button>
        </div>
        <div
            class=" mt-5 max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <label class="block uppercase text-white text-sm mb-2" for="username">Not registered?</label>
            <RouterLink to="/register">
                <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-1 px-4 rounded w-full">Create
                    an account</button>
            </RouterLink>
        </div>
    </section>
    <section v-if="user.loggedIn && onLine" class="mt-12 pt-6 pb-4">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <div class="flex justify-between mb-2">
                <div class="flex">
                    <label class="block uppercase text-white text-sm" for="username">Username:</label>
                    <p class="px-4 text-sm">{{ user.username }}</p>
                </div>
                <v-icon v-if="!editingName" name="fa-edit" class="hover:cursor-pointer" @click="editName" />
                <v-icon v-else name="fa-save" class="hover:cursor-pointer" @click="saveName" />
            </div>
            <div class="flex mb-2">
                <label class="block uppercase text-white text-sm" for="password">Name:</label>
                <p v-if="!editingName" class="px-4 text-sm">{{ user.name }}</p>
                <div v-else class="px-4">
                    <input
                        class="bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline"
                        v-model="editedName">
                </div>
            </div>
        </div>
    </section>
    <section v-if="user.loggedIn && onLine">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            Previous updates
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
            username: '',
            password: '',
            incorrectCredentials: false,
            errorMessage: '',
            editingName: false,
            editedName: this.user.name
        }
    },
    methods: {
        async login() {
            try {
                await this.user.apiLogin(this.username, this.password)
                this.incorrectCredentials = false
                this.$toast.success('Login successful')
                this.$router.push('/')
            } catch (error) {
                console.log(error.status)
                if (error.status === 401) {
                    this.incorrectCredentials = true
                    this.errorMessage = "Incorrect username or password"
                } else if (error.status === 404) {
                    this.incorrectCredentials = true
                    this.errorMessage = "User not found"
                } else {
                    // Handle other errors
                    console.log("Other error:", error);
                }
            }
        },
        editName() {
            this.editingName = true
        },
        async saveName() {
            if (this.editedName != this.user.name) {
                try {
                    await this.user.apiEditUser(this.editedName)
                    this.$toast.success('Profile updated')
                } catch (error) {
                    console.log(error.status)
                    if (error.status === 401) {
                        this.$toast.error('Error updating profile')
                    } else {
                        // Handle other errors
                        console.log("Other error:", error);
                    }
                }
            }
            this.editingName = false
        }
    },
}
</script>

<style lang="scss" scoped></style>