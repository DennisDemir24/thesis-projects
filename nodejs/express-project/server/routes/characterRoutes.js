import express from 'express'
import { getCharacters, getCharacter } from '../controllers/characterController.js'
const router = express.Router()


router.route('/').get(getCharacters)
router.route('/:id').get(getCharacter)


export default router