<template>
    <div id="app">
        <Navbar/>
        <form class="form input-group mb-3">
            <input class="form-control mr-sm-2" type="text" placeholder="Ingrese el codigo" aria-label="Search" v-model="codigo" @keyup.enter="buscar">
            <div class="input-group-append">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit" @click="buscar">Buscar</button>
            </div>
        </form>
        <br>
        <table class="table">
            <thead v-if="validos.length>0">
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Codigo</th>
                    <th scope="col">Especialidad</th>
                    <th scope="col">A. P.</th>
                    <th scope="col">A. M.</th>
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
      codigo:"",
      datos:require('./../public/codigos.json'),
      validos:[],
    }
  },
  components: {
    Navbar,
  },
//for in es para objetos, for of es para arreglos        
    methods:{
        buscar(){
        this.validos=[]
        if(this.codigo.length>5){
            var cad = []
            let valido=true
            for (var dato of this.datos){
                valido=true
                var cad = dato.codigo
            var test = cad.substr(0,this.codigo.length)
            if(test!=this.codigo){
                valido=false
            }
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
        this.codigo=""
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
  margin-top: 20px;
}
.center{
  margin: auto;
}
</style>