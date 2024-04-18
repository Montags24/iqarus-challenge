<template>
    <div v-if="!onLine" class="mt-12 px-3 py-3 block uppercase text-white text-md font-bold bg-slate-400 text-center">
        No accesss in offline mode
    </div>
    <section class="mt-12 mb-16 pt-3 bg-black">

        <RegisterUser v-if="!user.logged_in" @submitRegistration="submitRegistration"></RegisterUser>
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
    methods: {
        async submitRegistration(payload) {
            try {
                const user = await this.user.api_register(payload)
                console.log(user)
            } catch (error) {
                console.log(error)
            }

        }
    },


}
</script>

<style lang="scss" scoped></style>