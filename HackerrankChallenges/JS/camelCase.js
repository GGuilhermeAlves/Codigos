function camelcase(s) {
    let contador = 1
    for (let i = 0; i < s.length; i++){
        if (s[i] === s[i].toUpperCase()){
            contador++
        }
    }
    
    return contador
}
function main() {
    const s = "testeTestandoTestado"
    camelcase(s)
}
main()