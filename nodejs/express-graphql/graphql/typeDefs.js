const {gql} = require('apollo-server');

module.exports = gql`

    type Location {
        name: String,
        url: String
    }

    type Origin {
        name: String,
        url: String
    }

    type Character {
        id: ID
        name: String
        status: String
        species: String
        type: String
        gender: String
        origin: Origin
        location: Location
        image: String
        episodes: [String]
        url: String
    }
`

/* module.exports = gql`
    type Recipe {
        name: String
        description: String
        createdAt: String
        thumbsUp: Int
        thumbsDown: Int
    }

    input RecipeInput {
        name: String
        description: String
    }

    type Query {
        recipe(ID: ID!): Recipe!
        getRecipes(amount: Int): [Recipe]
    }

    type Mutation {
        createRecipe(recipeInput: RecipeInput): Recipe!
        deleteRecipe(ID: ID!): Boolean
        editRecipe(ID: ID!, recipeInput: RecipeInput): Recipe!
    }
` */