let h = 0
let n=20
let den = 1

while (den <= n){
    h = h + (1/den)
    den += 1
}
console.log("\n")
console.log("N: ",n)
console.log("H: ",h.toFixed(2))
