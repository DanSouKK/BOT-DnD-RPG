<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" temporary app>
            <v-toolbar flat>
                <v-list>
                    <v-list-tile>
                        <v-list-tile-title class="title">
                            Menu
                        </v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-toolbar>
            <v-divider></v-divider>
            <v-list dense class="pt-0">
                <v-list-tile v-for="route in routes" :key="route.title" :to="route.to">
                    <v-list-tile-action>
                        <v-icon>{{ route.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>{{ route.title }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app dark fixed>
            <div v-if="loggedIn">
                <v-toolbar-side-icon @click.stop="drawer = !drawer "></v-toolbar-side-icon>
            </div>
            <v-spacer></v-spacer>
            <div v-if="loggedIn">
                <userbar></userbar>
            </div>
            <div v-else>
                <v-btn key='login-button' to="/login">
                    Login
                </v-btn>
            </div>
        </v-toolbar>
        <v-toolbar-side-icon @click.stop="drawer = !drawer "></v-toolbar-side-icon>
        <v-container grid-list-xs,sm,md,lg,xl>
            <router-view></router-view>
        </v-container>
    </v-app>
</template>

<script>
const api_config = require('@/api_config');
import UserBar from '@/components/Usuario/UserBar'

export default {
    name: 'app',
    data () {
        return {
            drawer: false,
            loggedIn: this.$session.exists(),
            routes: [
                { title: 'Home', icon: 'fa-home', to: '/' },
                { title: 'Camapnhas e Arcos', icon: 'fa-dice', to:'/campanhas_e_arcos' },
                { title: 'Personagens', icon: 'fa-user-shield', to:'/personagens' },
                { title: 'Wiki', icon: 'fa-info-circle', to:'/wiki' },
            ]
        }
    },
    components: {
        userbar: UserBar
    },
    beforeUpdate: function () {
        this.loggedIn = this.$session.exists()
        if(this.$session.exists()) {
            this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + this.$session.get('jwt')
        }
    },
    timers: {
        refreshToken: { time: 500000, autostart: true, repeat: true }
    },
    methods: {
        refreshToken: function() {
            if(this.$session.exists()){
                let self = this
                this.$http.post(api_config.auth_refresh, {'refresh': this.$session.get('jwt-refresh')})
                .then(function(response) {
                    if (response.status === 200) {
                        self.$session.set('jwt', response.data.access)
                        self.$http.defaults.headers.common['Authorization'] = 'Bearer ' + self.$session.get('jwt')
                        console.log({'msg': 'token atualizado!', 'access': self.$session.get('jwt')})
                    }
                })
                .catch(function(error) {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx
                        console.log({'data': error.response.data, 'status': error.response.status, 'headers': error.response.headers})
                    } else if (error.request) {
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js
                        console.log({'request': error.request})
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        console.log({'Error': error.message})
                    }
                    console.log({'config': error.config});
                })
            }
        }
    },
}
</script>

<style>
body {
    margin: 0;
}

#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
