import express from 'express'
import dotenv from 'dotenv'
import bodyParser from 'body-parser'
import cors from 'cors'
import pokemonRoutes from './routes/pokemonRoutes.js'
import connectDB from './db/connect.js'
import {seed} from "./seedScript.js"
dotenv.config()
const app = express()
connectDB()


app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// app.use('/api', pokemonRoutes)

seed()

const port = process.env.PORT || 5050
app.listen(port, () => {
    console.log(`Server is running on port ${port}`)
})