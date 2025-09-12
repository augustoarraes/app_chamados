import { createRouter, createWebHistory } from "vue-router";
import Chamados from "../components/Chamados.vue";
import DetalheChamado from "../components/DetalheChamado.vue";

const routes = [
  { path: "/", name: "Chamados", component: Chamados },
  { path: "/chamados/:id", name: "DetalheChamado", component: DetalheChamado, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
