<template>
	<div>
		<campanhas></campanhas>
        <arcos></arcos>
		<personagens></personagens>
	</div>
</template>

<script>
import CampanhasListagem from '@/components/Campanha/CampanhasListagem'
import ArcosListagem from '@/components/Campanha/ArcosListagem'
import PersonagensListagem from '@/components/Personagem/PersonagensListagem'

export default {
	components: {
		campanhas: CampanhasListagem,
		arcos: ArcosListagem,
		personagens: PersonagensListagem
	}
}
</script>
