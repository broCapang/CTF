FROM ubuntu:22.04@sha256:965fbcae990b0467ed5657caceaec165018ef44a4d2d46c7cdea80a9dff0d1ea

ENV user acs_ctf

RUN apt update
RUN apt-get install -y socat

RUN adduser $user

COPY ./deploy/flag /home/$user/flag
COPY ./deploy/prob /home/$user/prob

RUN chown -R root:$user /home/$user
RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/prob

RUN chmod 755 /home/$user/prob
RUN chmod 440 /home/$user/flag

WORKDIR /home/$user
USER $user
EXPOSE 10001
CMD socat TCP-LISTEN:10001,reuseaddr,fork EXEC:/home/$user/prob