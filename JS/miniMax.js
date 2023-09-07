function miniMaxSum(arr) {
  let min = arr[0];
  let max = arr[0];
  let totalSum = 0;

  for (let i = 0; i < arr.length; i++) {
      totalSum += arr[i];
      if (arr[i] < min) {
        min = arr[i];
      }
      if (arr[i] > max) {
        max = arr[i];
      }
  }

const minSumResult = totalSum - max;
const maxSumResult = totalSum - min;

console.log(minSumResult + " " + maxSumResult);
}