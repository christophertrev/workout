/*By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?*/


var findnthPrime = function (n){
  var listOfPrimes = [2];
  var currentNumber = 3; 
  while (listOfPrimes.length < n){
    var isPrime = true;
    for(var i = 0; listOfPrimes[i] <= Math.sqrt(currentNumber); i++){
      if(currentNumber % listOfPrimes[i] === 0 ){
        isPrime = false;
      }
    }
    if(isPrime){
      listOfPrimes.push(currentNumber);
    }
    currentNumber++;


  }

  return listOfPrimes[n-1];


}



console.log(findnthPrime(10001))