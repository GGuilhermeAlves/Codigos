function hackerrankInString(s) {
    let char = "hackerrank"
    let cont = 0
    for(let i = 0; i < s.length; i++){
        if(s[i] == char[cont]){
            cont++
        } 
        if(char.length == cont){
            return "YES"
        }
    }
    return "NO"
}
hackerrankInString()