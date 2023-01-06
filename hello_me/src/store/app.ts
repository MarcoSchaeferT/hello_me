// Utilities
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    //
    links: [
      'Dashboard',
      'Messages',
      'Profile',
      'Updates',
    ],
  }),
})
