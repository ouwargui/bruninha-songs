FROM openjdk:13.0.2

WORKDIR /opt/Lavalink

COPY ./jdk-13.0.2/bin/Lavalink.jar Lavalink.jar
COPY ./jdk-13.0.2/bin/application.yml application.yml

EXPOSE 2333

CMD ["java", "-jar", "Lavalink.jar"]