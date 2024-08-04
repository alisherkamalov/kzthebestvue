import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import withUUID from "vue-uuid";
import App from './App.vue';
import router from './router';
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'

const app = createApp(App);
app.use(withUUID)
app.use(createPinia());
app.use(router);
app.use(autoAnimatePlugin)

app.mount('#app');

