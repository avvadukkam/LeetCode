class Solution:
    def longcommonprefix(strs:List)->List:
        result = ""
        for i in range(len(strs[0])): #Take the first word and iterate through each letter
            for word in strs: # for each word in the list
                if len(word) < i+1: # if the length of word is less than i return result
                    return result
                elif strs[0][i] != word[i]: # if the word's split till i is not equal to the first word split till i return result
                    return result
            result += strs[0][i] # Add each common letter to the result
        return result # return the result

