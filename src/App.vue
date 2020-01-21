<template>
  <div id="app">
    <input v-model="codigo">
    <br>
    <br>
    <ul v-for="item in validos">
      {{item}}
    </ul>
    {{validar}}
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
      datos:[
        {
          "codigo": "20199502J",
          "especialidad": "M6",
          "nombre": "FLORES-HINOJOSA-MARKO JHAMIL"
        },
        {
          "codigo": "20199501C",
          "especialidad": "M4",
          "nombre": "SARMIENTO-BELTRAN-RAFAEL JUNIOR"
        },
        {
          "codigo": "20199006B",
          "especialidad": "I1",
          "nombre": "HUAMANI-RAMOS-CELSO JULIAN"
        },
        {
          "codigo": "20199005F",
          "especialidad": "C1",
          "nombre": "ESCOBEDO-RODRIGUEZ-KENNEDYN EDILBERTO"
        },
        {
          "codigo": "20199004J",
          "especialidad": "Q1",
          "nombre": "ALARCÓN-ALIAGA-CHRISTOPHER DAVID"
        },
        {
          "codigo": "20199003C",
          "especialidad": "C1",
          "nombre": "MAQUERA-MURRUGARRA-EDUARDO MARTÍN JESÚS"
        },
        {
          "codigo": "20199002G",
          "especialidad": "M6",
          "nombre": "CASTILLO-TARAZONA-MAXIMO ALEJANDRO"
        },
        {
          "codigo": "20199001K",
          "especialidad": "N6",
          "nombre": "LÁPIZ-PINEDO-EMMANUEL FAUSTINO"
        },
        {
          "codigo": "20197507D",
          "especialidad": "S1",
          "nombre": "PALACIOS-SILVERA-RONALD JOSE"
        },
        {
          "codigo": "20197506H",
          "especialidad": "M3",
          "nombre": "QUISPE-PILLACA-RICHARD"
        },
        {
          "codigo": "20197505A",
          "especialidad": "I1",
          "nombre": "ROSALES-RODRIGUEZ-FELIX ALFREDO"
        },
        {
          "codigo": "20197504E",
          "especialidad": "M6",
          "nombre": "GAMARRA-CHAPOÑAN-ALEJANDRO DAVID"
        },
        {
          "codigo": "20197503I",
          "especialidad": "G3",
          "nombre": "QUISPE-PONCE-RAUL AUGUSTO"
        },
        {
          "codigo": "20197502B",
          "especialidad": "G1",
          "nombre": "VALENCIA-DAVALOS-JOSE ANTONIO"
        },
        {
          "codigo": "20197501F",
          "especialidad": "I2",
          "nombre": "GONZALES-LOZANO-GREGOR GERARDO"
        },
        {
          "codigo": "20197015D",
          "especialidad": "I1",
          "nombre": "HUAMANI-MACHACA-MARIA FELIPA"
        },
        {
          "codigo": "20197014H",
          "especialidad": "M4",
          "nombre": "ESPINOZA-HUAMANI-ANTONY EDWIN"
        },
        {
          "codigo": "20197013A",
          "especialidad": "N1",
          "nombre": "SALAZAR-MACALUPU-MARTIN SANTOS"
        },
        {
          "codigo": "20197012E",
          "especialidad": "P2",
          "nombre": "SAAVEDRA-MARTINEZ-PEDRO JAVIER"
        },
        {
          "codigo": "20197011I",
          "especialidad": "M5",
          "nombre": "CHAVEZ-BONILLA-LUZ ROSAURA"
        },
        {
          "codigo": "20197010B",
          "especialidad": "G3",
          "nombre": "GONZA-GONZA-JOSE LUIS"
        },
        {
          "codigo": "20197009D",
          "especialidad": "G1",
          "nombre": "LAURENTE-HUAMAN-ELEF JOEL"
        },
        {
          "codigo": "20197008H",
          "especialidad": "I2",
          "nombre": "BERRIOS-BEJAR-JORGE ALEJANDRO"
        },
        {
          "codigo": "20197007A",
          "especialidad": "S3",
          "nombre": "OSCCO-HUAMANÌ-PABLO JULIÀN"
        },
        {
          "codigo": "20197006E",
          "especialidad": "M3",
          "nombre": "MENDEZ-CÁRDENAS-EDUARD"
        },
        {
          "codigo": "20197005I",
          "especialidad": "C1",
          "nombre": "QUILLA-LAURENTE-OSCAR JUNIOR"
        },
        {
          "codigo": "20197004B",
          "especialidad": "C1",
          "nombre": "ESTUCO-TICONA-JESUS ANGEL"
        },
        {
          "codigo": "20197003F",
          "especialidad": "M6",
          "nombre": "VARGAS MACHUCA-DIONICIO-FRANK LUIS"
        },
        {
          "codigo": "20197002J",
          "especialidad": "C1",
          "nombre": "MENDOZA-QUISPE-JOSE JUNIOR"
        },
        {
          "codigo": "20197001C",
          "especialidad": "C1",
          "nombre": "ALBORNOZ-GAGO-RENZO WILLIAM"
        },
        {
          "codigo": "20195516F",
          "especialidad": "G3",
          "nombre": "YUMANGA-BRAVO-PERCY"
        },
        {
          "codigo": "20195515J",
          "especialidad": "L1",
          "nombre": "TORRES-APAZA-CARLOS MANUEL"
        },
        {
          "codigo": "20195514C",
          "especialidad": "E1",
          "nombre": "ROJAS-GUERRERO-RONALD BARONI"
        },
        {
          "codigo": "20195513G",
          "especialidad": "M4",
          "nombre": "DE LA CRUZ-ANTAURCO-MARVIN JOSEPH"
        },
        {
          "codigo": "20195512K",
          "especialidad": "S1",
          "nombre": "RAMIREZ-PADILLA-JUAN MIGUEL"
        },
        {
          "codigo": "20195511D",
          "especialidad": "S2",
          "nombre": "QUINTO-LEON-JULIO ANGEL"
        },
        {
          "codigo": "20195510H",
          "especialidad": "M5",
          "nombre": "PEREZ-PEÑA-LEONIDAS ISRAEL"
        },
        {
          "codigo": "20195509J",
          "especialidad": "I2",
          "nombre": "NATIVIDAD-ALVARADO-HENRY ALEX"
        },
        {
          "codigo": "20195508C",
          "especialidad": "M6",
          "nombre": "MEDINA-TABER-CARLOS MARTIN"
        },
        {
          "codigo": "20195507G",
          "especialidad": "E1",
          "nombre": "LAZARO-FERRER-RAFAEL ARTURO"
        },
        {
          "codigo": "20195506K",
          "especialidad": "I1",
          "nombre": "HURTADO-CHUMPITAZI-JOSÉ LUIS"
        },
        {
          "codigo": "20195505D",
          "especialidad": "L1",
          "nombre": "GARRAFA-AYQUIPA-CELIA ROMINA"
        },
        {
          "codigo": "20195504H",
          "especialidad": "E1",
          "nombre": "DOLORES-CACHAY-FERNANDO EDUARDO"
        },
        {
          "codigo": "20195503A",
          "especialidad": "I1",
          "nombre": "DIAZ-PARIONA-JEAN ROBERTO"
        },
      ],
      validos:[],
    }
  },
  components: {
    HelloWorld
  },
  computed:{
    validar:function(){
      this.validos=[]
      if(this.codigo.length!=0){
        var cad = []
        let valido=true
        for(let i=0;i<this.datos.length;i++){
          valido=true
          for(let j=0;j<this.codigo.length;j++){
            if(this.datos[i].codigo[j]!=this.codigo[j]){
              valido=false
            }
          }
          if(valido){
              this.validos.push(this.datos[i].codigo + " - " + this.datos[i].especialidad + " - " + this.datos[i].nombre)
          }
        }
        /*
        for(let i=0;i<this.datos.length;i++){
          cad = cad + " " + this.datos[i].codigo
        }
        */
        //falta revisar si se puede hacer con for in
        return("")
      }
    }
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
  margin-top: 60px;
}
</style>

