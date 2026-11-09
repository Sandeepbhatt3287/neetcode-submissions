class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        

        wordqueue = deque()
        wordqueue.append(beginWord)

        dis =1

        while wordqueue:

            length = len(wordqueue)

            for _ in range(length):

                word_cur = wordqueue.popleft()

                if word_cur == endWord:
                    return dis

                
                for i in range(len(word_cur)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word_cur[i]:
                            continue
                        word_new = word_cur[:i] + ch + word_cur[i+1:]
                    

                        if word_new in wordset:
                            wordqueue.append(word_new)
                            wordset.remove(word_new)
                        
            dis +=1
        
        return 0

        
        

