#!/usr/bin/node
exports.logMe = function (item) {
  if (exports.logMe.preNum === undefined) {
    exports.logMe.preNum = 0;
  } else {
    exports.logMe.preNum++;
  }
  console.log(`${exports.logMe.preNum}: ${item}`);
};
