import mongoose from "mongoose";

const PokemonSchema = new mongoose.Schema({
    name: {
        type: String,
    },
    type: {
        type: String,
    },
    height: {
        type: Number,
    },
    weight: {
        type: Number,
    },
    photo: {
        type: String,
    },
})


export const Pokemon = mongoose.model("Pokemon", PokemonSchema)