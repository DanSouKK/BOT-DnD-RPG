<template>

</template>

<script>
export default {
    name: 'LoggedExample',
    data () {
        return { }
    },
    beforeCreate: function () {
        if (!this.$session.exists()) {
            this.$router.push('/login')
        }
    },
    methods: {
        logout: function () {
            this.$session.destroy()
            this.$router.push('/login')
        }
    }
}
</script>

<style lang="css">
</style>
