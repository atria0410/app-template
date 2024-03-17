FROM nginx:1.25.4

COPY default.conf /etc/nginx/conf.d/default.conf

COPY ./log/interface /var/log/nginx/interface
COPY ./log/api /var/log/nginx/api

CMD ["nginx", "-g", "daemon off;"]
