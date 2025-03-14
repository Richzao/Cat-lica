const express = require('express')
const calc = require('./calculadora');

const app = express();

app.get('/', (req, res) => {
    res.send("Olá mundo");
});

app.get('/ola/:nome', (req, res) => {
    res.send(`Olá ${req.params.nome}!`);
});

const PORT = 8080;
app.listen(PORT, () => {
    console.log('App rodando na porta ' + PORT);
});