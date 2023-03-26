/* const Recipe = require('../models/Recipe')

module.exports = {
    Query: {
        async recipe(_, {ID}) {
            return await Recipe.findById(ID)
        },
        async getRecipes(_, {amount}) {
            return await Recipe.find().sort({createdAt: -1}).limit(amount) 
        }
    },
    Mutation: {
        async createRecipe(_, {recipeInput: {name, description}}) {
            const newRecipe = new Recipe({
                name,
                description,
                createdAt: new Date().toISOString(),
                thumbsUp: 0,
                thumbsDown: 0
            })

            const recipe = await newRecipe.save()
            return {
                id: recipe.id,
                ...recipe._doc,
            }
        }
    }
} */

const Characters = require('../models/Characters')

module.exports = {
    Query: {
        async characters() {
            try {
                const characters = await Characters.find()
                return characters
            } catch (error) {
                console.error(error)
            }
        }
    }
}