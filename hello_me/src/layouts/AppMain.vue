<template>
  <v-main class="bg-grey-lighten-3">
    <v-card>
      <v-row>
        <v-col cols="5" offset="10px">
          <v-card max-width="434" min-width="434" class="pa-4">
            <helloMe />
          </v-card>
        </v-col>

        <v-col cols="4">
          <v-card class="pa-4">
            <v-sheet
              min-height="92vh"
              rounded="lg"
              color="secondary_v"
              class="pd-3"
            >
              <!--  -->
            </v-sheet>
          </v-card>
        </v-col>

        <v-col cols="3">
          <v-card class="pa-4">
            <v-sheet
              rounded="lg"
              min-height="268"
              color="secondary_v"
              class="pa-4"
            >
              <!--  -->
            </v-sheet>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-main>
</template>

<script setup lang="ts">
import helloMe from "../components/HelloMe.vue";
</script>
