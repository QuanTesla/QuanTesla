FROM node:latest
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY . /app
CMD ["npm", "run", "serve"]
# CMD ["/bin/bash"]
