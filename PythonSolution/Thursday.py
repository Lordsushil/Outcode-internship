from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    graph = defaultdict(list)
    level = {beginWord}
    visited = set()
    found = False

    while level and not found:
        next_level = set()
        for word in level:
            visited.add(word)
        for word in level:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        if new_word == endWord:
                            found = True
                        graph[word].append(new_word)
                        next_level.add(new_word)
        level = next_level

    res = []

    def dfs(path, word):
        if word == endWord:
            res.append(path[:])
            return
        for nei in graph[word]:
            path.append(nei)
            dfs(path, nei)
            path.pop()

    dfs([beginWord], beginWord)
    return res


beginWord = "bot"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


result = findLadders(beginWord, endWord, wordList)
print("All shortest transformation sequences:")
for seq in result:
    print(seq)
