let x = 18;
let y = 6;


const operacoes = ["soma", "subtração", "multiplicação", "divisão"];

function imprimirResultado(num1, num2, resultado, op){
    console.log(`Resultado da ${op} entre ${num1} e ${num2} é igual a ${resultado}`);
}

let add = x + y;
let minus = x - y;
let mult = x * y
let div = x / y

imprimirResultado(x, y, add, operacoes[0])
imprimirResultado(x, y, minus, operacoes[1])
imprimirResultado(x, y, mult, operacoes[2])
imprimirResultado(x, y, div, operacoes[3])


let matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [true, false, null, undefined],
];

function imprimirMatriz(a){
    for(let i = 0; i < a.length; i ++){
        let linha = ""
        for(let j = 0; j < a[i].length; j++){
            linha += a[i][j] + "\t";
        }
        console.log(linha)
    }
}

imprimirMatriz(matriz);

let capitais = {
    DF: "Brasília",
    DDD_DF: 61,
    SP: "São Paulo",
    DDD_SP: 11,
    RJ: "Rio de Janeiro",
    DDD_RJ: 21
}

console.log(capitais.DF + " - " + capitais.DDD_DF)

for (const key in capitais) {
    console.log(key + ": " + capitais[key])
}

function verificar_numero_par(numx){
    if (numx % 2 == 0){
        return true
    } else {
        return false
    }
}

let numx = 8

if (verificar_numero_par(numx)){
    console.log(`O número ${numx} é par`)
} else {
    console.log(`O número ${numx} é ímpar`)
}