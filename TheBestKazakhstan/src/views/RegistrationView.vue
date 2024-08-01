<script>
import TheNav from '@/components/TheNav.vue';
import TheReg from '@/components/TheRegistration.vue';

export default {
    components: { TheNav,TheReg },
    data() {
        
        return {}
    }
}
</script>

<template>
  <main>
    <TheNav></TheNav>
    <TheReg></TheReg>
  </main>
</template>
<style>
main {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
</style>