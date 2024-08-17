# Use Node.js base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the port on which the app runs
EXPOSE 3000

# Start the application
CMD ["node", "app.js"]
