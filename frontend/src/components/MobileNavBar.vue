<template>
    <nav class="bg-off-black text-white text-center fixed inset-x-0 bottom-0 pb-3 pt-2 px-6">
        <div class="max-w-lg mx-auto">
            <div class="flex justify-between font-montserrat text-xs">
                <RouterLink to="/">
                    <div class="flex flex-col items-center pb-2" :class="{ 'text-orange-500': $route.name == 'home' }">
                        <!-- <v-icon name="io-send" /> -->
                        <svg class="h-6 w-6 fill-current" viewBox="-5.2 -5.2 62.40 62.40"
                            xmlns="http://www.w3.org/2000/svg" stroke="#000000">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                            <g id="SVGRepo_iconCarrier">
                                <rect fill="none" height="4.8" rx="1.6" width="27.2" x="12.4" y="26"></rect>
                                <rect fill="none" height="4.8" rx="1.6" width="24" x="12.4" y="35.6"></rect>
                                <g>
                                    <path
                                        d="m36.4 14.8h8.48a1.09 1.09 0 0 0 1.12-1.12 1 1 0 0 0 -.32-.8l-10.56-10.56a1 1 0 0 0 -.8-.32 1.09 1.09 0 0 0 -1.12 1.12v8.48a3.21 3.21 0 0 0 3.2 3.2z">
                                    </path>
                                    <path
                                        d="m44.4 19.6h-11.2a4.81 4.81 0 0 1 -4.8-4.8v-11.2a1.6 1.6 0 0 0 -1.6-1.6h-16a4.81 4.81 0 0 0 -4.8 4.8v38.4a4.81 4.81 0 0 0 4.8 4.8h30.4a4.81 4.81 0 0 0 4.8-4.8v-24a1.6 1.6 0 0 0 -1.6-1.6zm-32-1.6a1.62 1.62 0 0 1 1.6-1.55h6.55a1.56 1.56 0 0 1 1.57 1.55v1.59a1.63 1.63 0 0 1 -1.59 1.58h-6.53a1.55 1.55 0 0 1 -1.58-1.58zm24 20.77a1.6 1.6 0 0 1 -1.6 1.6h-20.8a1.6 1.6 0 0 1 -1.6-1.6v-1.57a1.6 1.6 0 0 1 1.6-1.6h20.8a1.6 1.6 0 0 1 1.6 1.6zm3.2-9.6a1.6 1.6 0 0 1 -1.6 1.63h-24a1.6 1.6 0 0 1 -1.6-1.6v-1.6a1.6 1.6 0 0 1 1.6-1.6h24a1.6 1.6 0 0 1 1.6 1.6z">
                                    </path>
                                </g>
                            </g>
                        </svg>
                        <p class="pt-1">Update</p>
                    </div>
                </RouterLink>
                <RouterLink to="/map">
                    <div class="flex flex-col items-center pb-2" :class="{ 'text-orange-500': $route.name == 'map' }">
                        <svg class="h-5 w-5 fill-current" version="1.0" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 64 64"
                            enable-background="new 0 0 64 64" xml:space="preserve">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                            <g id="SVGRepo_iconCarrier">
                                <path
                                    d="M32,0C18.746,0,8,10.746,8,24c0,5.219,1.711,10.008,4.555,13.93c0.051,0.094,0.059,0.199,0.117,0.289l16,24 C29.414,63.332,30.664,64,32,64s2.586-0.668,3.328-1.781l16-24c0.059-0.09,0.066-0.195,0.117-0.289C54.289,34.008,56,29.219,56,24 C56,10.746,45.254,0,32,0z M32,32c-4.418,0-8-3.582-8-8s3.582-8,8-8s8,3.582,8,8S36.418,32,32,32z">
                                </path>
                            </g>
                        </svg>
                        <p class="pt-1">Maps</p>
                    </div>
                </RouterLink>
                <RouterLink to="/profile">
                    <div class="flex flex-col items-center pb-2"
                        :class="{ 'text-orange-500': $route.name == 'profile' }">
                        <svg class="h-5 w-5 fill-current" viewBox="0 0 20 20" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                            <g id="SVGRepo_iconCarrier">
                                <title>profile_round [#1342]</title>
                                <desc>Created with Sketch.</desc>
                                <defs> </defs>
                                <g id="Page-1" stroke="none" stroke-width="1">
                                    <g id="Dribbble-Light-Preview" transform="translate(-140.000000, -2159.000000)">
                                        <g id="icons" transform="translate(56.000000, 160.000000)">
                                            <path
                                                d="M100.562548,2016.99998 L87.4381713,2016.99998 C86.7317804,2016.99998 86.2101535,2016.30298 86.4765813,2015.66198 C87.7127655,2012.69798 90.6169306,2010.99998 93.9998492,2010.99998 C97.3837885,2010.99998 100.287954,2012.69798 101.524138,2015.66198 C101.790566,2016.30298 101.268939,2016.99998 100.562548,2016.99998 M89.9166645,2004.99998 C89.9166645,2002.79398 91.7489936,2000.99998 93.9998492,2000.99998 C96.2517256,2000.99998 98.0830339,2002.79398 98.0830339,2004.99998 C98.0830339,2007.20598 96.2517256,2008.99998 93.9998492,2008.99998 C91.7489936,2008.99998 89.9166645,2007.20598 89.9166645,2004.99998 M103.955674,2016.63598 C103.213556,2013.27698 100.892265,2010.79798 97.837022,2009.67298 C99.4560048,2008.39598 100.400241,2006.33098 100.053171,2004.06998 C99.6509769,2001.44698 97.4235996,1999.34798 94.7348224,1999.04198 C91.0232075,1998.61898 87.8750721,2001.44898 87.8750721,2004.99998 C87.8750721,2006.88998 88.7692896,2008.57398 90.1636971,2009.67298 C87.1074334,2010.79798 84.7871636,2013.27698 84.044024,2016.63598 C83.7745338,2017.85698 84.7789973,2018.99998 86.0539717,2018.99998 L101.945727,2018.99998 C103.221722,2018.99998 104.226185,2017.85698 103.955674,2016.63598"
                                                id="profile_round-[#1342]"> </path>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </svg>
                        <p class="pt-1">Profile</p>
                    </div>
                </RouterLink>
            </div>
        </div>
    </nav>
</template>


<script>
import { formSVG } from '../assets/svg/index'
export default {
    data() {
        return {
            formSVG: formSVG
        }
    },

}
</script>

<style lang="scss" scoped></style>