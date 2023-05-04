#!/usr/bin/node

const request = require('request');
const process = require('process');


// check if the ID number was passed to the command line
if (process.argc < 3) {
        console.log("Input the Movie ID");
        process.exit();
}

movieId = process.argv[2];
// movieUrl - api - films - movieId
movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function makeRequest(url) {
    // makeRequest - returns a promise which rejects if an error is the rsponse
    // resolve if successful
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
}

async function requestMovie(url) {
    const response = await makeRequest(url);
    const characterList = response.characters;
    return characterList;
}

async function requestData(data) {
    // requestData uses await to wait for each response from makeRequest function
    //+ then pushes it to the list
    // Return: A list
    const results = [];

    for (const charLink of data) {
        const response = await makeRequest(charLink);
        results.push(response.name);
    };

    return results;
};

requestMovie(movieUrl)
    .then((result) => {
        requestData(result)
        .then((results) => {
            for (const chars of results) {
                console.log(chars);
            }
        })
        .catch((error) => {
                console.error(error);
        });
    });
