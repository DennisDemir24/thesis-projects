import express from 'express'
import dotenv from 'dotenv'
import bodyParser from 'body-parser'
import cors from 'cors'
import axios from 'axios'
dotenv.config()

const app = express()

app.use(express.json())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}))
app.use(cors())

app.get('/', async (req, res) => {
    try {
        const {data} = await axios.get('https://pokeapi.co/api/v2/pokemon/', {
            params: {
                limit: 100
            }
        })
        res.json(data);
    } catch (err) {
        console.log(err)
    }
})


const port = process.env.PORT || 5050
app.listen(port, () => {
    console.log(`Server is running on port ${port}`)
})