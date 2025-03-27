# Etapa de construcción
FROM node:18-alpine AS builder

WORKDIR /app

COPY src/package*.json ./
COPY src/vite.config.js .
COPY src/tailwind.config.js .
COPY src/postcss.config.js .

RUN npm install

COPY src/ .

RUN npm run build

# Etapa de producción con NGINX
FROM nginx:stable-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
