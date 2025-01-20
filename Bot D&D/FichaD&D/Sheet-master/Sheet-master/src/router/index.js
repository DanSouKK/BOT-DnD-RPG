import Vue from 'vue'
import Router from 'vue-router'

import HomeView from '@/views/HomeView'
import WikiView from '@/views/WikiView'

import CampanhasArcosListagemView from '@/views/Campanha/CampanhasArcosListagemView'
import CampanhaDetalheView from '@/views/Campanha/CampanhaDetalheView'
import ArcoDetalheView from '@/views/Campanha/ArcoDetalheView'

import PersonagensListagemView from '@/views/Personagem/PersonagensListagemView'
import PersonagemDetalheView from '@/views/Personagem/PersonagemDetalheView'

import PerfilView from '@/views/Usuario/PerfilView.vue'

import LoginView from '@/views/Usuario/LoginView'
import RegisterView from '@/views/Usuario/RegisterView'


Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'HomeView',
			component: HomeView
		},
		{
			path: '/login',
			name: 'LoginView',
			component: LoginView
		},
		{
			path: '/register',
			name: 'RegisterView',
			component: RegisterView
		},
		{
			path: '/wiki',
			name: 'WikiView',
			component: WikiView
		},
		{
			path: '/campanhas_e_arcos',
			name: 'CampanhasArcosListagemView',
			component: CampanhasArcosListagemView
		},
		{
			path: '/campanha/:id',
			name: 'CampanhaDetalheView',
			component: CampanhaDetalheView,
			props: true
		},
		{
			path: '/arco/:id',
			name: 'ArcoDetalheView',
			component: ArcoDetalheView,
			props: true
		},
		{
			path: '/personagens',
			name: 'PersonagensListagemView',
			component: PersonagensListagemView
		},
		{
			path: '/personagem/:id',
			name: 'PersonagemDetalheView',
			component: PersonagemDetalheView,
			props: true
		},
		{
			path: '/perfil',
			name: 'PerfilView',
			component: PerfilView
		}
	]
})
