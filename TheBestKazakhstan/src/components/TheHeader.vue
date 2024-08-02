<template>
    <div class="hidden">
        <div class="root-header">
            <img src="/bgheader.jpg" class="bgheader"/>
            <div class="left-header">
                <h1 class="text-header1">
                    <span class="text-span01">
                        The
                    </span>
                    <span class="text-span1">
                        Best
                    </span>
                    <span class="text-span2">
                        Kazakhstan
                    </span>
                </h1>
                <h1 class="text-header2">
                    Наш новостной сайт создан для того, чтобы предоставлять жителям Казахстана самые актуальные и достоверные новости. Мы стремимся быть вашим надежным источником информации и помочь вам быть в курсе всего, что происходит вокруг.</h1>
            </div>
            
        </div>
    </div>
    
</template>

<script>
export default {
    data() {
        return {}
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
</script>

<style>
.bgheader {
    width: 100%;
    object-fit: cover;
}
.text-header1 {
    font-family: 'Inter';
    font-size: 70px;
    width: 700px;
    

}
.text-header1:hover {
    color: white;
}
.video-header {
    translate: 0px 150px;
    width: 500px;
    height: 250px;
}
.text-header2 {
    margin-top: 15px;
    font-family: 'Inter';
    font-size: 15px;
    width: 500px;
    color: white;
    text-align: center
}
.text-span01 {
    font-family: 'Inter';
    font-size: 70px;
    color: black;
    transition: all 0.5s ease;
}
.text-span01:hover {
    color: white;
}
.text-span1 {
    font-family: 'Inter';
    font-size: 70px;
    color: white;
    color: black;
    transition: all 0.5s ease;
}
.text-span1:hover {
    color: white;
}
.text-span2 {
    font-family: 'Inter';
    font-size: 70px;
    transition: all 0.5s ease;
    color: white;
    text-shadow: 2px 0 #4ddbff, -2px 0 #4ddbff, 0 2px #4ddbff, 0 -2px #4ddbff,
             1px 1px #4ddbff, -1px -1px #4ddbff, 1px -1px #4ddbff, -1px 1px #4ddbff;
}
.text-span2:hover {
    text-shadow: none;
    color: #4ddbff;
}
.left-header {
    position: absolute;
    margin-top: 120px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.root-header {
    width: 100%;
    height: 440px;
    background-color: white;
    display: flex;
    position: relative;
    justify-content: space-between;
}
@media (min-width:300px) {
    .text-span01 {
        font-size: 45px;
        margin-right: 15px;
    }
    .text-span1 {
        font-size: 45px;
    }
    .text-span2 {
        font-size: 45px;
    }
    .text-header1 {
        line-height: 50px;
        text-align: center;
        width: 200px;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        align-content: center;
        justify-content: center;
    }
    .text-header2 {
        font-size: 15px;
        margin-top: 35px;
        width: 300px;
    }
}
@media (min-width:400px) {
    .text-span01 {
        font-size: 45px;
    }
    .text-span1 {
        font-size: 45px;
    }
    .text-span2 {
        font-size: 45px;
    }
    .text-header2 {
        font-size: 15px;
        margin-top: 35px;
        width: 300px;
    }
}
@media (min-width:700px) {
    .text-header2 {
        font-size: 15px;
        margin-top: 45px;
        width: 500px;
    }
}
@media (min-width:900px) {
    .text-span01 {
        font-size: 70px;
        margin-right: 15px;
    }
    .text-span1 {
        font-size: 70px;
        margin-right: 15px;
    }
    .text-span2 {
        font-size: 70px;
    }
    .text-header1 {
        width: 700px;
        display: flex;
        flex-wrap: nowrap;
        margin-top: 15px;
        
    }
    .text-header2 {
        font-size: 17.5px;
        margin-top: 45px;
        width: 500px;
    }
}
@media (min-width:1280px) {
    .text-span01 {
        font-size: 70px;
        margin-right: 15px;
    }
    .text-span1 {
        font-size: 70px;
        margin-right: 15px;
    }
    .text-span2 {
        font-size: 70px;
    }
    .text-header1 {
        width: 700px;
        display: flex;
        flex-wrap: nowrap;
        
    }
    .text-header2 {
        font-size: 20px;
        margin-top: 45px;
        width: 500px;
    }
}
</style>
