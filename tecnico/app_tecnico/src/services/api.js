import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

// pega token do localStorage (ou Pinia/Vuex, se você usar)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("jwt_access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
