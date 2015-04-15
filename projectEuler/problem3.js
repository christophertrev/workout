/*
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

//this problem is basicaly find all primes of a number. 

//Naive solution

function findLargestPrime(number){

  //find all factors
  //max factor is its square root
  var squareRoot = Math.sqrt(number);
  var factors = [];
  for(var i = 2 ; i< squareRoot; i++){
    console.log('current number', i);
    console.log('number divided by cur', number/i);
    if(isInteger(number / i )){
      factors.unshift(i);
      factors.push(number/i);
    }
  }

  function isInteger(number){
    return number === Math.floor(number);
  }

  return factors

}
// Math.sqrt();

console.log(findLargestPrime(100));
