#!/usr/bin/node
if (isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
}
else if (process.argv[2] <= 0){
    return;
}
else {
    let x = process.argv[2];
    while (x > 0) {
        console.log('C is fun');
        i--;
    }
}
