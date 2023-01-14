<template>
  <v-app-bar class="px-3" color="primary" absolute min-heigth="10vh">
    <v-avatar color="grey-darken-1" size="45"></v-avatar>

    <v-spacer></v-spacer>

    <v-tabs centered color="grey-darken-2">
      <v-tab v-for="link in links" v-bind:key="link">
        {{ link }}
      </v-tab>
    </v-tabs>
    <v-spacer></v-spacer>

    <v-avatar
      class="hidden-sm-and-down"
      color="grey-darken-1"
      size="32"
    ></v-avatar>
  </v-app-bar>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useAppStore } from "@/store/app";

var store = useAppStore();
var links = store.links;
</script>
