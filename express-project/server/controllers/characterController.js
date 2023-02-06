import {Character} from '../models/Character.js'

const getCharacters = async (req, res) => {
    try {
        const characters = await Character.find({})
        res.json(characters)
    } catch (err) {
        console.log(err)
    }
}


const getCharacter = async (req, res) => {
    try {
        const character = await Character.findOne({
            id: req.params.id
        })

        if (!character) {
            return res.status(404).json({
                msg: 'Character not found'
            })
        }

        res.json(character)
    } catch (err) {
        console.log(err)
    }
}



export {getCharacters,getCharacter} 