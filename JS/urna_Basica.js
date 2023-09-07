prompt = require("prompt-sync")()

let joao = 0;
let guilherme = 0;
let maria = 0;
let nulo = 0;
let branco = 0;
let votos = 0;

while (menu != 5) {

    console.log("0- Voto Nulo")
    console.log("1- Candidato João")
    console.log("2- Candidato Guilherme")
    console.log("3- Candidato Maria")
    console.log("4- Voto em branco")
    console.log("5- Encerrar Votação")

    var menu = prompt();
    switch (menu) {

        case "0":
            nulo++
            votos++
            break;

        case "1":
            joao++
            votos++
            break;

        case "2":
            guilherme++
            votos++
            break;

        case "3":
            maria++
            votos++
            break;

        case "4":
            branco++
            votos++
            break;

        case "5":
            console.log("Encerrando Votação...")
            console.log("Total de votos: " + votos)
            console.log("Total de votos Candidato João: " + joao, (joao / votos * 100 + "% dos votos"))
            console.log("Total de votos Candidato Guilherme: " + guilherme, (guilherme / votos * 100 + "% dos votos"))
            console.log("Total de votos Candidato Maria: " + maria, (maria / votos * 100 + "% dos votos"))
            console.log("Total de votos Branco: " + branco, (branco / votos * 100 + "% dos votos"))
            console.log("Total de votos Nulo: " + nulo, (nulo / votos * 100 + "% dos votos"))
    }
}
