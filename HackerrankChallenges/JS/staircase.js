function staircase(n) {
    let simbolo = "#";
    for (let i = 0; i < n; i++){
        console.log(simbolo.padStart(n, " "));
        simbolo += "#"
    }
}

function main() {
    const n = 10;

    staircase(n);
}
main()