from finite_automaton.grammar import (
    generate_grammar_sentence,
    generate_grammar_expression,
    is_expression,
    is_sentence
)
from finite_automaton.ndfa import generate_NDFA, NDFA_table
from finite_automaton.dfa import generate_DFA, DFA_table


def get_inputs():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def convert_objects(lines):
    grammars = []
    acc_lines = []
    for line in lines:
        if is_expression(line):
            acc_lines.append(line)

        elif len(acc_lines) and not line:
            grammars.append(generate_grammar_expression(acc_lines))
            acc_lines = []

        if line and is_sentence(line):
            grammars.append(generate_grammar_sentence(line))

    if len(acc_lines):
        grammars.append(generate_grammar_expression(acc_lines))
        acc_lines = []
    return grammars


grammars = convert_objects(get_inputs())

print("### NDFA ###")
NDFA = generate_NDFA(grammars)
print(NDFA_table(NDFA))

print()
print("### DFA ###")
DFA = generate_DFA(NDFA)
print(DFA_table(DFA))
