<template>
    <div class="table-responsive">
        <table class="table bg-dark text-white border-white" v-if="this.$store.state.validos.length>0">
            <thead>
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
                <tr v-for="valido in this.$store.state.validos" v-bind:key="valido.id">
                    <th scope="row">{{valido.id}}</th>
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
}
</script>

<style>

</style>