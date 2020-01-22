<template>
  <div id="app">
    <input v-model="codigo" @keyup.enter="buscar">
    <button @click="buscar">Buscar</button>
    <br>
    <table class="center">
        <tr v-if="validos.length>0">
          <td><strong>Codigo</strong></td>
          <td><strong>Especialidad</strong></td>
          <td><strong>Nombre</strong></td>
        </tr>
      <tr v-for="valido in validos" v-bind:key="valido.codigo">
        <td>{{valido.codigo}}</td>
        <td>{{valido.especialidad}}</td>
        <td>{{valido.nombre}}</td>
      </tr>
    </table>
    
  </div>
</template>

<script>
//se puede usar v-for con li y creo que no es necesario usar computadas
//ver lo del require json
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app', 
  data(){
    return{
      codigo:"",
      datos:require('./prueba.json'),
      validos:[],
    }
  },
  components: {
    HelloWorld
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
                  "codigo": dato.codigo,
                  "especialidad": dato.especialidad,
                  "nombre": dato.nombre
                }
              )
          }
        }
      }
      this.codigo=""
    }
  },
  computed:{
  }
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