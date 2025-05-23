const express = require("express");
const mustacheExpress = require("mustache-express");
const { verifyCampo, verifyDate } = require("./controller/functions.js");
const app = express();

app.engine("html", mustacheExpress());
app.set("view engine", "html");
app.set("views", __dirname + "/views");
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index.html");
});

app.post("/agendar_consulta", (req, res) => {
  let dados_consulta = req.body;
  let erro_form = false;
  let campos_invalidos = [];

  const camposObrigatorios = [
    { campo: dados_consulta.nome, nome: "Nome" },
    { campo: dados_consulta.sobrenome, nome: "Sobrenome" },
    { campo: dados_consulta.cpf, nome: "CPF" },
    { campo: dados_consulta.data_nascimento, nome: "Data de nascimento" },
    { campo: dados_consulta.telefone, nome: "Telefone" },
    { campo: dados_consulta.cep, nome: "CEP" },
    { campo: dados_consulta.endereco, nome: "Endereço" },
    { campo: dados_consulta.data_consulta, nome: "Data da consulta" },
    { campo: dados_consulta.hora_consulta, nome: "Hora da consulta" },
  ];

  for (const item of camposObrigatorios) {
    if (verifyCampo(item.campo, item.nome, campos_invalidos)) {
      erro_form = true;
    }
  }

  if (
    dados_consulta.data_consulta.length > 0 &&
    dados_consulta.hora_consulta.length > 0
  ) {
    if (
      !verifyDate(dados_consulta.data_consulta, dados_consulta.hora_consulta)
    ) {
      erro_form = true;
      campos_invalidos.push("A data e a hora da consulta devem ser futuras!");
    }
  }
  res.render("index.html", { erro_form, campos_invalidos, dados_consulta });
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
