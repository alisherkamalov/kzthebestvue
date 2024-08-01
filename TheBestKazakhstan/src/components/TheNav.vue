<template>
        <div class="thenav"> 
            <div class="left-nav">
                <RouterLink to="/">
                    <img src="/logo.png" class="logo" />
                </RouterLink>
            </div>
            <div class="right-nav">
                <button v-for="(button,index) in buttons"
                :key="index"
                class="nav-button"
                :style="{
                    width:button.width
                }">
                <RouterLink class="router"
                :to="button.route">{{ button.text }}</RouterLink>
                </button>
                <div class="burger-button" @click="toggleMenu">
                    <div 
                      class="line-burger-btn" 
                      v-for="(line, index) in lines" 
                      :key="index"
                    ></div>
                </div>
            </div>
        </div>
        <div :class="{ 'burger-menu': true, active: isOpen }">
            <div class="open-burger-menu-white">
                <div class="close-burger-button"  @click="toggleMenu">
                    <div class="close-lines"  v-for="(closeline, index) in closelines" 
                    :key="index"
                    :style="{
                        rotate: closeline.rotate,
                        translate: closeline.offset
                    }"></div>
                    
                    
                </div>
                <img src="/logo.png" class="logo-burger"/>
                <button v-for="(buttonburger,index) in buttonburgers"
                    :key="index"
                    class="nav-button-burger"
                    :style="{
                        width:buttonburger.width
                    }">
                    <RouterLink 
                :to="buttonburger.route">{{ buttonburger.text }}</RouterLink>
                </button>
            </div>
            <div class="open-burger-menu-black" @click="toggleMenu"></div>
          </div>
    
    
    
</template>

<script>
import { RouterLink } from 'vue-router';
export default {
  data() {
    return {
      buttons: [
        { text: 'Регистрация', width: '150px',route:'/registration' },
        { text: 'Вход', width: '75px',route:'/authorization' },
      ],
      lines: [{}, {}, {}],
      buttonburgers: [
        { text: 'Регистрация', width: '150px',route:'/registration' },
        { text: 'Вход', width: '150px',route:'/authorization' },
      ],
      closelines: [
        { rotate: '130deg', offset: '0px 5px' },
        { rotate: '-130deg', offset: '0px -4.75px' }
      ],
      isOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style scoped>
.router {
    text-decoration: none;
    color: black;
    transition: all 0.5s ease;
}
.router:hover {
    color: white;
}
.logo-burger {
    margin-top: 15px;
    width: 45px;
    height: 45px;
    margin-bottom: 15px;
}
.right-nav {
    display: flex;
    flex-direction: row;
}
.burger-button {
    width: 45px;
    height: 45px;
    border-radius: 15px;
    border: 1px solid #4077CE;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
}
.close-burger-button {
    width: 45px;
    height: 45px;
    border-radius: 15px;
    border: 1px solid #4077CE;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
    position: absolute;
    top: 15px;
    right: 15px;
}
.close-burger-button:hover {
    background-color: #4077CE;
}
.line-burger-btn {
    width: 25px;
    height: 2px;
    margin: 4px 0;
    background-color: #4077CE;
    transition: all 0.3s ease;
}
.close-lines {
    width: 25px;
    height: 2px; 
    margin: 4px 0;
    background-color: #4077CE;
    transition: all 0.3s ease;
}
.close-burger-button:hover .close-lines{
    background-color: white;
}
.burger-button:hover {
    background-color: #4077CE;
}

.burger-button:hover .line-burger-btn {
    background-color: white;
}

.burger-button:active {
    scale: 0.96;
}

.burger-menu {
    display: none; /* Hidden by default */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 100;
    transition: all 0.3s ease;
    transition-delay: 2s;
}

.burger-menu.active {
    display: flex;
    transition: all 0.3s ease;
    transition-delay: 2s;
}

.open-burger-menu-white {
    width: 0px; /* Initially collapsed */
    height: 100%;
    background-color: white;
    z-index: 101;
    position: fixed;
    left: 0;
    top: 0;
    display: flex;
    padding-left: 15px;
    flex-direction: column;
    transition: all 0.3s ease; /* Transition for width */
    transition-delay: 2s;
}

.burger-menu.active .open-burger-menu-white {
    transition: all 0.5s ease;
    width: 200px; /* Expand to full width */
    transition-delay: 2s;
}

.open-burger-menu-black {
    width: 100%;
    height: 100%;
    background-color: black;
    opacity: 0; /* Initially transparent */
    z-index: 100;
    position: fixed;
    top: 0;
    left: 0;
    transition: all 0.3s ease; /* Transition for opacity */
    transition-delay: 2s;
}

.burger-menu.active .open-burger-menu-black {
    transition: all 0.5s ease;
    opacity: 0.5; /* Darkened background */
    transition-delay: 2s;
}

.nav-button {
    height: 50px;
    border: 1px solid #4077CE;
    border-radius: 15px;
    font-family: "Inter";
    font-size: 15px;
    font-weight: 600;
    background-color: transparent;
    margin-right: 25px;
    transition: all 0.5s ease-out;
}
.nav-button-burger {
    height: 50px;
    border: 1px solid #4077CE;
    border-radius: 15px;
    font-family: "Inter";
    font-size: 15px;
    font-weight: 600;
    background-color: transparent;
    margin-top: 10px;
    transition: all 0.5s ease-out;
}
.nav-button:active {
    scale: 0.96;
}
.nav-button:hover {
    color: white;
    background-color: #4077CE;
    border: 0;
}
.nav-button:hover .router {
    color: white;
}
.nav-button-burger:active {
    scale: 0.96;
}
.nav-button-burger:hover {
    color: white;
    background-color: #4077CE;
    border: 0;
}
.logo {
    height: 50px;
}
.thenav {
    border-radius: 25px;
    width: 1086px;
    height: 75px;
    padding-left: 25px;
    padding-right: 25px;
    margin-top: 25px;
    box-shadow: 10px 10px 50px -25px black;
    position: fixed;
    overflow: hidden;
    z-index: 99;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.3); 
    backdrop-filter: blur(10px); 
    -webkit-backdrop-filter: blur(10px);
    transition: all 0.5s ease;
}
@media (min-width:300px) {
    .thenav {
        width: 80%;
        padding-right: 25px;
    }
    .nav-button {
        display: none;
    }
    .burger-button {
        display: flex;
        flex-direction: column;
    }
}
@media (min-width:600px) {
    .thenav {
        width: 90%;
        padding-right: 25px;
    }
    .nav-button {
        display: none;
    }
    .burger-button {
        display: flex;
        flex-direction: column;
    }
}
@media (min-width:900px) {
    .thenav {
        width: 90%;
        padding-right: 0px;
    }
    .right-nav {
        display: flex;
        flex-direction: row;
    }
    .nav-button {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .burger-button {
        display: none;
    }

}
@media (min-width:1280px) {
    .thenav {
        width: 90%;
        padding-right: 0px;
    }
    .nav-button {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .right-nav {
        display: flex;
        flex-direction: row;
    }
    .burger-button {
        display: none;
    }
}
</style>