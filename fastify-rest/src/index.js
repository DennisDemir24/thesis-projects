const Fastify = require('fastify')
const app = Fastify({
    logger: true
})
const characterRoutes = require('./routes/characterRoutes')
const connectDB = require('./db/connect')
connectDB()
characterRoutes(app)

    
app.listen({port: 3000}, (err, address) => {
    if (err) {
        fastify.log.error(err)
        process.exit(1)
    }
    console.log(`server listening on ${address}`)
})