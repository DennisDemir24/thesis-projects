const fastify = require('fastify')()
const mercurius = require('mercurius')
const Characters = require('./models/Character');
const express = require('express');
const connectDB = require('./db/connect');
const {startingMeasurement, endingMeasurement} = require('./utils/performance')
connectDB()



const myMiddleware = (request, reply, done) => {
    const start = startingMeasurement()
    const end = endingMeasurement(start)
    // reply.send(JSON.stringify(end))
    console.log(
        JSON.stringify(end)
    )
    done()
}

fastify.addHook(
    'onRequest',
    myMiddleware
)


const schema = `
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
        episode: [String]
        url: String
        created: String
    }
`

// Define resolvers
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

fastify.register(mercurius, {
    schema,
    resolvers,
    graphiql: true
})

fastify.get('/', async (request, reply) => {
    const {query} = request.body
    return reply.graphql(query)
})


// Start the server
const start = async () => {
    try {
        await fastify.listen({
            port: 5151
        })
        fastify.log.info(`server listening on ${fastify.server.address().port}`)
    } catch (err) {
        fastify.log.error(err)
        process.exit(1)
    }
}

start()