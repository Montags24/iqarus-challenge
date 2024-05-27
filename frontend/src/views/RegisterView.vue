<template>
    <div v-if="!onLine" class="mt-12 px-3 py-3 block uppercase text-white text-md font-bold bg-slate-400 text-center">
        No accesss in offline mode
    </div>
    <section class="mt-12 mb-16 pt-3 bg-black">
        <RegisterUser v-if="!user.logged_in || !onLine" @submitRegistration="submitRegistration"
            :usernameInUse="usernameInUse">
        </RegisterUser>
    </section>
</template>

<script>
import RegisterUser from '@/components/RegisterUser.vue';
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
        RegisterUser,
    },
    data() {
        return {
            usernameInUse: false
        }
    },
    methods: {
        async submitRegistration(payload) {
            try {
                this.usernameInUse = false
                await this.user.apiRegister(payload)
                this.$toast.success('Registration successful. Please login')
                this.$route.push('/login')
            } catch (error) {
                console.log(error.status)
                if (error.status === 409) {
                    this.usernameInUse = true
                } else {
                    // Handle other errors
                    console.log("Other error:", error);
                }
            }
        }
    },
}
</script>

<style lang="scss" scoped></style>