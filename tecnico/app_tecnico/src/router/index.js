import { createRouter, createWebHistory } from "vue-router";
import Chamados from "../components/Chamados.vue";
import DetalheChamado from "../components/DetalheChamado.vue";
import Login from "../components/Login.vue";

const routes = [
  { path: "/login", name: "Login", component: Login },
  { path: "/", name: "Chamados", component: Chamados },
  { path: "/chamados/:id", name: "DetalheChamado", component: DetalheChamado, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem("jwt_access_token");
  if (to.name !== "Login" && !isAuthenticated) next({ name: "Login" });
  else next();
});


export default router;
