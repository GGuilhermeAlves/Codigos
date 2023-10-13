function plusMinus(arr) {
    let contadorPositivo = 0;
    let contadorNegativo = 0;
    let contadorZero = 0;
    
    for (let i = 0; i < arr.length; i++){
        if (arr[i] > 0){
            contadorPositivo++
        } else if (arr[i] < 0){
            contadorNegativo++
        } else {
            contadorZero++
        }
    }
}