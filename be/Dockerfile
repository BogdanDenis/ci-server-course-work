FROM ci-server-api:latest

RUN apt-get update -yq \
    && apt-get install curl gnupg -yq \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash \
    && apt-get install nodejs -yq

ENTRYPOINT ["python3"]
CMD ["/app/main.py"]
EXPOSE 8080 5678