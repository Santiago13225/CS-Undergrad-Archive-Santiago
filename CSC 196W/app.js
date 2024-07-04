'use strict';

const express = require('express');
const app = express();
const port = 3000;

// Exercise 1 endpoint 7here
app.get('/math/circle/:r', function(req, res){
    let radius = req.params.r;

    let area = (Math.PI * radius *radius).toFixed(2);
    let circumference = (Math.PI * 2 * radius).toFixed(2);
    
    let jsonData = {
        "area": area,
        "circumference": circumference
    }

    console.log(typeof(jsonData));
    console.log(jsonData);
    res.send(jsonData);
});

//defining the root route for the server
app.get("/", (req, res) => {
    //sending a message as response to the route
    res.send("Go to '/math/circle/:r' where r is the radius of the circle.");
});

//const PORT = process.env.PORT || 8000;
//app.listen(PORT);

// Exercise 2 endpoint here
//const express = require('express');
//const app = express();
//const port = 3000;
// Getting Hello with name api
app.get('/hello/:name', (request, response) => {
    const{first, last} = req.query;
    if(!first, !last){
        res.status(400).send('Missing Required GET parameters:' + (!first ? 'first': 'last'));
    }else {
        res.send('Hello ' + first + ' ' + last); 
    }
})

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
})

const PORT = process.env.PORT || 8000;
app.listen(PORT);