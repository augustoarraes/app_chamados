<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Lista de Chamados</h1>

    <table class="min-w-full border border-gray-300">
      <thead>
        <tr class="bg-gray-100">
          <th class="border px-4 py-2">ID</th>
          <th class="border px-4 py-2">Título</th>
          <th class="border px-4 py-2">Prioridade</th>
          <th class="border px-4 py-2">Data Criação</th>
          <th class="border px-4 py-2">Status</th>
          <th class="border px-4 py-2">Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="chamado in chamados" :key="chamado.id" class="hover:bg-gray-50">
          <td class="border px-4 py-2">{{ chamado.id }}</td>
          <td class="border px-4 py-2">{{ chamado.titulo }}</td>
          <td class="border px-4 py-2">{{ chamado.prioridade }}</td>
          <td class="border px-4 py-2">
            {{ formatarData(chamado.data_criacao) }}
          </td>
          <td class="border px-4 py-2">{{ chamado.status }}</td>
          <td class="border px-4 py-2 text-center">
            <button
              @click="detalharChamado(chamado)"
              class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
            >
              Detalhar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const chamados = ref([]);

const router = useRouter();

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3NzIyMTkyLCJpYXQiOjE3NTc3MDA1OTIsImp0aSI6IjU5ZjM5OTAyMzdkMTRiM2NiNzUzZDJmMTYxYzk5MzljIiwidXNlcl9pZCI6MX0.8ngZ84OEw0myQmV0-uA-dn70B9Pb6yMvbOdi1bL95n4";

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/chamados/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    chamados.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar chamados:", error);
  }
});

function formatarData(data) {
  return new Date(data).toLocaleString("pt-BR");
}


const detalharChamado = (sub) => {
  router.push(`/chamados/${sub.id}`)
}

</script>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}
</style>
