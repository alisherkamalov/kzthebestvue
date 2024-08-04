<template>
    <div class="thenav"> 
      <div class="left-nav">
        <RouterLink to="/">
          <img src="/logo.png" class="logo" />
        </RouterLink>
      </div>
      <div class="right-nav">
        <button
          v-for="(button, index) in buttons"
          :key="index"
          class="nav-button"
          :style="{ width: button.width, display: button.display }"
        >
          <RouterLink class="router" :to="button.route">{{ button.text }}</RouterLink>
        </button>
        <div class="burger-button" @click="toggleMenu">
          <div class="line-burger-btn" v-for="(line, index) in lines" :key="index"></div>
        </div>
      </div>
    </div>
    <div :class="{ 'burger-menu': true, active: isOpen }">
      <div class="open-burger-menu-white">
        <div class="close-burger-button" @click="toggleMenu">
          <div class="close-lines" v-for="(closeline, index) in closelines" :key="index" :style="{ rotate: closeline.rotate, translate: closeline.offset }"></div>
        </div>
        <img src="/logo.png" class="logo-burger"/>
        <button
          v-for="(buttonburger, index) in buttonburgers"
          :key="index"
          class="nav-button-burger"
          :style="{ width: buttonburger.width, display: buttonburger.display }"
        >
          <RouterLink class="router" :to="buttonburger.route">{{ buttonburger.text }}</RouterLink>
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
          { text: 'Регистрация', width: '150px', route: '/registration', display: 'flex' },
          { text: 'Вход', width: '75px', route: '/authorization', display: 'flex' }
        ],
        lines: [{}, {}, {}],
        buttonburgers: [
          { text: 'Регистрация', width: '150px', route: '/registration', display: 'flex' },
          { text: 'Вход', width: '150px', route: '/authorization', display: 'flex' }
        ],
        closelines: [
          { rotate: '130deg', offset: '0px 5px' },
          { rotate: '-130deg', offset: '0px -4.75px' }
        ],
        isOpen: false,
        userFound: false
      };
    },
    async mounted() {
      this.checkUserAndUpdateButtons();
      this.checkScreenWidth();
      window.addEventListener('resize', this.checkScreenWidth);
  
      window.requestAnimationFrame(() => {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('show'); 
            } else {
              entry.target.classList.remove('show'); 
            }
          });
        }, {
          threshold: 0.1
        });
  
        const hiddenElements = document.querySelectorAll('.hidden');
        hiddenElements.forEach((el) => observer.observe(el));
      });
    },
    beforeDestroy() {
      // Clean up event listener
      window.removeEventListener('resize', this.checkScreenWidth);
    },
    methods: {
      toggleMenu() {
        this.isOpen = !this.isOpen;
      },
      
      checkScreenWidth() {
        if (window.innerWidth <= 900) {
          this.buttons[0].display = 'none';
          this.buttons[1].display = 'none';
          if (this.userFound) {
            this.buttonburgers[0].display = 'none';
            this.buttonburgers[1].display = 'flex';
            this.buttonburgers[1].text = 'Профиль';
            this.buttonburgers[1].width = '100px';
          } else {
            this.buttonburgers[0].display = 'flex';
            this.buttonburgers[1].display = 'flex';
          }
        } else {
          this.buttons[0].display = 'flex';
        this.buttons[1].display = 'flex';
          if (this.userFound) {
            this.buttons[0].display = 'none';
            this.buttons[1].display = 'flex';
            this.buttons[1].text = 'Профиль';
            this.buttons[1].width = '100px';
          } else {
            this.buttons[0].display = 'flex';
            this.buttons[1].display = 'flex';
          }
        }
      },

      checkUserAndUpdateButtons() {
        this.$nextTick(async () => {
        try {
          const storedToken = localStorage.getItem('userToken');

          if (!storedToken) {
            console.log('No token found in local storage');
            this.userFound = false;
            this.checkScreenWidth();
            return;
          }

          const response = await fetch('http://127.0.0.1:8000/users/?format=json', {
            method: 'GET',
            headers: {
              Accept: 'application/json'
            }
          });

          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const users = await response.json();
          let userExists = false;

          for (const user of users) {
            if (user.token === storedToken) {
             console.log('User found:', user.fullname);
              userExists = true;
              break; // Exit loop if token is found
            }
         }

          this.userFound = userExists;
          this.checkScreenWidth();

        } catch (error) {
        console.error('Error finding user:', error);
        this.userFound = false;
        this.checkScreenWidth();
        }
      });
}

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
    display: none; 
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
    width: 0px; 
    height: 100%;
    background-color: white;
    z-index: 101;
    position: fixed;
    left: 0;
    top: 0;
    display: flex;
    padding-left: 15px;
    flex-direction: column;
    transition: all 0.3s ease;
    transition-delay: 2s;
}

.burger-menu.active .open-burger-menu-white {
    transition: all 0.5s ease;
    width: 200px; 
    transition-delay: 2s;
}

.open-burger-menu-black {
    width: 100%;
    height: 100%;
    background-color: black;
    opacity: 0; 
    z-index: 100;
    position: fixed;
    top: 0;
    left: 0;
    transition: all 0.3s ease; 
    transition-delay: 2s;
}

.burger-menu.active .open-burger-menu-black {
    transition: all 0.5s ease;
    opacity: 0.5;
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
    justify-content: center;
    align-items: center;
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