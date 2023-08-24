class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_line(i):
            cur_line = []
            cur_len = 0
            
            while i < len(words) and cur_len + len(words[i]) <= maxWidth:
                cur_line.append(words[i])
                cur_len += len(words[i]) + 1
                i += 1
            
            return cur_line
        
        def create_line(line,i):
            base_len = -1
            for word in line:
                base_len += len(word) + 1
            
            extra_spaces = maxWidth - base_len
            
            if(len(line) == 1 or i == len(words)):
                return " ".join(line) + " " * extra_spaces
            
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count
            
            for j in range(needs_extra_space):
                line[j] += " "
            for j in range(word_count):
                line[j] += " " * spaces_per_word
            
            return " ".join(line)
        
        ans = []
        i = 0
        
        while i < len(words):
            cur_line = get_line(i)
            i += len(cur_line)
            ans.append(create_line(cur_line,i))
            
        return ans
            
        
        print(tot_line)
        return tot_line
        