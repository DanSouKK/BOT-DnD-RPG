<template>
    <div>
        <personagem :id='id'></personagem>
    </div>
</template>

<script>
import PersonagemDetalhe from '@/components/Personagem/PersonagemDetalhe'

export default {
        data () {
            return { }
        },
        props: {id: String},
        components: {
            personagem: PersonagemDetalhe
        }
}
</script>

<style>
</style>
