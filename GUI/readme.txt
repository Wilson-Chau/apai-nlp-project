To run the application, please read readme file inside chatbot and flask folder and follow the instruction to run front and back end.

You will also need doker to run the elastic database. Use the following command
docker run -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.security.http.ssl.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  docker.elastic.co/elasticsearch/elasticsearch:8.9.0


