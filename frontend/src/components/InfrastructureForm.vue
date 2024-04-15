<template>
    <!-- START ROADS -->
    <section class="pb-4">
        <label class="px-3 block uppercase text-white text-md font-bold">
            Roads
        </label>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="road-condition">
                Condition
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="road-condition" v-model="payload.roadCondition">
                    <option>Clear</option>
                    <option>Damaged</option>
                    <option>Blocked</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="road-damage">
                Type of damage
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="road-damage" v-model="payload.roadDamage">
                    <option>Flooded</option>
                    <option>Debris</option>
                    <option>Collapsed</option>
                    <option>None</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="road-access">
                Accessibility
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="road-access" v-model="payload.roadAccess">
                    <option>Passable</option>
                    <option>Impassable</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
    </section>
    <!-- END ROADS -->
    <!-- START BUILDINGS -->
    <section class="pb-4">
        <label class="px-3 block uppercase text-white text-md font-bold">
            Buildings
        </label>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="building-integrity">
                Structural Integrity
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="building-integrity" v-model="payload.buildingIntegrity">
                    <option>Intact</option>
                    <option>Damaged</option>
                    <option>Collapsed</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="building-type">
                Type
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="building-type" v-model="payload.buildingType">
                    <option>Residential</option>
                    <option>Commercial</option>
                    <option>Government</option>
                    <option>None</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="building-damage">
                Damage Assessment
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="building-damage" v-model="payload.buildingDamage">
                    <option>Minor</option>
                    <option>Moderate</option>
                    <option>Severe</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
    </section>
    <!-- END BUILDINGS -->
    <!-- START UTILITIES -->
    <section class="pb-4">
        <label class="px-3 block uppercase text-white text-md font-bold">
            Utilities
        </label>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="utility-power">
                Power Supply
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="utility-power" v-model="payload.utilityPower">
                    <option>Available</option>
                    <option>Outages</option>
                    <option>Generators</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="utility-water">
                Water Supply
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="utility-water" v-model="payload.utilityWater">
                    <option>Functional</option>
                    <option>Contaminated</option>
                    <option>Shortages</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="utility-comms">
                Telecommunications
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="utility-comms" v-model="payload.utilityComms">
                    <option>Functional</option>
                    <option>Cell Service Only</option>
                    <option>Internet Connectivity</option>
                    <option>Limited</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
    </section>
    <!-- END UTILITIES -->
    <section class="pb-10 flex justify-center">
        <button class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
            @click="submitForm">Submit <v-icon name="io-send" /></button>
    </section>
</template>

<script>
export default {
    emits: ['submitForm'],
    data() {
        return {
            payload: {
                formName: 'infrastructure',
                roadCondition: '',
                roadDamage: '',
                roadAccess: '',
                buildingType: '',
                buildingDamage: '',
                buildingIntegrity: '',
                utilityWater: '',
                utilityPower: '',
                utilityComms: '',
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
