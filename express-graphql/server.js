const express = require('express');
const app = express();
const {ApolloServer, gql} = require('apollo-server')
const Characters = require('./models/Character')

const mongoose = require('mongoose')

const typeDefs = gql`
    type Query {
        characters: [Character]
        character(id: ID!): Character
    }

    type Location {
        name: String,
        url: String
    }

    type Origin {
        name: String,
        url: String
    }

    type Character {
        id: ID
        name: String
        status: String
        species: String
        type: String
        gender: String
        origin: Origin
        location: Location
        image: String
        episodes: [String]
        url: String
    }
`

const resolvers = {
    Query: {
        characters: async () => {
            try {
                const characters = await Characters.find()
                return characters
            } catch (error) {
                console.error(error)
            }
        },
        character: async (_, {id}) => {
            try {
                const character = await Characters.findOne({
                    id: id
                })
                return {
                    ...character._doc
                }
            } catch (error) {
                console.error(error)
            }
        }
    }
}


const server = new ApolloServer({
    typeDefs,
    resolvers
})

const connectDB = async () => {
    try {
        const conn = await mongoose.connect("mongodb+srv://dennisd123:dennisd123@cluster0.yushi.mongodb.net/RestThesisAPI?retryWrites=true&w=majority")

        console.log(`MongoDB Connected: ${conn.connection.host}`)
    } catch (error) {
        console.error(`Error: ${error.message}`)
        process.exit(1)
    }
}
connectDB()


const PORT = process.env.PORT || 5005;

server.listen(PORT,()=>{
    console.log(`Running running on port ${PORT}`)
});

