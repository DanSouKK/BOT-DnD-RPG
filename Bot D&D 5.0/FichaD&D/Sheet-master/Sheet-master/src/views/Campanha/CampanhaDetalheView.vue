<template>
    <div>
        <campanha :id='id'></campanha>
    </div>
</template>

<script>
import CampanhaDetalhe from '@/components/Campanha/CampanhaDetalhe'

export default {
        data () {
            return { }
        },
        props: {id: String},
        components: {
            campanha: CampanhaDetalhe
        }
}
</script>

<style>
</style>
