const n = 1; // variável constante, ou seja, não aceita mudança de valor uma vez definida
console.log('n = ' + n)

var j = 3; // variável que permite redeclaração e alteração de valor
j = 4;
console.log('j = ' + j)

let x = 4; // variável não permite redeclaração mas permite alteração de valor
x = 5;
console.log('x = ' + x)

let nome = "Ricardo"
let telefone = "123456"
console.log("Meu nome é: " + nome + ".\nTelefone: " + telefone + ".")
console.log(`Meu nome é: ${nome}.\nTelefone: ${telefone}.`) // String template

let y = 3.14;
console.log(`O valor de x é: ${y}.`)

let b = false;
b = true;

let c = 3;

if(c){ // qualquer valor diferente de 0 retorna true
    console.log("chama")
}

let conect = null
console.log(conect)