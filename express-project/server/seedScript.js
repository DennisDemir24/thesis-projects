import { Pokemon } from "./models/Pokemon.js";
import mongoose from "mongoose";
import axios from 'axios'

let pokemons = []

const fetchPokemon = async (url) => {
    try {
        const {data} = await axios.get(url)
        return data
    } catch (err) {
        console.log(err)
    }
}

const fetchPokemons = async () => {
    try {
        const {data} = await axios.get('https://pokeapi.co/api/v2/pokemon/', {
            params: {
                limit: 250
            }
        })

        const promises = data.results.map(async (item) => {
            const pokemon = await fetchPokemon(item.url)
            return pokemon
        })
        
        let promiseData = await Promise.all(promises)
        promiseData.map((item) => {
            console.log(item)
            pokemons.push({
                name: item.name,
                imgUrl: item.sprites.front_default
            });
        })
        console.log(pokemons)
        /* data.results.map(item => {
            pokemons.push({
                name: item.name,
                url: item.url
            })
        }) */
    } catch (err) {
        console.log(err)
    }
}




fetchPokemons()

export const seed = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        console.log('MongoDB Connected...')
        await Pokemon.deleteMany({})
        await Pokemon.insertMany(pokemons)
        console.log('Data Imported...')
        process.exit()
    } catch (err) {
        console.log(err)
        process.exit(1)
    }
}