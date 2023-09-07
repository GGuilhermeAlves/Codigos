function divisores(numero) {
  let lista = [];
  for (let valor; valor <= numero; valor++) {
    if (numero % valor == 0) {
      lista.push(valor);
    }
  }
  return lista;
}
