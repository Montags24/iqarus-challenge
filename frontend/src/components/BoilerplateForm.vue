<template>
    <div class="flex flex-wrap gap-x-6">
        <section v-for="(section, index) in formObj.sections" :key="index" class="pb-4 px-4 w-full">
            <div class="rounded-lg border border-gray-700 bg-[#161b22] flex flex-col text-white px-4 py-3">
                <label class="block uppercase text-white text-md font-bold">
                    {{ section.title }}
                </label>
                <div v-for="(entry, index) in section.formEntries" :key="index" class="">
                    <label class="block uppercase text-white text-sm mb-2" :for="entry.label">
                        {{ entry.title }}
                    </label>
                    <div class="relative mb-3">
                        <select v-if="!entry.textarea"
                            class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline"
                            :id="entry.label" v-model="payload[entry.payloadLabel]">
                            <option v-for="(option, optionIndex) in entry.options" :key="optionIndex">{{ option }}
                            </option>
                        </select>
                        <textarea v-else
                            class="shadow bg-black appearance-none border border-gray-700 rounded w-full py-1 px-3 leading-tight focus:outline-none focus:shadow-outline"
                            :id="entry.label" v-model="payload[entry.payloadLabel]" rows="4" maxlength="250"></textarea>
                        <div v-if="!entry.textarea"
                            class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-white">
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                            </svg>
                        </div>
                        <span v-if="entry.textarea" class="text-sm">{{ payload[entry.payloadLabel] ?
                            payload[entry.payloadLabel].length
                            : 0
                            }}/250</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <section class="pb-10 flex justify-center">
        <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
            @click="submitForm">Submit </button>
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
            payload: {}
        };
    },
    methods: {
        submitForm() {
            this.payload.formName = this.formObj.category
            this.$emit('submitForm', this.payload)
        }
    },
    watch: {
        formObj(newCategory, oldCategory) {
            if (newCategory != oldCategory) {
                this.payload = {}
            }
        }
    }
};
</script>

<style>
/* Add custom styles here if needed */
</style>
