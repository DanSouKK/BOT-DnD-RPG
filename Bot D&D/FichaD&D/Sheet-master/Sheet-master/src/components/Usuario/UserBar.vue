<template>
    <v-menu :nudge-width="100">
        <v-toolbar-title slot="activator">
            <v-btn flat>
                <span>{{ username }}&nbsp;</span>
                <v-icon>fa-caret-down</v-icon>
            </v-btn>
        </v-toolbar-title>
        <v-list>
            <v-list-tile key="Perfil" to="/perfil">
                <v-list-tile-action>
                    <v-icon>fa-user</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                    <v-list-tile-title>Perfil</v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
            <v-divider ></v-divider>
            <v-list-tile key="Sair" @click="logout">
                <v-list-tile-action>
                    <v-icon>fa-sign-out-alt</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                    <v-list-tile-title>Sair</v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
        </v-list>
    </v-menu>
</template>

<script>
export default {
    data (){
        return {
            username: this.$session.get('username')
        }
    },
    methods: {
        logout: function() {
            this.$session.destroy()
            this.$router.push('/login')
        }
    }
}
</script>

<style>
</style>
