<template>
    <div v-if="loading">
        <p>Loading...</p>
    </div>
    <div v-else>
        <h1>Listagem Arcos</h1>
        <hr>
        {{ arcos }}
    </div>
</template>

<script>
const api_config = require('@/api_config');

export default {
    data () {
        return {
            loading: true,
            arcos: []
        }
    },
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
        this.$http.get(api_config.arco)
        .then(function(response) {
            // console.log(response)
            // JSON responses are automatically parsed.
            self.arcos = response.data
            console.log({'msg': 'arcos loaded!', 'arcos': self.arcos})
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
    }
}
</script>

<style>
</style>
