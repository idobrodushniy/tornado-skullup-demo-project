FROM nginx:stable-alpine

RUN apk update && apk add nmap
COPY ./conf.d /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./wait_for_other_services.sh /etc/nginx/wait_for_other_services.sh

CMD ["nginx", "-g", "daemon off;"]