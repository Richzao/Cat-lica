const calc = require("./calculadora");
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  let html = "<h1>app_calculadora</h1>";
  html += "<h3>Rotas disponíveis</h3>";
  html += '<p>/somar/:a/:b (<a href="somar/2/3">somar</a>/2/3)</p>';
  html += '<p>/subtrair/:a/:b (<a href="subtrair/2/3">subtrair/2/3</a>)</p>';
  html +=
    '<p>/multiplicar/:a/:b (<a href="multiplicar/2/3">multiplicar/2/3</a>)</p>';
  html += '<p>/dividir/:a/:b (<a href="dividir/2/3">dividir/2/3</a>)</p>';
  res.send(html);
});

app.get("/somar/:a/:b", (req, res) => {
  let a = parseFloat(req.params.a);
  let b = parseFloat(req.params.b);

  soma = calc.somar(a, b);

  res.send(`A soma de ${a} e ${b} é igual a ${soma}`);
});

app.get("/subtrair/:a/:b", (req, res) => {
  let a = parseFloat(req.params.a);
  let b = parseFloat(req.params.b);

  const subtracao = calc.subtrair(a, b);

  res.send(`A subtração de ${a} e ${b} é igual a ${subtracao}`);
});

app.get("/multiplicar/:a/:b", (req, res) => {
  let a = parseFloat(req.params.a);
  let b = parseFloat(req.params.b);

  const mult = calc.multiplicar(a, b);

  res.send(`A multiplicação de ${a} e ${b} é igual a ${mult}`);
});

app.get("/dividir/:a/:b", (req, res) => {
  let a = parseFloat(req.params.a);
  let b = parseFloat(req.params.b);

  const div = calc.dividir(a, b);

  res.send(`A divisão de ${a} e ${b} é igual a ${div}`);
});

const PORT = 8080;

app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
