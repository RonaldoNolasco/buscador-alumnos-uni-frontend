<template>
    <div id="app">
        <Navbar/>
        <Search/>
    </div>
</template>

<script>
//se puede usar v-for con li y creo que no es necesario usar computadas
//ver lo del require json
import Navbar from '@/components/Navbar.vue'
import Search from '@/components/Search.vue'

export default {
    name: 'app', 
    data(){
        return{
        }
    },
    components: {
        Navbar,
        Search
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