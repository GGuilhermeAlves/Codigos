const prompt = require('prompt-sync')();

let entrada = 0
let numeros = [];

entrada = prompt("Digite os números")
numeros.push(entrada)
// função para calcular o cubo
const cubo = valor => (valor * valor * valor)
// exibindo o valor original
console.log()
console.log('Array original:')
console.log(numeros)
// exibindo o vetor resultante
console.log()
console.log('Cubo dos valores do array original:')
numerosAoCubo = numeros.map(cubo)
console.log(numerosAoCubo)



