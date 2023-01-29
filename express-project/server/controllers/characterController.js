import {Character} from '../models/Character.js'
import { checkObjectId } from '../middleware/checkObjectId.js'

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
        // find character by id
        const {id: id} = req.params
        const character = await Character.findById({
            _id: id
        })

        if (!character) {
            return res.status(404).json({
                msg: 'Character not found'
            })
        }

        console.log(character)
        res.json(character)
    } catch (err) {
        console.log(err)
    }
}



export {getCharacters,getCharacter} 