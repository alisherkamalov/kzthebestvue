<script>
import TheNav from '@/components/TheNav.vue';
import TheAuth from '@/components/TheAuthorization.vue';
export default {
  data() {
    return {

    }
    
  },
  components: { TheNav, TheAuth }
}
</script>

<template>
  <main>
    <TheNav></TheNav>
    <TheAuth></TheAuth>
  </main>
</template>