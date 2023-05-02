
const precoEtanol = 5.79;
const precoGasolina = 6.18;
const kmPorLitro = 10;
const distanciaEmKm = 100;
const tipoCombustivel = "Etanol";

const litrosConsumidos = distanciaEmKm / kmPorLitro;

if (tipoCombustivel === "Etanol") {
    const valorGasto = litrosConsumidos * precoEtanol;
    console.log(valorGasto.toFixed(2))
} else {
    const valorGasto = litrosConsumidos * precoGasolina;
    console.log(valorGasto.toFixed(2))
}
