<template>
    <!-- START ROADS -->
    <section class="pb-4">
        <label class="px-3 block uppercase text-white text-md font-bold">
            Security risks
        </label>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-armed-groups">
                Presence of armed groups
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="risk-armed-groups" v-model="payload.riskArmedGroups">
                    <option>Present</option>
                    <option>Absent</option>
                    <option>Unknown</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-report">
                Reports of violence or unrest
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="risk-report" v-model="payload.riskViolence">
                    <option>Confirmed</option>
                    <option>Suspected</option>
                    <option>Not reported</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-local-enforcement">
                Law enforcement or military presence
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="risk-local-enforcement" v-model="payload.riskLocalEnforcement">
                    <option>Present</option>
                    <option>Absent</option>
                    <option>Unknown</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-incidents">
                Reported Incidents
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="risk-incidents" v-model="payload.riskIncidents">
                    <option>Looting</option>
                    <option>Theft</option>
                    <option>Vandalism</option>
                    <option>Violence</option>
                    <option>No reported incidents</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-incidents-to-relief">
                Security incidents affecting relief efforts
            </label>
            <div class="relative">
                <select
                    class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="risk-incidents-to-relief" v-model="payload.riskIncidentsToRelief">
                    <option>High risk</option>
                    <option>Moderate risk</option>
                    <option>Low risk</option>
                    <option>Unknown</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="w-full px-4 mb-3 md:mb-0">
            <label class="block uppercase text-white text-sm mb-2" for="risk-incidents-to-relief">
                Additional Comments
            </label>
            <div class="relative">
                <textarea
                    class="block w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500 resize-none"
                    id="risk-incidents-to-relief" v-model="payload.riskComments" rows="4"></textarea>
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
                formName: 'security',
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
