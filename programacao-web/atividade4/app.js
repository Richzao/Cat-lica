var estoque = [];

var produto = {
  id: 5,
  nome: "Arroz",
  quantidade: 10,
};

var produto2 = {
  id: 5,
  nome: "Macarrão",
  quantidade: 10,
};

export function addProduto(estoque, produto) {
  produto.id = estoque.length + 1;
  estoque.push(produto);

  return estoque;
}

estoque = addProduto(estoque, produto);

export function listar(estoque) {
  for (let p of estoque) {
    console.log(p);
  }
}
estoque = addProduto(estoque, produto2);

export function remover(id, estoque) {
  const indexRemove = estoque.findIndex((p) => p.id === id);

  if (indexRemove !== -1) {
    estoque.splice(indexRemove, 1);
  } else {
    console.log("Id inexistente...");
  }
  return estoque;
}
