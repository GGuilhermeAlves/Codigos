let numero = 5;
const isNumeroPar = (numero % 2) === 0;

if (isNumeroPar) {
    console.log("O Número é par");
} else {
    console.log.apply("O número é impar");
}
