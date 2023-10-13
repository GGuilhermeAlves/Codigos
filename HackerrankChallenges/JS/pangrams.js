function pangrams(s) {
    const filtro = s.toLowerCase().match(/[a-z]/ig);
    const frase = new Set(filtro);
    
    if (frase.size === 26) {
        return "pangram";
    } else {
        return "not pangram";
    }
}