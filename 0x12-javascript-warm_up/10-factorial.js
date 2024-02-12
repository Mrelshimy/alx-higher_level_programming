#!/usr/bin/node
function factorial(a){
    if (parseInt(a) > 0) {
    return (factorial(parseInt(a - 1)));
    }
}
console.log(factorial(process.argv[2]));
