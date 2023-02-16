const {ApolloServer} = require('apollo-server');
const mongoose = require('mongoose');

// APOLLO SERVEr
// typeDefs: GraphQL Type Definitions
// resolvers: How do we resolve queries / mutations

const typeDefs = require('./graphql/typeDefs');
const resolvers = require('./graphql/resolvers');

const server = new ApolloServer({
    typeDefs,
    resolvers
});

mongoose.connect(MONGODB, {useNewUrlParser: true})
    .then(() => {
        console.log('MongoDB Connected');
        return server.listen({port: 5008});
    })
    .then(res => {
        console.log(`Server running at ${res.url}`);
    })