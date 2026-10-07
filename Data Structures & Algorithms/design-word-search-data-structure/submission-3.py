class WordDictionary:

    def __init__(self):
        # The root of the trie is just a dict
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        # We add each word char by char in the trie
        l = word[0]
        self.word_dict[l] = self.word_dict.get(l, {})
        curr_wd = self.word_dict
        for i in range(1, len(word)):
            prev_l = word[i-1]
            l = word[i]
            curr_wd[prev_l][l] = curr_wd[prev_l].get(l, {})
            curr_wd = curr_wd[prev_l]
        curr_wd[l]["."] = {}

    def search(self, word: str) -> bool:
        # We search within the trie using DFS with a stack
        stack = [(self.word_dict,0)]

        while stack:
            curr_wd, idx = stack.pop()
            # Expecting a word with an additional letter when there aren't any
            if not curr_wd:
                continue

            l = word[idx]
            if l != '.':
                if l not in curr_wd:
                    continue
                if len(word) == idx + 1:
                    if '.' in curr_wd[l]:
                        return True
                    continue
                stack.append((curr_wd[l], idx + 1))
            else:
                if len(curr_wd) == 1 and '.' in curr_wd:
                    continue
                if len(word) == idx + 1:
                    for l_wd in curr_wd.values():
                        if '.' in l_wd:
                            return True
                    continue
                for wd in list(curr_wd.values()):
                    if wd:
                        stack.append((wd, idx + 1))
        return False
