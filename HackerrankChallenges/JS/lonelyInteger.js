function findLonelyInteger(arr) {
    let lonelyInteger = 0;
  
    for (let i = 0; i < arr.length; i++) {
      lonelyInteger ^= arr[i];
    }
  
    return lonelyInteger;
  }
  
  // Exemplo de uso:
  const arr = [1, 2, 3, 4, 3, 2, 1, 6];
  const lonely = findLonelyInteger(arr);
  console.log(lonely); // Deve imprimir 4