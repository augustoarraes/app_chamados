FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN apk add --no-cache iputils curl net-tools

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]