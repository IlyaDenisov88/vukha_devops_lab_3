FROM ubuntu:lucid

WORKDIR /calc

COPY . /calc

CMD ["bash", "dog.bash"]




