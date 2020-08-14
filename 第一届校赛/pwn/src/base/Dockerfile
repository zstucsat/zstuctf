FROM ubuntu:16.04

RUN useradd -m ctf

WORKDIR /home/ctf

COPY setup.sh /root/setup.sh
RUN chmod +x /root/setup.sh
RUN /root/setup.sh
RUN rm /root/setup.sh

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
	cp /usr/bin/timeout /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

CMD ["/bin/sh"]

EXPOSE 9999
