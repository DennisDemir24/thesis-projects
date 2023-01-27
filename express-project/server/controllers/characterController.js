import {Character} from '../models/Character.js'

const getCharacters = async (req, res) => {
    try {
        const characters = await Character.find({})
        res.json(characters)
    } catch (err) {
        console.log(err)
    }
}



export {getCharacters} 