const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        const conn = await mongoose.connect("mongodb+srv://dennisd123:dennisd123@cluster0.yushi.mongodb.net/RestThesisAPI?retryWrites=true&w=majority")

        console.log(`MongoDB Connected: ${conn.connection.host}`)
    } catch (error) {
        console.error(`Error: ${error.message}`)
        process.exit(1)
    }
}


module.exports = connectDB