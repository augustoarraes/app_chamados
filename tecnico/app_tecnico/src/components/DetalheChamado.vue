<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "../services/api.js";

const router = useRouter()
const route = useRoute()

const chamado = ref({
    id: '',
  titulo: '',
  descricao: '',
  status: '',
  prioridade: ''
});

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3NzM3OTYxLCJpYXQiOjE3NTc3MTYzNjEsImp0aSI6ImQwNDBiYWU5Y2ZmZDQ0NmY5NDM3YWY3OTUyODgxZGE0IiwidXNlcl9pZCI6MX0.jnk_tHaisfKCiihGa93KgbPZIevRYDx2ZSIr0bbdmcs";

onMounted(async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/chamados/${route.params.id}/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    chamado.value = await response.json();
  } catch (error) {
    console.error("Erro ao carregar chamado:", error);
  }
});

async function atualizarChamado() {
  try {
    await api.put(`http://localhost:8000/api/chamados/${route.params.id}/`, {
      titulo: chamado.value.titulo,
      descricao: chamado.value.descricao,
      status: chamado.value.status,
      prioridade: chamado.value.prioridade
    },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    router.push("/"); // redireciona para Home
  } catch (error) {
    console.error("Erro ao atualizar chamado:", error);
  }
}

</script>

<template>
  <div class="p-6 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Detalhe do Chamado</h1>

    <form @submit.prevent="atualizarChamado" class="space-y-4">
      <div>
        <label class="block font-medium">ID</label>
        <input v-model="chamado.id" disabled class="border p-2 w-full bg-gray-100" />
      </div>

      <div>
        <label class="block font-medium">Título</label>
        <input v-model="chamado.titulo" disabled class="border p-2 w-full bg-gray-100" />
      </div>

      <div>
        <label class="block font-medium">Descrição</label>
        <textarea v-model="chamado.descricao" class="border p-2 w-full" rows="3"></textarea>
      </div>

      <div>
        <label class="block font-medium">Status</label>
        <select v-model="chamado.status" class="border p-2 w-full">
          <option value="open">Aberto</option>
          <option value="in_progress">Em Atendimento</option>
          <option value="resolved">Resolvido</option>
          <option value="closed">Cancelado</option>
        </select>
      </div>

      <div class="flex justify-between mt-6">
        <router-link
          to="/"
          class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
        >
          Cancelar
        </router-link>

        <button
          type="submit"
          class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Atualizar
        </button>
      </div>
    </form>
  </div>
</template>


