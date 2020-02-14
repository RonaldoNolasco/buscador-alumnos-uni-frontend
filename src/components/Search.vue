<template>
    <div>
        <div class="p-3 bg-dark text-white">
            <input class="col-lg-8 col-md-6 col-sm-6 col-11 form-control mr-sm-2 mr-2 mb-2" type="text" :placeholder="'Ingrese el '+relacion(tipo)" v-model="entrada" @keyup.enter="buscar" oninput="this.value = this.value.toUpperCase()">
            <select class="col-lg-2 col-md-3 col-sm-3 col-7 form-control mr-sm-2 mr-2" v-model="tipo">    
                <option value="codigo">Código</option>
                <option value="ap">Apellido Paterno</option>
                <option value="am">Apellido Materno</option>
                <option value="nombre">Nombre</option>
            </select>
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
            entrada:'',
            tipo:'codigo',
            datos:require('./../../public/codigos.json'),
            arrayRelacion:[
                { key:'codigo',value:'Código' },
                { key:'ap', value:'Apellido Paterno' },
                { key:'am', value:'Apellido Materno' },
                { key:'nombre', value:'Nombre' },
            ],
            validos:[],
        }
    },
    methods:{
        buscar(){
            this.validos=[]
            let valInput=false
            if(this.tipo=="codigo" && this.entrada.length>5) valInput=true;
            if(this.tipo=="ap" && this.entrada.length>3) valInput=true;
            if(this.tipo=="am" && this.entrada.length>3) valInput=true;
            if(this.tipo=="nombre" && this.entrada.length>3) valInput=true;
            if(valInput){
                let valido=true
                for (var dato of this.datos){
                    valido=true
                    if(this.tipo=="codigo") var comp = dato.codigo.substr(0,this.entrada.length);
                    if(this.tipo=="ap") var comp = dato.nombre.split('-')[0].substr(0,this.entrada.length);
                    if(this.tipo=="am") var comp = dato.nombre.split('-')[1].substr(0,this.entrada.length);
                    if(typeof(dato.nombre.split('-')[2])=="string"){
                        if(this.tipo=="nombre") var comp = dato.nombre.split('-')[2].substr(0,this.entrada.length);
                    }
                    if(comp!=this.entrada) valido=false;
                    if(valido){
                        this.validos.push(
                            {
                            "id": this.validos.length + 1,
                            "imgUrl": "https://www.orce.uni.edu.pe/fotosuni/0060"+dato.codigo+".jpg",
                            "codigo": dato.codigo,
                            "especialidad": dato.especialidad,
                            "ap": dato.nombre.split('-')[0],
                            "am": dato.nombre.split('-')[1],
                            "nombre": dato.nombre.split('-')[2]
                            }
                        )
                    }
                }
            }
            this.entrada="";
        },
        relacion(cad){
            for (var rela of this.arrayRelacion){
                if (rela.key==cad) {
                    return rela.value;
                    break;
                }
            }
        },
        agregar(){
            this.validos.push(5);
        }
    }
}
</script>

<style>

</style>