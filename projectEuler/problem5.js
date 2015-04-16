/*Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

//it will ahve all the primes  form 1 to maxNum
//dont need 1 
function evenlydivisibleBy(maxNum){
  //start at max if sum is not divisible by the next nubmer multiply
  // this straggey does not work it duplicates factors 
  maxNum = 10;
  // var sum = maxNum;
  // for (var i = maxNum -1 ; i > 2 ; i--){
  //   var remainder = sum % i;
  //   console.log(i , sum);
  //   console.log(sum % i);
  //   if( remainder !== 0 ){

  //     sum *= i;
  //     // console.log(sum % (sum % i ));

  //     // console.log( i , sum)
  //   }
  // } 
  // return sum

  // start with 1 
  var sum = 2; 
  for ( var i = 3 ; i <= maxNum; i++ ){
    // if( sum % i )
    // console.log(sum % i)
    console.log( 'old sum', sum)
    console.log( 'i ', i);
    var remainder = sum % i;
    console.log('remainder ', remainder)
    if(remainder !== 0){

      console.log( i % remainder)
      if( i % remainder === 0 ){
        sum *= remainder
      } else {
        sum *= i

      }

    }
    console.log('new sum ', sum)
  }

  return sum

}



// console.log(5* 2 * 3 * 3 * 4 * 7 );
// console.log(10 * 9 * 8 )
// console.log(10 * 9 * 8 * 7 )
// console.log(2 * 3 * 2 * 5 * 7 * 2 * 3 ) 
// console.log(4 % remainder)
console.log( 2 * 3 * 2 * 5 * 7 * 2)

console.log(evenlydivisibleBy(10))

// console.log( 720 % 3 )