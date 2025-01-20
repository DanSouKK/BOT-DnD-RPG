<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="dark">
                        <v-toolbar-title>Login form</v-toolbar-title>
                        <v-spacer></v-spacer>
                    </v-toolbar>
                    <v-card-text>
                        <v-alert v-if="error_auth" v-model="show_error_auth" dismissible type="error">
                            {{ error_auth.response.data.non_field_errors[0] }}
                        </v-alert>
                        <v-alert v-if="error_me" v-model="show_error_me" dismissible type="error">
                            {{ error_me.response.data.detail }}
                        </v-alert>

                        <v-text-field v-model="user.username" prepend-icon="fa-user" name="username" label="Username" type="text"></v-text-field>
                        <v-text-field v-model="user.password" id="password" prepend-icon="fa-lock" name="Password" label="Password" type="password"></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>

                        <v-btn color="info" to="/register">Register</v-btn>
                        or
                        <v-btn color="dark" @click="submit()">Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
const api_config = require('@/api_config');

export default {
    data (){
        return {
            user: {
                username: '',
                password: '',
            },
            error_auth: '',
            show_error_auth: true,
            error_me: '',
            show_error_me: true
        }
    },
    beforeCreate: function() {
        this.$session.destroy()
    },
    created: function() {
        this.$session.destroy()
    },
    afterCreate: function() {
        this.$session.destroy()
    },
    methods: {
        submit() {
            this.show_error_auth = true
            this.show_error_me = true
            this.$session.destroy()
            let self = this
            this.$http.post(api_config.auth, this.user)
            .then(function (response) {
                console.log({'msg': 'POST auth', 'response': response})
                if (response.status === 200) {
                    self.$session.start()
                    self.$session.set('jwt', response.data.access)
                    self.$session.set('jwt-refresh', response.data.refresh)
                    // console.log({'id_user': self.$session.get('id'), 'username': self.$session.get('username'), 'jwt': self.$session.get('jwt'), 'jwt-refresh': self.$session.get('jwt-refresh')})
                    self.$http.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
                }
            })
            .catch(function (error) {
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
                self.error_auth = error
                console.log({'config': error.config});
            })
            .then(function (){
                self.$http.get(api_config.user_me)
                .then(function (response) {
                    console.log({'msg': 'POST user_me', 'response': response})
                    if (response.status === 200) {
                        self.$session.set('username', response.data.username)
                        self.$session.set('id', response.data.id)
                        // console.log({'id_user': self.$session.get('id'), 'username': self.$session.get('username'), 'jwt': self.$session.get('jwt'), 'jwt-refresh': self.$session.get('jwt-refresh')})
                        self.$router.push('/')
                    }
                })
                .catch(function (error) {
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
                    self.error_me = error
                    console.log({'config': error.config});
                })
            })
        }
    }
}
</script>

<style>
</style>
