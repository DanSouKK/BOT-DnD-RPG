<template>
    <v-card class="elevation-12">
        <v-card color="black" class="white--text">
            <v-container fill-height fluid>
                <v-layout fill-height>
                <v-flex xs12 align-end flexbox>
                    <span class="headline">
                        Perfil
                    </span>
                </v-flex>
                </v-layout>
            </v-container>
        </v-card>
        <v-container fluid>
            <v-layout row wrap >
                    <v-flex >
                        <v-text-field label="Usuário" v-model="user.username">
                        </v-text-field>
                    </v-flex>
                    <v-flex >
                        <v-text-field label="Email" v-model="userData.email">
                        </v-text-field>
                    </v-flex>
            </v-layout>
            <v-layout row>
                <v-flex >
                    <v-text-field label="Primeiro nome" v-model="userData.first_name">
                    </v-text-field>
                </v-flex>
                <v-flex >
                    <v-text-field label="Último nome" v-model="userData.last_name">
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
                    <v-icon>edit</v-icon>
                </v-btn>
        </v-card-actions>
    </v-card>
</template>
<script>
export default {
    props: ['user'],
    data () {
        return {
            userData: this.user
        }
    },
    computed: {

    },
    methods: {
        update () {
            this.$emit('update', this.userData)
        }
    }
}
</script>
