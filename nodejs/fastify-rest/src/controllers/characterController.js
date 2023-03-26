const Character = require("../models/Character")

module.exports = {
    getCharacters: async (request, reply) => {
        try {
            const characters = await Character.find({})
            return characters
        } catch (err) {
            return err
        }
    },
    getCharacter: async (request, reply) => {
        try {
            const character = await Character.find({id: request.params.id})
            return character
        } catch (error) {
            return error
        }

    }
}