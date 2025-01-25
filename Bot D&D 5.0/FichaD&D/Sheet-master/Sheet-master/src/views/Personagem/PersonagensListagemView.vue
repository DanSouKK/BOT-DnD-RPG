<template>
    <div>
        <personagens></personagens>
    </div>
</template>

<script>
import PersonagensListagem from '@/components/Personagem/PersonagensListagem'

export default {
        data () {
            return { }
        },
        components: {
            personagens: PersonagensListagem
        }
}
</script>

<style>
</style>
