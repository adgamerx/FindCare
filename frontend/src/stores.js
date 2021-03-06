import { browser } from '$app/env'
import { writable } from 'svelte/store'

const storedUser = JSON.parse((browser && localStorage.getItem('user')) || null)

export const user = writable(browser && storedUser)

user.subscribe((profile_image) => browser && (localStorage.user = JSON.stringify(profile_image)))

export const adminQueryUserEmail = writable(null)
export const adminQueryDoctorName = writable(null)
export const doctorDashBoardHeader = writable(null)
