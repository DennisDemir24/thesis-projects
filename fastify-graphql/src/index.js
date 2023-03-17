const fastify = require('fastify')()
const mongoose = require('mongoose');
const { graphql, buildSchema } = require('graphql');





// Start the server
fastify.listen({port: 3000}, (err, address) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    console.log(`Server running at ${address}`);
  });