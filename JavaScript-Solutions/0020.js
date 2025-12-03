/*
20. Valid Parentheses


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false


Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const brackets = {")" : "(", "}": "{", "]": "["};

    let open = [];

    for (const char of s) {
        if (char in brackets) {
            if (open.length && open[open.length - 1] === brackets[char]) {
                open.pop();
            } else {
                return false;
            }
        } else {
            open.push(char);
        } 
    }

    return open.length === 0;
};