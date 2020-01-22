<template>
  <div id="app">
    <div class="field is-grouped">
      <input class="input is-info" type="text" placeholder="Info input" v-model="codigo" @keyup.enter="buscar">
      <button class="button is-info is-expanded" @click="buscar">Buscar</button>
    </div>
    <br>
    <table class="table center">
      <thead  v-if="validos.length>0">
        <tr>
          <td><strong>Codigo</strong></td>
          <td><strong>Especialidad</strong></td>
          <td><strong>Nombre</strong></td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="valido in validos" v-bind:key="valido.codigo">
          <td>{{valido.codigo}}</td>
          <td>{{valido.especialidad}}</td>
          <td>{{valido.nombre}}</td>
        </tr>
      </tbody>
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
      datos:require('./codigos.json'),
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