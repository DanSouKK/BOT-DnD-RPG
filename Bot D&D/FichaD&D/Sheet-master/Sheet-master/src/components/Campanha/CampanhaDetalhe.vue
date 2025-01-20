<template>
    <div v-if="loading">
        <p>Loading...</p>
    </div>
    <div v-else>
        <h1>{{ campanha.nome }}</h1>
        <hr>
        {{ campanha }}
    </div>
</template>

<script>
const api_config = require('@/api_config');

export default {
    data () {
        return {
            loading: false,
            campanha: {}
        }
    },
    props: {id: String},
    beforeCreate: function () {
        if (!this.$session.exists()) {
            this.$router.push('/login')
        }
        else{
            this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + this.$session.get('jwt')
        }
    },
    created: function () {
        let self = this
        this.$http.get(api_config.campanha+this.id+'/')
        .then(function(response) {
            // console.log(response)
            // JSON responses are automatically parsed.
            self.campanha = response.data
            console.log({'msg': 'campanha loaded!', 'campanha': self.campanha})
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
        .then(function() {
            self.loading = false
        })
    },
    methods: {
        submit() {
            let self = this
            this.$http.patch(api_config.user+self.$session.get('id')+'/', self.user)
            .then(function(response) {
                console.log(response)
                // JSON responses are automatically parsed.
                // self.user = response.data
                // console.log({'msg': 'user loaded!', 'user': self.user})
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
}
</script>

<style>
</style>
