# Use a Node.js image for building
FROM node:18 AS builder

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy the rest of the application files
COPY . .

# Build the React app
RUN yarn build

# Use Nginx to serve the app
FROM nginx:alpine

# Remove default Nginx static files and copy our built app
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
