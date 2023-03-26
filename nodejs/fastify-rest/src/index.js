const fastify = require('fastify')()
const express = require('express')
const fastifyExpress = require('@fastify/express');
//const characterRoutes = require('./routes/characterRoutes')
const connectDB = require('./db/connect')
const {startingMeasurment, endingMeasurment} = require('./utils/performance')
const Character = require('./models/Character')
const {getCharacters} = require('./controllers/characterController')
connectDB()
const app = express()

const myMiddleware = (request, reply, done) => {
    const start = startingMeasurment()
    const end = endingMeasurment(start)
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

fastify.register(fastifyExpress, { app })


fastify.get('/api/characters', async (request, reply) => {
    try {
        const characters = await getCharacters()
        return characters
    } catch (err) {
        return err
    }
})

fastify.get('/api/characters/:id', async (request, reply) => {
    try {
        const character = await Character.find({id: request.params.id})
        return character
    } catch (error) {
        return error
    }
})





    
// Start the server
const start = async () => {
    try {
        await fastify.listen({
            port: 5008
        })
        fastify.log.info(`server listening on ${fastify.server.address().port}`)
    } catch (err) {
        fastify.log.error(err)
        process.exit(1)
    }
}
start()