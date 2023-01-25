import express from 'express'
import { getPokemon, getPokemons } from '../controllers/pokemonController.js'
const router = express.Router()

router.route('/').get(getPokemons)
router.route('/:id').get(getPokemon)


export default router