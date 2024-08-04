<script>
import TheNav from '@/components/TheNav.vue';
import TheProfile from '@/components/TheProfile.vue';
export default {
  data() {
    return {

    }
    
  },
  components: { TheNav, TheProfile }
}
</script>

<template>
  <main>
    <TheNav></TheNav>
    <TheProfile></TheProfile>
  </main>
</template>