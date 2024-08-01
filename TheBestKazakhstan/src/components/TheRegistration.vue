<template>
    <div class="hidden">
        <div class="root-reg">
            <img src="/bg-a-r.jpg" class="bg-img">
        </div>
    </div>
    
</template>

<script>

</script>

<style scoped>
.bg-img {
    width: 100%;
    object-fit: cover;
    position: relative;
}
.root-reg {
    width: 100%;
    height: 600px;
}
@media (min-width:300px) {
    .bg-img {
        height: 500px;
        
    }
}
@media (min-width:1086px) {
    .bg-img {
        height: 700px;
    }
}
</style>