# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN yarn install

# Expose the application port (change if needed)
EXPOSE 3000

# Start the application
CMD ["yarn", "dev"]
