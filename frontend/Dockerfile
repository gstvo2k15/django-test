FROM node:18-alpine as build-stage
WORKDIR /app
COPY src/ .
RUN npm install && npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html