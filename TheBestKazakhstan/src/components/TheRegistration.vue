<template>
  <div class="hidden">
    <div class="root-reg">
      <img src="/bg-a-r.jpg" class="bg-img" loading="eager">
      <div class="reg-cont">
        <img src="/logoreg.jpeg" class="logo-reg" />
        <input v-model="name" class="name-input" placeholder="Имя Фамилия" />
        <input v-model="pass" class="pass-input" placeholder="Пароль" type="password"/>
        <input v-model="phone" class="phone-input" placeholder="Номер Телефона" type="number"/>
        <h1 class="reg-message" :style="{ opacity: opacityerror }">
          {{texterror}}
        </h1>
        <button
          v-for="(buttonreg, index) in buttonsreg"
          :key="index"
          class="button-reg"
          :style="{
            width: buttonreg.width,
            position: buttonreg.position,
            left: buttonreg.left,
            bottom: buttonreg.bottom,
            fontSize: buttonreg.size
          }"
          @click="buttonreg.click"
        >
          {{ buttonreg.text }}
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { v4 as uuidv4 } from 'uuid';

export default {
  setup() {
    const router = useRouter();
    const name = ref('');
    const pass = ref('');
    const phone = ref('');
    const opacityerror = ref('0');
    const texterror = ref('Такой аккаунт уже существует!');
    const token_user = ref(uuidv4());

    const userData = ref({
      fullname: '',
      password: '',
      phone: '',
      token: token_user.value,
    });

    const checkDuplicateUser = async (userData) => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/users/', {
          params: {
            fullname: userData.fullname,
            password: userData.password,
            phone: userData.phone
          },
          headers: { Accept: 'application/json' }
        });

        // Check if any user matches the given fullname, password, or phone
        const users = response.data;
        return users.some(user => 
          user.fullname === userData.fullname || 
          user.password === userData.password || 
          user.phone === userData.phone
        );
      } catch (error) {
        console.error('Error checking duplicate user:', error);
        return false;
      }
    };

    const createUser = async () => {
      try {
        const isDuplicate = await checkDuplicateUser(userData.value);
        if (isDuplicate) {
          opacityerror.value = '1';
          console.error('User already exists with similar data');
          return;
        }

        const response = await axios.post('http://127.0.0.1:8000/users/', userData.value, {
          headers: {
            'Content-Type': 'application/json',
          }
        });
        console.log('User created:', response.data);
        router.push('/')
        return response.data;
      } catch (error) {
        if (error.response) {
          console.error('Error response data:', error.response.data);
        }
        console.error('Error creating user:', error);
        throw error;
      }
    };

    const onRegisterButtonClick = async () => {
      userData.value.fullname = name.value;
      userData.value.password = pass.value;
      userData.value.phone = phone.value;
      userData.value.token = token_user.value;
      localStorage.setItem('userToken', userData.value.token);
      await createUser();
    };

    const buttonsreg = [
      {
        text: 'Зарегистрироваться',
        width: '90%',
        position: 'relative',
        left: 'auto',
        bottom: 'auto',
        size: '17px',
        click: onRegisterButtonClick
      },
      {
        text: 'Уже есть аккаунт? Войти',
        width: '200px',
        position: 'absolute',
        left: '30px',
        bottom: '25px',
        size: '12px',
        click: '',
        route: '/login'
      }
    ];

    return {
      buttonsreg,
      name,
      pass,
      phone,
      opacityerror,
      texterror,
      userData,
      token_user
    };
  },
  
  mounted() {
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
  }
};
</script>











  

<style>
.reg-message {
    font-size: 10px;
    height: 10px;
    position: absolute;
    bottom: 155px;
    left: 30px;
    color: red;
    transition: all 0.5s ease;
}
.overflow-regdiv {
    
    width: 150px;
    height: 150px;

}

.pre-container {
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
}
.logo-reg {
    margin-top: 15px;
    width: 100px;
    height: 75px;
}
.button-reg {
    height: 50px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #4077CE;
    color: #4077CE;
    font-family: 'Inter';
    transition: all 0.5s ease;
    cursor: pointer;
}
.button-reg:hover {
    translate: 0px -5px;
    color: white;
    background-color: #4077CE;
    border: 0px;
}
.button-reg:active {
    scale: 0.95;
}
.reg-text1 {
    margin-top: 25px;
    color: rgb(26, 26, 26);
    transition: all 0.5s ease;
    font-size: 20px;
}

input::placeholder:focus {
    color: #4077CE;
}
input:focus {
    outline: none;
    border: none;
    border-bottom: 1px solid #4077CE;
}
.name-input {
    width: 90%;
    height: 40px;
    border: 0px;
    transition: all 0.5s ease;
    border-radius: 0px;
    border-bottom: 1px solid grey;
}
.pass-input {
    width: 90%;
    height: 40px;
    border: 0px;
    border-radius: 0px;
    border-bottom: 1px solid grey;
    transition: all 0.5s ease;
}
.phone-input {
    width: 90%;
    height: 40px;
    border: 0px;
    border-radius: 0px;
    border-bottom: 1px solid grey;
    transition: all 0.5s ease;
}

.reg-cont {
    width: 50%;
    height: 350px;
    background-color: white;
    border-radius: 25px;
    position: relative;
    transition: all 0.5s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 150px;
    gap: 30px;
    
}
.bg-img {
    width: 100%;
    object-fit: cover;
    position: absolute;
}
.root-reg {
    width: 100%;
    height: 600px;
    position: relative;
    align-items: start;
    display: flex;
    justify-content: center;
}
@media (min-width:300px) {
    .bg-img {
        height: 700px;
        
    }
    .reg-cont {
        margin-top: 150px;
        width: 80%;
        height: 475px;
    }

}
@media (min-width:700px) {
    .bg-img {
        height: 700px;
        
    }
    .reg-cont {
        margin-top: 150px;
        width: 80%;
        height: 475px;
    }
}
@media (min-width:1086px) {
    .bg-img {
        height: 700px;
    }
    .reg-cont {
        margin-top: 150px;
        width: 600px;
        height: 475px;
    }
}
</style>