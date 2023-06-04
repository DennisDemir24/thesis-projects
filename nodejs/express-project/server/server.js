import express from 'express'
import dotenv from 'dotenv'
import characterRoutes from './routes/characterRoutes.js'
import connectDB from './db/connect.js'
import { startingMeasurement, endingMeasurement } from './utils/performance.js'
import {seed} from "./seedScript.js"
dotenv.config()
const app = express()
connectDB()


app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// use startMeasurment and endingMeasurment middleware
app.use((req, res, next) => {
    const start = startingMeasurement()
    res.on('finish', () => {
        const end = endingMeasurement(start)
        console.log(JSON.stringify(end))
    })
    next()
})

app.use('/api/character', characterRoutes)


const port = process.env.PORT || 5050
app.listen(port, () => {
    console.log(`Server is running on port ${port}`)
})