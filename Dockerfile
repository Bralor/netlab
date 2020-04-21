FROM debian:latest
RUN apt-get -y update &&\
    apt-get -y upgrade && \
    apt-get -y install autoconf \
    build-essential \
    flex \
    bison \
    ncurses-dev \
    libreadline-dev \
    git && \
    cd home/ && \
    git clone https://gitlab.labs.nic.cz/labs/bird && \
    cd bird && \
    autoreconf && \
    ./configure && \
    make && \
    cd ../ && git clone https://gitlab.labs.nic.cz/labs/bird-tools && \
    cd bird-tools/netlab && \
    cp /home/bird/bird /home/bird/birdc common/

CMD ["./start", "-c", "cf-ospf-base"]
