import express from 'express'
import { getCharacters } from '../controllers/characterController.js'
const router = express.Router()


router.route('/').get(getCharacters)


export default router