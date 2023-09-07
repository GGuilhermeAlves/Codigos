function camelCaseCount(s) {
    let contador = 1;
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === s[i].toUpperCase()) {
            contador++;
            console.log(s[i])
        }
    }
    
    return contador;
}

const input = "testandoExemploTeste";
console.log(camelCaseCount(input));
