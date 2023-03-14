# thesis-projects
Bachelors thesis in computer science, where we compare the performance between GraphQL and REST APIs in different programming languages and frameworks, and benchmark different metrics.

#fastapi-rest

curl -I http://localhost:8000/characters

#fastapi-graphql

wrk -t12 -c400 -d30s http://localhost:8000/graphql -s <(echo 'query { characters { id name } }')
