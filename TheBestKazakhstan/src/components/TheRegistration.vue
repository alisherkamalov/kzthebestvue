<template>
<div class="hidden">
    <div class="root-reg">
        <img src="/bg-a-r.jpg" class="bg-img">
        <div class="reg-cont">
            <img src="/logoreg.jpeg" class="logo"/>
            <input class="name-input" placeholder="Имя Фамилия"/>
            <input class="pass-input" placeholder="Пароль"/>
            <input class="phone-input" placeholder="Номер Телефона"/>
            <button 
            v-for="(buttonreg,index) in buttonsreg"
            :key="index"
            class="button-reg"
            :style="{
                width:buttonreg.width,
                position:buttonreg.position,
                left:buttonreg.left,
                bottom:buttonreg.bottom,
                FontSize:buttonreg.size
            }"
            >{{buttonreg.text}}</button>
        </div>
    </div>
</div>
    
</template>

<script>
export default {
    data() {
        return {
            buttonsreg: [
                {
                    text:'Зарегистрироваться',
                    width:'90%',
                    position:'relative',
                    left:'auto',
                    bottom:'auto',
                    size:'17px'
                },
                
                {
                    text:'Уже есть аккаунт? Войти',
                    width:'200px',
                    position:'absolute',
                    left:'30px',
                    bottom:'25px',
                    size:'10px'
                }
            ]
        }
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
}
//clip-path: polygon(10% 0%, 90% 0%, 100% 10%, 100% 100%, 90% 100%, 100% 100%, 0% 100%, 0% 10%);
</script>

<style scoped>
.logo {
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
body {
    perspective: 1000px;
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
    transform-style: preserve-3d;
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