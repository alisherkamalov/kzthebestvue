<template>
<div class="hidden">
    <div class="news-root">
        <h1 class="news-text1">Актуальные <span class="news-span1">новости</span></h1>
        <div class="news-containers"
            :style="{
                height: newscontheight + 'px',
                overflow: 'hidden'
            }"
            ref="newsContainers">
            <div class="news-cont"
                v-for="(cont, index) in conts"
                :key="index">
                
            </div>  
        </div>
        <div class="buttons">
            <button @click="increaseHeight"
                class="addnews-btn"
                :style="{
                    width: widthbtnadd,
                    backgroundColor:btnaddcolor
                }">
                {{ textbtnadd }}
            </button>
            <button
                class="startnews-btn"
                :style="{
                    opacity: startbtnop,
                    display: startbtndisp
                }"
                @click="startHeight">
                Свернуть обратно
            </button>
        </div>
    </div>
</div>
    
    
</template>

<script>
import { supabase } from './SupabaseClient.js'
export default {
  data() {
    return {
      conts: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      newscontheight: 440,
      textbtnadd: 'Показать еще',
      btnaddcolor: '#4077CE',
      widthbtnadd: '150px',
      startbtnop: 0,
      startbtndisp: 'none',
      screenWidth: window.innerWidth,
      user: null
    };
  },
  computed: {
    isSmallScreen() {
      return this.screenWidth <= 700;
    }
  },
  methods: {
    increaseHeight() {
      if (this.isSmallScreen) {
        this.newscontheight += 430;
        if (this.newscontheight > 4720) {
          this.newscontheight = 4720;
          this.textbtnadd = 'Новости закончились';
          this.btnaddcolor = 'grey';
          this.widthbtnadd = '250px';
          this.startbtnop = 1;
          this.startbtndisp = 'flex';
        } else if (this.newscontheight === 440) {
          this.startbtnop = 0;
          this.startbtndisp = 'none';
        }
      } else {
        this.newscontheight += 440;
        if (this.newscontheight > 1720) {
          this.newscontheight = 1720;
          this.textbtnadd = 'Новости закончились';
          this.btnaddcolor = 'grey';
          this.widthbtnadd = '250px';
          this.startbtnop = 1;
          this.startbtndisp = 'flex';
        } else if (this.newscontheight === 440) {
          this.startbtnop = 0;
          this.startbtndisp = 'none';
        }
      }
    },
    startHeight() {
      this.newscontheight = 440;
      this.textbtnadd = 'Показать еще';
      this.btnaddcolor = '#4077CE';
      this.widthbtnadd = '150px';
      this.startbtnop = 0;
      this.startbtndisp = 'none';
    },
    updateWidth() {
      this.screenWidth = window.innerWidth;
    }
  },
  async mounted() {
    window.addEventListener('resize', this.updateWidth);
    const { data, error } = await supabase
      .from('users') // замените на правильное имя таблицы
      .select('*')
      .eq('id', '9bef0eeb-a27d-4d0d-9828-9200be823f7b') 
      .single()

    if (error) {
      console.error('Error fetching user:', error)
    } else {
      this.user = data
    }
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
};
</script>



<style scoped>
.hidden {
    max-width: 1240px;
    min-width: 300px;
    height: auto;
    
}
.buttons {
    display: flex;
    width: 100%;
    flex-direction: row;
    justify-content: start;
}
.addnews-btn {
    height: 50px;
    margin-left: 170px;
    border: 1px solid #4077CE;
    border-radius: 15px;
    font-family: "Inter";
    font-size: 15px;
    font-weight: 600;
    position: relative;
    top: -25px;
    cursor: pointer;
    color: white;
    margin-right: 25px;
    transition: all 0.5s ease-out;
}
.startnews-btn {
    height: 50px;
    cursor: pointer;
    width: 250px;
    margin-left: 15px;
    border: 1px solid #4077CE;
    border-radius: 15px;
    font-family: "Inter";
    font-size: 15px;
    font-weight: 600;
    position: relative;
    top: -25px;
    justify-content: center;
    align-items: center;
    background-color: transparent;
    margin-right: 25px;
    transition: all 0.5s ease-out;
}
.startnews-btn:active {
    scale: 0.96;
}
.startnews-btn:hover {
    color: white;
    background-color: #4077CE;
    border: 0;
}
.addnews-btn:active {
    scale: 0.96;
}
.addnews-btn:hover {
    color: white;
    background-color: #4077CE;
    border: 0;
}
.news-root {
    display: flex;
    flex-direction: column;
    max-width: 1240px;
    min-width: 300px;
    padding-top: 70px;
    gap: 35px;
    justify-content: center;
    transition: all 1s ease-out;
    box-shadow: 1px 1px 1px 1px white;
}
.news-text1 {
    width: 100%;
    text-align: center;
    font-family: 'Inter';
    font-size: 60px;
    margin-bottom: 15px;
}
.news-span1 {
    text-align: center;
    font-family: 'Inter';
    font-size: 60px;
    color: white;
    transition: all 0.5s ease-out;
    text-shadow: 2px 0 black, -2px 0 black, 0 2px black, 0 -2px black,
             1px 1px black, -1px -1px black, 1px -1px black, -1px 1px black;
}
.news-span1:hover {
    color: black;
    text-shadow: none;
}
.news-containers {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    transition: all 0.5s ease-out;
}
.news-cont {
    width: 300px;
    height: 400px;
    border-radius: 15px;
    border: 1px solid grey;
    margin-left: 15px;
    background-color: white;
    opacity: 0.3;
    margin-top: 25px;
    transition: all 0.5s ease;
}
.news-cont:hover {
    translate: 0px -15px;
    opacity: 1;
    box-shadow: 16.85px 12.18px 41.09px 1px #8a8a8ab2;
}
@media (min-width:300px) {
    .buttons {
        flex-direction: column;
        width: 100px;
    }
    .addnews-btn {
        left: -70px;
    }
    .startnews-btn {
        left: 85px;
        top: -10px;
    }
    .news-text1 {
        font-size: 30px;
    }
    .news-span1 {
        font-size: 30px;
    }
    .news-cont {
        margin-left: 15px;

    }
}
@media (min-width:1086px) {
    .buttons {
        flex-direction: row;
        width: 1000px;
    }
    .addnews-btn {
        left: auto;
    }
    .startnews-btn {
        left: auto;
        top: -25px;
    }
    .news-text1 {
        font-size: 60px;
    }
    .news-span1 {
        font-size: 60px;
    }
    .news-cont {
        margin-left: 15px;
        
    }
}
</style>