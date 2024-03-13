#!/usr/bin/node

exports.converter = function (base) {
  return function converterRec (number) {
    if (number < base) {
      return number.toString(base);
    } else {
      return converterRec(Math.floor(number / base)) + (number % base).toString(base);
    }
  };
};
