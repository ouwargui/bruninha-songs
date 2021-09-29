FROM openjdk:13.0.2

WORKDIR /opt/Lavalink

COPY Lavalink.jar Lavalink.jar
COPY application.yml application.yml

CMD ["java", "-jar", "Lavalink.jar"]