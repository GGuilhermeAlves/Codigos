// Programa para listar os numeros divisiveis para cada valor dentro de um array utilizando o método .map

const prompt = require('prompt-sync')();

let numeros = [];
let continuar = true
while (continuar) {
    entrada = prompt("Digite os números: ")
    if (isNaN(entrada)) {
        console.log("saindo...")
        break
    } else {
        numeros.push(entrada)
    }
}

const divisivel = valor => {
    let divisores = []
    for (let i = 1; i <= valor; i++) {
        if (valor % i === 0) {
            divisores.push(i)
        }
    }
    return divisores
}

console.log()
console.log('Array original:')
console.log(numeros)

console.log()
console.log('Divisores dos valores do array original:')
numerosDivisiveis = numeros.map(divisivel)
console.log(numerosDivisiveis)