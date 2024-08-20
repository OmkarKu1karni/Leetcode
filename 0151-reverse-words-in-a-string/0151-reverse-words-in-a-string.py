class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        n = len(s)
        i = 0

        # Iterate over the string and extract words
        while i < n:
            if s[i] != ' ':  # If it's not a space, add the character to the current word
                word += s[i]
            else:
                if word:  # If a word is complete, add it to the list
                    words.append(word)
                    word = ""  # Reset the word for the next one
            i += 1

        # Append the last word if any
        if word:
            words.append(word)

        # Now reverse the words list manually
        left = 0
        right = len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # Manually join the words with a single space
        result = ""
        for i in range(len(words)):
            result += words[i]
            if i < len(words) - 1:  # Add a space between words, but not after the last word
                result += " "

        return result

        