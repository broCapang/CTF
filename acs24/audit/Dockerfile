FROM ubuntu:22.04@sha256:b6b83d3c331794420340093eb706a6f152d9c1fa51b262d9bf34594887c2c7ac

RUN apt-get update && apt-get install -y socat

RUN adduser acs

WORKDIR /home/acs

COPY ./flag ./flag
COPY ./deploy/prob ./prob

RUN chmod 644 ./flag 
RUN chmod 755 ./prob

USER acs

EXPOSE 8080
CMD socat TCP-LISTEN:8080,reuseaddr,fork, EXEC:"timeout 120 ./prob",stderr