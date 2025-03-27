FROM node:18-alpine as build-stage
WORKDIR /app

COPY src/package*.json ./
COPY src/vite.config.js .
COPY src/tailwind.config.js .
COPY src/postcss.config.js .
COPY src/ .

RUN npm install
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
