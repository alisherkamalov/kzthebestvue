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
    <div class="reg-div">
      <TheNav></TheNav>
      <TheReg></TheReg>
    </div>
    
  </main>
</template>
<style>
.reg-div {
  display: flex;
  justify-content: center;
  
}
</style>