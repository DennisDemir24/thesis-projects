const fastify = require('fastify')()
const express = require('express')
const fastifyExpress = require('@fastify/express');
//const characterRoutes = require('./routes/characterRoutes')
const connectDB = require('./db/connect')
const characterRoutes = require('./routes/characterRoutes')
connectDB()
const app = express()

const myMiddleware = (req, res, next) => {
    console.log('This is my middleware')
    next()
}

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(myMiddleware)
app.use('/api/characters', characterRoutes)



    
app.listen({port: 3000}, (err, address) => {
    if (err) {
        fastify.log.error(err)
        process.exit(1)
    }
    console.log(`server listening on ${address}`)
})