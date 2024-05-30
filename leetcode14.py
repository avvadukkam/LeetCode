'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''


def longcommonprefix(strs:list)->list:
    result = ""
    for i in range(len(strs[0])): #Take the first word and itrate through each letter
        for word in strs: # for each word in the list
            if len(word) < i+1: # if the length of word is less than i return result
                return result
            elif strs[0][i] != word[i]: # if the word's split till i is not equal to the first word split till i return result
                return result
        result += strs[0][i] # Add each common letter to the result
    return result # return the result


#strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longcommonprefix(strs))
