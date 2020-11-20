class Solution:
    def decodeString(self, s: str) -> str:
        def isInteger(char):
            try:
                int(char)
                return True
            except:
                return False
        
        count = []
        current_string = []
        ans = ""
        i = 0
        while i < len(s):
            if isInteger(s[i]):
                string_num = ""
                while isInteger(s[i]):
                    string_num += s[i]
                    i += 1
                count.append(int(string_num))
            elif s[i] == '[':
                current_string.append(ans)
                ans = ""
                i += 1
            elif s[i] == ']':
                pop_string = current_string.pop()
                pop_count = count.pop()
                ans = pop_string + ans*pop_count
                i += 1
            else:
                ans += s[i]
                i += 1
        
        return ans