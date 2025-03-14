function transporMatriz(a) {  
    let at = []  
    for(let i = 0; i < a.length; i ++){
        for(let j = 0; j < a[i].length; j++){
            if (!at[j]){
                at[j] = []
            }
            at[j][i] = a[i][j]
        }
    }
    return at;
}

let a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for(let i = 0; i < a.length; i ++){
    let linha = ""
    for(let j = 0; j < a[i].length; j++){
        linha += a[i][j] + "\t";
    }
    console.log(linha)
}

a = transporMatriz(a);

for(let i = 0; i < a.length; i ++){
    let linha = ""
    for(let j = 0; j < a[i].length; j++){
        linha += a[i][j] + "\t";
    }
    console.log(linha)
}
