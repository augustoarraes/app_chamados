<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="bg-white shadow-lg rounded p-6 w-96">
      <h1 class="text-2xl font-bold mb-4 text-center">Login</h1>

      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="block font-medium">Usuário</label>
          <input v-model="username" type="text" class="border p-2 w-full" required />
        </div>

        <div>
          <label class="block font-medium">Senha</label>
          <input v-model="password" type="password" class="border p-2 w-full" required />
        </div>

        <button
          type="submit"
          class="bg-blue-600 text-white px-4 py-2 rounded w-full hover:bg-blue-700"
        >
          Entrar
        </button>
      </form>

      <p v-if="errorMessage" class="text-red-500 mt-4 text-center">
        {{ errorMessage }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const username = ref("");
const password = ref("");
const errorMessage = ref("");

async function login() {
  try {
    const response = await axios.post("http://localhost:8000/api/token/", {
      username: username.value,
      password: password.value,
    });

    if (response.status === 200) {
      const token = response.data.access;
      localStorage.setItem("jwt_access_token", token); // aqui salva o token
      router.push("/"); // vai para a tela Chamados (Home)
    }
  } catch (error) {
    errorMessage.value = "Usuário ou senha inválidos";
    console.error("Erro no login:", error);
  }
}
</script>
