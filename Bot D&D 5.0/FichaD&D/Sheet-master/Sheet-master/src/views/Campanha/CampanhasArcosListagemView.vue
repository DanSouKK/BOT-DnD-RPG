<template>
    <div>
        <v-layout row wrap>
            <campanhas></campanhas>
        </v-layout>
        <v-layout row wrap>
            <arcos></arcos>
        </v-layout>
    </div>
</template>

<script>
import CampanhasListagem from '@/components/Campanha/CampanhasListagem'
import ArcosListagem from '@/components/Campanha/ArcosListagem'

export default {
        data () {
            return { }
        },
        components: {
            campanhas: CampanhasListagem,
            arcos: ArcosListagem
        }
}
</script>

<style>
</style>
