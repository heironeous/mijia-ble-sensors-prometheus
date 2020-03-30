FROM python:3-alpine

RUN apk add --no-cache py-bluez make gcc libc-dev glib-dev git && \
    pip  --no-cache-dir install https://github.com/heironeous/mijia-ble-sensors-prometheus && \
