# APP de Chamados

Sistema simples de gestão de chamados internos (suporte técnico).

O Sistema está distribuído da seguinte forma:
- Atendentes: App Web em Django Template (Bootstrap) Django. A camada python também é o backend do frontend em Vue.js (técnicos).
- Técnicos: FrontEnd em Vue.js
- Banco de Dados: SQLite

Requisitos para o Sistema: `docker` e `docker compose`


## Subindo a aplicação

```bash
docker compose up -d
```

Ambiente Django:
- Acessando a Aplicação da Atendente [http://localhost:8000](http://localhost:8000)
- Acessado o Swagger da API do backend [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

Ambiente FrontEnd do Técnico:
- Acessando a Aplicação do Técnico [http://localhost:5173](http://localhost:5173)

Usuários para teste:
- Django: admin + admin
- Atendente: arraes.malu@gmail.com + malu
- Tecnico: arraes.davi@gmail.com + davi


## Contato

Augusto Arraes
[site](http://linktr.ee/a.arraes)