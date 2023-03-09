const characterController = require('../controllers/characterController')

module.exports = (app) => {
    app.get('/api/characters', characterController.getCharacters)

    app.get('/api/characters/:id', characterController.getCharacter)
}