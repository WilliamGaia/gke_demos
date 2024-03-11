FROM nginx:1.10.1-alpine
COPY index.html /usr/share/nginx/html
COPY ./test/index.html /usr/share/nginx/html/test
COPY default.conf /etc/nginx/conf.d
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]