FROM nginx:1.10.1-alpine
COPY index.html /usr/share/nginx/html
COPY index.html /usr/share/nginx/html/prod
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]