<template>
    <div class="thehome">
      <TheNav></TheNav>
      <TheHeader></TheHeader>
    </div>
    <div class="news-center">
      <TheNews></TheNews>
    </div>
  </template>
  
  <script>
  import TheNav from '@/components/TheNav.vue'
  import TheHeader from '@/components/TheHeader.vue'
  import TheNews from '@/components/TheNews.vue'
  
  export default {
    components: { TheNav, TheHeader, TheNews },
    data() {
      return {}; 
    },
    
  }
  </script>
  
  <style scoped>
  .thehome {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
  }
  .news-center {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
  }
  </style>
  