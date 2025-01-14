/* 
  String: Rotate String

  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

var str = "Hello World";

var rotateAmnt1 = 0;
var expected1 = "Hello World";

var rotateAmnt2 = 1;
var expected2 = "dHello Worl";

var rotateAmnt3 = 2;
var expected3 = "ldHello Wor";

var rotateAmnt4 = 4;
var expected4 = "orldHello W";

var rotateAmnt5 = 13;
var expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) { }