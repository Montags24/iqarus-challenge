<template>
    <section v-for="(section, index) in formObj" :key="index" class="pb-4">
        <label class="px-3 block uppercase text-white text-md font-bold">
            {{ section.title }}
        </label>
        <div v-for="(entry, index) in section.formEntries" :key="index" class="w-full px-4 mb-3">
            <label class="block uppercase text-white text-sm mb-2" :for="entry.label">
                {{ entry.title }}
            </label>
            <div class="relative">
                <select v-if="!entry.textarea"
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    :id="entry.label" v-model="payload[entry.payloadLabel]">
                    <option v-for="(option, optionIndex) in entry.options" :key="optionIndex">{{ option }}</option>
                </select>
                <textarea v-else
                    class="block w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500 resize-none"
                    :id="entry.label" v-model="payload[entry.payloadLabel]" rows="4"></textarea>
                <div v-if="!entry.textarea"
                    class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
    </section>
    <section class="pb-10 flex justify-center">
        <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
            @click="submitForm">Submit <v-icon name="io-send" /></button>
    </section>
</template>

<script>
export default {
    emits: ['submitForm'],
    props: {
        formObj: {
            type: Object,
        },
    },
    data() {
        return {
            payload: {
                formName: this.formObj.formName,
            }
        };
    },
    methods: {
        submitForm() {
            this.$emit('submitForm', this.payload)
        }
    }
};
</script>

<style>
/* Add custom styles here if needed */
</style>
