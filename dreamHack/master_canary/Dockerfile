FROM ubuntu:22.04@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428a6d21

ENV user=mc_thread
ENV chall_port=7182

# Update package lists and install socat
RUN apt-get update && \
    apt-get -y install socat && \
    rm -rf /var/lib/apt/lists/*

# Add the user to the system
RUN adduser --disabled-password --gecos "" $user

# Copy the necessary files
COPY ./flag /home/$user/flag
COPY ./$user /home/$user/$user

# Change ownership and set permissions
RUN chown root:$user /home/$user/flag && \
    chown root:$user /home/$user/$user && \
    chmod 755 /home/$user/$user && \
    chmod 440 /home/$user/flag

# Set the working directory and switch to the non-root user
WORKDIR /home/$user
USER $user

# Expose the challenge port
EXPOSE $chall_port

# Use JSON array syntax for CMD to avoid potential issues
CMD ["sh", "-c", "while :; do socat -T 30 TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/$user; done"]

