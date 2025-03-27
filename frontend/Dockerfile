# Etapa 1: construcción con Vite + Tailwind
FROM node:18-alpine as build-stage
WORKDIR /app

COPY src/package*.json ./
RUN npm install

COPY src/ .
RUN npm run build

# Etapa 2: servir con NGINX
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
