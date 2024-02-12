#!/usr/bin/node
exports.AddMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
