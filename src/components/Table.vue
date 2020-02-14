<template>
    <div>
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
export default {
    name:'Table',
    props:['validos']
}
</script>

<style>

</style>