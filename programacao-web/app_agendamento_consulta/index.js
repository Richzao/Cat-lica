const express = require("express");
const mustacheExpress = require("mustache-express");
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

  if (dados_consulta.nome.length == 0) {
    erro_form = true;
    campos_invalidos.push("Nome");
  }
  if (dados_consulta.sobrenome.length == 0) {
    erro_form = true;
    campos_invalidos.push("Sobrenome");
  }
  if (dados_consulta.cpf.length == 0) {
    erro_form = true;
    campos_invalidos.push("CPF");
  }

  res.render("index.html", { erro_form, campos_invalidos, dados_consulta });
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`App rodando na porta ${PORT}`);
});
