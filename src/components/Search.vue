<template>
    <div>
        <div class="p-3 bg-dark text-white">
            <input class="col-lg-2 col-md-2 col-sm-2 col-2 form-control mr-sm-2 mr-2 mb-2" type="text" :placeholder="'Código'" v-model="codigo" oninput="this.value = this.value.toUpperCase()">
            <input class="col-lg-2 col-md-2 col-sm-2 col-2 form-control mr-sm-2 mr-2 mb-2" type="text" :placeholder="'Apellido paterno'" v-model="ap" oninput="this.value = this.value.toUpperCase()">
            <input class="col-lg-2 col-md-2 col-sm-2 col-2 form-control mr-sm-2 mr-2 mb-2" type="text" :placeholder="'Apellido materno'" v-model="am" oninput="this.value = this.value.toUpperCase()">
            <input class="col-lg-2 col-md-2 col-sm-2 col-2 form-control mr-sm-2 mr-2 mb-2" type="text" :placeholder="'Nombre'" v-model="nombre" oninput="this.value = this.value.toUpperCase()">
            <button class="col-lg-1 col-md-2 col-sm-2 col-3 form-control btn btn-outline-success" @click="buscar">Buscar</button>
        </div>
        <Table :validos="validos"/>
    </div>
</template>

<script>
import Table from '@/components/Table.vue'
export default {
    name:'Search',
    components:{
        Table
    },
    data() {
        return {
            codigo:"",
            ap:"",
            am:"",
            nombre:"",
            validos:[],
        }
    },
    methods:{
        buscar(){
            let response = fetch(
                'http://localhost:8081/api/registrox?'+'codigo='+this.codigo+'&nombre='+this.nombre+'&ap='+this.ap+'&am='+this.am,
                {
                    method:'GET',
                    headers:{
                        'Content-Type':'application/json;charset=utf-8'
                    }
                }
            )
            .then(response => response.json())
            .then(data => 
                {
                    this.validos = data
                    for(let [index,value] of this.validos.entries()){
                        this.validos[index].id = index+1
                        this.validos[index].imgUrl = "https://www.orce.uni.edu.pe/fotosuni/0060"+this.validos[index].codigo+".jpg"
                    }
                }
            );
        }
    }
}
</script>

<style>

</style>