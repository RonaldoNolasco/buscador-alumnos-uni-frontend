<template>
    <div id="app">
        <Navbar/>
        <div class="p-3 bg-dark">
            <div class="input-group">
                <input class="form-control mr-sm-2" type="text" placeholder="Ingrese el codigo" aria-label="Search" v-model="entrada" @keyup.enter="buscar">
                <select class="mr-sm-2" v-model="tipo">
                    <option value="codigo" selected="selected">Código</option>
                    <option value="ap">Apellido Paterno</option>
                    <option value="am">Apellido Materno</option>
                    <option value="nombre">Nombre</option>
                </select>
                <button class="btn btn-outline-success my-2 my-sm-0" @click="buscar">Buscar</button> 
            </div>
        </div>
        <table class="table tabla bg-dark text-white">
            <thead v-if="validos.length>0">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Codigo</th>
                    <th scope="col">Especialidad</th>
                    <th scope="col">Apellido Paterno</th>
                    <th scope="col">Apellido Materno</th>
                    <th scope="col">Nombres</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="valido in validos" v-bind:key="valido.id">
                    <th scope="row">{{valido.id}}</th>
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
        validos:[],
        validarElemento: true
        }
    },
    components: {
        Navbar,
    },
//for in es para objetos, for of es para arreglos
    methods:{
        buscar(){
            this.validos=[]
            if(this.tipo=="codigo"){
                if(this.entrada.length>5){
                    let valido=true
                    for (var dato of this.datos){
                        valido=true
                        var comp = dato.codigo.substr(0,this.entrada.length)
                        if(comp!=this.entrada) valido=false;
                        if(valido){
                            this.validos.push(
                                {
                                "id": this.validos.length + 1,
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
            }
            else if(this.tipo=="ap"){
                if(this.entrada.length>3){
                    let valido=true;
                    for(var dato of this.datos){
                        valido=true;
                        var comp = dato.nombre.split('-')[0].substr(0,this.entrada.length);
                        if(comp!=this.entrada) valido=false;
                        if(valido){
                            this.validos.push(
                                {
                                "id": this.validos.length + 1,
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
            }
            else if(this.tipo=="am"){
                if(this.entrada.length>3){
                    let valido=true;
                    for(var dato of this.datos){
                        valido=true;
                        var comp = dato.nombre.split('-')[1].substr(0,this.entrada.length);
                        if(comp!=this.entrada) valido=false;
                        if(valido){
                            this.validos.push(
                                {
                                "id": this.validos.length + 1,
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
            }
            else {
                if(this.entrada.length>3){
                    let valido=true;
                    for(var dato of this.datos){
                        valido=true;
                        if(typeof(dato.nombre.split('-')[2])=="string"){
                            var comp = dato.nombre.split('-')[2].substr(0,this.entrada.length);
                            if(comp!=this.entrada) valido=false;
                            if(valido){
                                this.validos.push(
                                    {
                                    "id": this.validos.length + 1,
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
    width: 90%;
}
</style>