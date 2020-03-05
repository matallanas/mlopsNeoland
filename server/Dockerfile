FROM python:3.7

EXPOSE 5000

ENV MLFLOW_HOME /opt/mlflow
ENV SERVER_PORT 5000
ENV SERVER_HOST 0.0.0.0
ENV BACKEND_URI ${MLFLOW_HOME}/fileStore
ENV ARTIFACT_URI ${MLFLOW_HOME}/artifactStore
ENV SERVICE_NAME db
ENV SERVICE_PORT 3306

RUN pip install mlflow==1.6.0  mysqlclient==1.4.6 

RUN mkdir -p /server
WORKDIR /server
COPY ./server/wait-for-it.sh /server

RUN chmod +x wait-for-it.sh

CMD ./wait-for-it.sh ${SERVICE_NAME}:${SERVICE_PORT} -- mlflow server \
    --backend-store-uri ${BACKEND_URI} \
    --default-artifact-root ${ARTIFACT_URI} \
    --host ${SERVER_HOST} \
    --port ${SERVER_PORT}