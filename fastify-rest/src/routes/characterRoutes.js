const express = require('express')
const router = express.Router()
const Character = require("../models/Character")
const characterController = require("../controllers/characterController")


router.get('/', async (req, res) => {
    try {
        const characters = await Character.find({})
        res.status(200).json({characters})
    } catch (err) {
        res.status(500).json({err})
    }
})

router.get('/:id', async (req, res) => {
    try {
        const character = await Character.find({id: req.params.id})
        res.status(200).json({character})
    } catch (error) {
        res.status(500).json({error})
    }
})

module.exports = router