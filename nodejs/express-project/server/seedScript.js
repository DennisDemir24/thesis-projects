import { Character } from "./models/Character.js";
import mongoose from "mongoose";
import axios from 'axios'
import { createRequire } from "module";
const require = createRequire(import.meta.url);

const characterJson = require('./db.json')


let characters = []

const fetchCharacters = async () => {
    try {
        const { data } = await axios.get('https://rickandmortyapi.com/api/character/', {
            params: {
                count: 826,
                pages: 42,
            }
        })
        data.results.map(character => {
            characters.push({
                id: character.id,
                name: character.name,
                status: character.status,
                species: character.species,
                type: character.type,
                gender: character.gender,
                origin: {
                    name: character.origin.name,
                    url: character.origin.url,
                },
                location: {
                    name: character.location.name,
                    url: character.location.url,
                },
                image: character.image,
                episodes: character.episode,
                url: character.url,
            })
        })
    } catch (err) {
        console.log(err)
    }
}




export const seed = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        console.log('MongoDB Connected...')
        await Character.deleteMany({})
        await Character.create(characterJson)
        //await Character.insertMany(characters)
        console.log('Data Imported...')
        process.exit()
    } catch (err) {
        console.log(err)
        process.exit(1)
    }
}
