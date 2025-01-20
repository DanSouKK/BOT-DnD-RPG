<template>
    <div>
        <arco :id='id'></arco>
    </div>
</template>

<script>
import ArcoDetalhe from '@/components/Campanha/ArcoDetalhe'

export default {
        data () {
            return { }
        },
        props: {id: String},
        components: {
            arco: ArcoDetalhe
        }
}
</script>

<style>
</style>
