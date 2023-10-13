function marsExploration(s) {
    let cont = 0
    
    for(let i = 0;i < s.length; i += 3){
        if(s[i] != "S"){
           cont++ 
        }
        if(s[i+1] != "O"){
            cont++
        }
        if(s[i+2] != "S"){
            cont++
        } 
    }
    
return cont
}