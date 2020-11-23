class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def convertToMorse(word):
            morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            ans = ""
            for letter in word:
                ans += morse_map[ord(letter) - 97]
            return ans
        
        transformation_set = set()
        for word in words:
            morse_word = convertToMorse(word)
            if morse_word not in transformation_set:
                transformation_set.add(morse_word)
            
        return len(transformation_set)