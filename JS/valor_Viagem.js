

const precoCombustivel = 5.70;
const kmPorLitro = 10;
const distanciaEmKm = 100;
const litrosConsumidos = distanciaEmKm / kmPorLitro;
const valorGasto = litrosConsumidos * precoCombustivel;

console.log("Litros Consumidos: "+litrosConsumidos);
console.log("Valor Gasto: R$"+valorGasto.toFixed(2));







