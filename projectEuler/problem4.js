/*
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

function findLargestPalidromeProduct(nDigits){
  // start with n9's x n9s
  //possible numbers 
  var highestNumber = Math.pow(10, nDigits) - 1;
  var lowestNumber = Math.pow(10, nDigits-1);
  console.log(highestNumber, lowestNumber);

  for (var i = highestNumber; i >= lowestNumber ; i--){
    for (var j = highestNumber; j >= lowestNumber; j--){
      if(isPalidrome(j * i)){
        return i * j;
      }
    }
  }

  function isPalidrome(number){
    var numberString = number.toString(); 
    var halfWayPoint = numberString.length/2;
    var upperbound = halfWayPoint;
    if( halfWayPoint !== Math.floor(halfWayPoint)){
      //it is odd number
      halfWayPoint = Math.floor(halfWayPoint);
      upperbound = halfWayPoint +1; 
    }
    var firstHalf = numberString.slice(0,halfWayPoint);
    var secondHalf = numberString.slice(upperbound).split('').reverse().join('');
    return firstHalf === secondHalf;
  };
}


console.log(findLargestPalidromeProduct(3));
//580085