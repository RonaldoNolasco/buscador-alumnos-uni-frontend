<template>
    <div id="app">
        <Navbar/>
        <div class="p-3 bg-dark">
            <input class="col-lg-7 col-md-7 col-sm-7 col-12 form-control" type="text" :placeholder="'Ingrese el '+relacion(tipo)" v-model="entrada" @keyup.enter="buscar" oninput="this.value = this.value.toUpperCase()">
            <select class="col-lg-3 col-md-3 col-sm-3 col-8 form-control" v-model="tipo">    
                <option value="codigo">Código</option>
                <option value="ap">Apellido Paterno</option>
                <option value="am">Apellido Materno</option>
                <option value="nombre">Nombre</option>
            </select>
            <button class="col-lg-2 col-md-2 col-sm-2 col-4 form-control btn btn-outline-success" @click="buscar">Buscar</button> 
        </div>
        <table class="table bg-dark text-white">
            <thead v-if="validos.length>0">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Imagen</th>
                    <th scope="col">Codigo</th>
                    <th scope="col">Especialidad</th>
                    <th scope="col">Apellido Paterno</th>
                    <th scope="col">Apellido Materno</th>
                    <th scope="col">Nombres</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="valido in validos" v-bind:key="valido.id">
                    <td scope="row"><strong>{{valido.id}}</strong></td>
                    <td><img :src="valido.imgUrl" width="35px"></td>
                    <td>{{valido.codigo}}</td>
                    <td>{{valido.especialidad}}</td>
                    <td>{{valido.ap}}</td>
                    <td>{{valido.am}}</td>
                    <td>{{valido.nombre}}</td>
                </tr>   
            </tbody>
        </table>
    </div>
</template>

<script>
//se puede usar v-for con li y creo que no es necesario usar computadas
//ver lo del require json
import Navbar from './components/Navbar.vue'

export default {
    name: 'app', 
    data(){
        return{
        entrada:"",
        tipo:"codigo",
        datos:require('./../public/codigos.json'),
        arrayRelacion:[
            { key:'codigo',value:'Código' },
            { key:'ap', value:'Apellido Paterno' },
            { key:'am', value:'Apellido Materno' },
            { key:'nombre', value:'Nombre' },
        ],
        validos:[],
        }
    },
    components: {
        Navbar,
    },
//for in es para objetos, for of es para arreglos
    methods:{
        /*
        relacion(cad){
            if(cad=="codigo") return "Codigo";
            else if(cad=="ap") return "Apellido Parteno";
            else if(cad=="am") return "Apellido Marteno";
            else return "Nombre";
        },
        */
        relacion(cad){
            for (var rela of this.arrayRelacion){
                if (rela.key==cad) {
                    return rela.value;
                    break;
                }
            }
        },
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
        }
    },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #000;
  min-height: 100vh;
}
.table{
    margin-bottom: 0px !important;
}
.table td{
    vertical-align: middle !important;
}
.form-control{
    display: table-row !important;
}
</style>