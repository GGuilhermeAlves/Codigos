function miniMaxSum(arr) {
    let max = 0
    let min = 0
    
    arr.sort()
    for(let i = 0; i < arr.length -1; i++){
        
        min += arr[i];
    }
    
    arr.reverse()
    for(let i = 0; i < arr.length -1; i++){
        
        max += arr[i];
    }
    
    console.log(`${min} ${max}`)
    }