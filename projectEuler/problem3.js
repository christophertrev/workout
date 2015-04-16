/*
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/



//this problem is basicaly find all primes factors of a number. 

//Naive solution



function findLargestPrimeFactor(number){

  //find all factors
  //max factor is its square root
  var squareRoot = Math.sqrt(number);
  console.log('squareRoot', squareRoot);
  var largestPrime = 0 ;
  // var smallfactors = [];
  // var largefactors = [];
  for(var i = 1 ; i<= squareRoot; i++){
    console.log('current number', i);
    console.log('number divided by cur', number/i);
    var currentOtherFactor = number/ i; 
    if(isInteger(currentOtherFactor)){
      //if the conjugate Factor is an Integer it is a properfactor
      // console.log(largestPrime < (currentOtherFactor))
      if( isPrime(i)  && largestPrime < i ){
        largestPrime = i;
      }


      if( isPrime (currentOtherFactor) && largestPrime < (currentOtherFactor) ){
        largestPrime = currentOtherFactor 
      }


      // smallfactors.push(i);
      // largefactors.unshift(currentOtherFactor);
    }
  }

  function isInteger(number){
    return number === Math.floor(number);
  }

  function isPrime(n){
    var sqrt = Math.sqrt(n)
    if(isInteger(sqrt)){
      return false;
    }
    for(var i = 2; i < sqrt; i ++){
      if(isInteger(n/i)){
        return false;
      }
    }
    return true;

  }
  // console.log(smallfactors, largefactors);
  // console.log(largestPrime);
  return largestPrime;

}
// Math.sqrt();

console.log(findLargestPrimeFactor(100));
