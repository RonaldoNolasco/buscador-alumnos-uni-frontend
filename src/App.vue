<template>
    <div id="app">
        <Navbar/>
        <Search/>
        <template v-if="this.$store.state.validos.length > 0">
            <Footer/>
        </template>
    </div>
</template>

<script>
//se puede usar v-for con li y creo que no es necesario usar computadas
//ver lo del require json
import Navbar from '@/components/Navbar.vue'
import Search from '@/components/Search.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'app', 
    data(){
        return{
        }
    },
    components: {
        Navbar,
        Search,
        Footer
    },
//for in es para objetos, for of es para arreglos
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