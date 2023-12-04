class Grammar:
    def _init_(self):
        self.nonterminals = set()
        self.terminals = set()
        self.productions = {}
        self.start_symbol = None

    def read_grammar_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Skip empty lines and comments

                parts = line.split('->')
                if len(parts) != 2:
                    raise ValueError(f"Invalid production: {line}")

                left_side = parts[0].strip()
                right_side = parts[1].strip()

                if not right_side:
                    raise ValueError(f"Invalid production: {line}")

                if not self.start_symbol:
                    self.start_symbol = left_side

                self.nonterminals.add(left_side)

                for symbol in right_side.split():
                    if symbol.isupper():
                        self.nonterminals.add(symbol)
                    else:
                        self.terminals.add(symbol)

                if left_side in self.productions:
                    self.productions[left_side].append(right_side)
                else:
                    self.productions[left_side] = [right_side]

    def print_nonterminals(self):
        print("Nonterminals:", ', '.join(sorted(self.nonterminals)))

    def print_terminals(self):
        print("Terminals:", ', '.join(sorted(self.terminals)))

    def print_productions(self):
        print("Productions:")
        for nonterminal, productions in self.productions.items():
            print(f"{nonterminal} -> {' | '.join(productions)}")

    def productions_for_nonterminal(self, nonterminal):
        if nonterminal in self.productions:
            return self.productions[nonterminal]
        else:
            return []

    def is_nonterminal(self, symbol):
        return symbol in self.nonterminals

    def is_terminal(self, symbol):
        return symbol in self.terminals

    def is_start_symbol(self, symbol):
        return symbol == self.start_symbol

    def is_cfg(self):
        for nonterminal, productions in self.productions.items():
            for production in productions:
                if not production[0].isupper():
                    return False  # CFG productions must start with a nonterminal
        return True


# Example usage:
if _name_ == "_main_":
    grammar = Grammar()
    grammar.read_grammar_from_file("your_grammar_file.txt")

    grammar.print_nonterminals()
    grammar.print_terminals()
    grammar.print_productions()

    # Example: Get productions for a given nonterminal
    nonterminal = 'S'
    print(f"Productions for {nonterminal}: {grammar.productions_for_nonterminal(nonterminal)}")

    # Example: Check if a symbol is a nonterminal or terminal
    symbol = 'A'
    print(f"{symbol} is a nonterminal: {grammar.is_nonterminal(symbol)}")
    print(f"{symbol} is a terminal: {grammar.is_terminal(symbol)}")

    # Example: Check if a symbol is the start symbol
    print(f"{symbol} is the start symbol: {grammar.is_start_symbol(symbol)}")

    # Example: Check if the grammar is a CFG
    print(f"Is the grammar a CFG: {grammar.is_cfg()}")