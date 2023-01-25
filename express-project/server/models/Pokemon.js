import mongoose from "mongoose";

const PokemonSchema = new mongoose.Schema({
    name: {
        type: String,
    },
    imgUrl: {
        type: String,
    },
    /* url: {
        type: String,
    }, */
})


export const Pokemon = mongoose.model("Pokemon", PokemonSchema)