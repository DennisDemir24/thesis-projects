import {Pokemon} from '../models/Pokemon.js'

const getPokemons = async (req, res) => {
    try {
        const pokemons = await Pokemon.find({})
        res.json(pokemons)
    } catch (err) {
        console.log(err)
    }
}

const getPokemon = async (req, res) => {
    try {
        // find pokemon by name
        const pokemon = await Pokemon.findOne({name: req.params.id})
        res.json(pokemon)
    } catch (err) {
        console.log(err)
    }
}



export {getPokemons, getPokemon}