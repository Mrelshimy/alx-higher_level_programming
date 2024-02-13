#!/usr/bin/node
exports.converter = function (base) {
  return function (ipArgument) {
    return ipArgument.toString(base);
  };
};
