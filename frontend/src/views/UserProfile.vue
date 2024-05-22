<template>
    <!-- START USER LOGIN AND REGISTER-->
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
    <!-- DISPLAY USER DETAILS ON LOGIN -->
    <section v-if="user.loggedIn && onLine" class="mt-12 pt-6 pb-4">
        <div class="max-w-xs mx-auto rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
            <div class="flex justify-between mb-2">
                <div class="flex">
                    <label class="block uppercase text-white text-sm" for="username">Username:</label>
                    <p class="px-4 text-sm">{{ user.username }}</p>
                </div>
                <svg v-if="!editingName" class="hover:cursor-pointer size-5" @click="editName" viewBox="0 0 24 24"
                    fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#000000">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <path
                            d="M21.2799 6.40005L11.7399 15.94C10.7899 16.89 7.96987 17.33 7.33987 16.7C6.70987 16.07 7.13987 13.25 8.08987 12.3L17.6399 2.75002C17.8754 2.49308 18.1605 2.28654 18.4781 2.14284C18.7956 1.99914 19.139 1.92124 19.4875 1.9139C19.8359 1.90657 20.1823 1.96991 20.5056 2.10012C20.8289 2.23033 21.1225 2.42473 21.3686 2.67153C21.6147 2.91833 21.8083 3.21243 21.9376 3.53609C22.0669 3.85976 22.1294 4.20626 22.1211 4.55471C22.1128 4.90316 22.0339 5.24635 21.8894 5.5635C21.7448 5.88065 21.5375 6.16524 21.2799 6.40005V6.40005Z"
                            stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path
                            d="M11 4H6C4.93913 4 3.92178 4.42142 3.17163 5.17157C2.42149 5.92172 2 6.93913 2 8V18C2 19.0609 2.42149 20.0783 3.17163 20.8284C3.92178 21.5786 4.93913 22 6 22H17C19.21 22 20 20.2 20 18V13"
                            stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </g>
                </svg>
                <svg v-else class="hover:cursor-pointer size-5 fill-current text-white" @click="saveName"
                    viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#000000">
                    <g id="SVGRepo_bgCarrier" stroke-width="1.5"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M18.1716 1C18.702 1 19.2107 1.21071 19.5858 1.58579L22.4142 4.41421C22.7893 4.78929 23 5.29799 23 5.82843V20C23 21.6569 21.6569 23 20 23H4C2.34315 23 1 21.6569 1 20V4C1 2.34315 2.34315 1 4 1H18.1716ZM4 3C3.44772 3 3 3.44772 3 4V20C3 20.5523 3.44772 21 4 21L5 21L5 15C5 13.3431 6.34315 12 8 12L16 12C17.6569 12 19 13.3431 19 15V21H20C20.5523 21 21 20.5523 21 20V6.82843C21 6.29799 20.7893 5.78929 20.4142 5.41421L18.5858 3.58579C18.2107 3.21071 17.702 3 17.1716 3H17V5C17 6.65685 15.6569 8 14 8H10C8.34315 8 7 6.65685 7 5V3H4ZM17 21V15C17 14.4477 16.5523 14 16 14L8 14C7.44772 14 7 14.4477 7 15L7 21L17 21ZM9 3H15V5C15 5.55228 14.5523 6 14 6H10C9.44772 6 9 5.55228 9 5V3Z">
                        </path>
                    </g>
                </svg>
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
    <!-- DISPLAY USER PREVIOUS UPDATES -->
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
        maps: {
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