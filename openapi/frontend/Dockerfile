FROM node:22-alpine AS build

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN npm install && npm run build


FROM nginx:latest

COPY --from=build /usr/src/app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
