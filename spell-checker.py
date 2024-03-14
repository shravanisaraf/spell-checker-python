class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SpellChecker:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        if node is None:
            return TreeNode(word)

        if word < node.value:
            node.left = self._insert(node.left, word)
        elif word > node.value:
            node.right = self._insert(node.right, word)

        return node

    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if node is None:
            return False

        if word == node.value:
            return True
        elif word < node.value:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def spell_check(self, word):
        return self.search(word)

    def find_suggestions(self, word):
        suggestions = []
        self._find_suggestions(self.root, word, suggestions)
        return suggestions

    def _find_suggestions(self, node, word, suggestions):
        if node is None:
            return

        if node.value.startswith(word):
            suggestions.append(node.value)

        if word < node.value:
            self._find_suggestions(node.left, word, suggestions)
        elif word > node.value:
            self._find_suggestions(node.right, word, suggestions)
        else:
            self._find_suggestions(node.left, word, suggestions)
            self._find_suggestions(node.right, word, suggestions)

def load_dictionary(spell_checker, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip().lower()
            spell_checker.insert(word)

def main():
    spell_checker = SpellChecker()
    dictionary_file = "mydictionary.txt"

    load_dictionary(spell_checker, dictionary_file)

    while True:
        user_input = input("Enter a word to spell check (or 'quit' to exit): ").lower()
        if user_input == 'quit':
            break

        if spell_checker.spell_check(user_input):
            print(f"{user_input} is spelled correctly.")
        else:
            suggestions = spell_checker.find_suggestions(user_input)
            if suggestions:
                print(f"{user_input} is misspelled. Suggestions: {', '.join(suggestions)}")
            else:
                print(f"{user_input} is misspelled, and no suggestions were found.")

if __name__ == "__main__":
    main()
