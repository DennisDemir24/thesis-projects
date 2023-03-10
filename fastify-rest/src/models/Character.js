const mongoose = require("mongoose")

const CharacterSchema = new mongoose.Schema({
    id: {
        type: Number
    },
    name: {
        type: String,
    },
    status: {
        type: String,
    },
    species: {
        type: String,
    },
    type: {
        type: String,
    },
    gender: {
        type: String,
    },
    origin: {
        type: Object,
    },
    location: {
        type: Object,
    },
    image: {
        type: String,
    },
    episodes: {
        type: Array,
    },
    url: {
        type: String,
    },
    created: {
        type: Date,
    }
})


module.exports = mongoose.model("Character", CharacterSchema)