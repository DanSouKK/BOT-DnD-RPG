<template>
	<v-card class="elevation-12">
	    <v-card color="black" class="white--text">
	        <v-container fill-height fluid>
	            <v-layout fill-height>
	            <v-flex xs12 align-end flexbox>
	                <span class="headline">Alterar senha</span>
	            </v-flex>
	            </v-layout>
	        </v-container>
	    </v-card>
	    <v-container fluid>
	        <v-layout row wrap>
	                <v-flex xs4 md12 sm12>
	                    <v-text-field label="Senha antiga">
	                    </v-text-field>
	                </v-flex>
		            <v-flex xs4 md12 sm12>
		                <v-text-field label="Nova senha">
		                </v-text-field>
		            </v-flex>
		            <v-flex xs4 md12 sm12>
		                <v-text-field label="Confirmar senha">
		                </v-text-field>
		            </v-flex>
	        </v-layout>
	    </v-container>
	    <v-card-actions>
	         <v-btn
	                absolute
	                dark
	                fab
	                bottom
	                right
	                color="primary"
	                slot="activator"
	                @click="update"
	            >
	                <v-icon>done</v-icon>
	            </v-btn>
	    </v-card-actions>
	</v-card>
</template>
<script>
export default {
	data () {
		return {

		}
	},
	mounted () {

	},
	methods: {
		update () {
			
		}
	}
}	
</script>
