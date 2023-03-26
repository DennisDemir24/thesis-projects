const express = require('express');
const app = express();
const {ApolloServer, gql} = require('apollo-server-express');
const Characters = require('./models/Character')
const {
    startingMeasurment,
    endingMeasurment,
} = require('./utils/performance')

// Define the middleware function

  app.use(express.json())
  app.use(express.urlencoded({ extended: false }));
  app.use((req, res, next) => {
      const start = startingMeasurment()
      console.log(start)
      res.on('finish', () => {
          const end = endingMeasurment(start)
          console.log(JSON.stringify(end))
      })
      next()
  })

const mongoose = require('mongoose')

const typeDefs = gql`
    type Query {
        characters: [Character]
        character(id: ID!): Character
        charactersByIds(ids: [ID!]!): [Character]
        getCharacters(amount: Int): [Character]
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
        getCharacters: async (_, {amount}) => {
            try {
                const characters = await Characters.find().limit(amount)
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
        },
        charactersByIds: async (_, {ids}) => {
            try {
                const characters = await Characters.find({
                    id: {
                        $in: ids
                    }
                })
                return characters
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

const PORT = process.env.PORT || 5008;
async function startServer() {
    await server.start();
    server.applyMiddleware({app});

    // use middlewares
    

    await new Promise(
        resolve => app.listen({port: PORT}, resolve)
    )
    console.log(`🚀 Server ready at http://localhost:${PORT}${server.graphqlPath}`)
    return {server, app};
}
startServer()

   /*  app.use(express.json())
    app.use(express.urlencoded({ extended: false }));
    app.use((req, res, next) => {
        const start = startingMeasurment()
        console.log(start)
        res.on('finish', () => {
            const end = endingMeasurment(start)
            console.log(JSON.stringify(end))
        })
        next()
    }) */

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










