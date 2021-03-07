# Libraries
import re
from ply.lex import lex
from ply.yacc import yacc

# A pre-defined dictionary to distiguish nouns
nouns = {
	'princess' : 'PRINCESS',
	'dragon' : 'DRAGON',
	'sword' : 'SWORD',
	'door' : 'DOOR',
	'house' : 'HOUSE'
}

# A pre-defined dictionary to distiguish verbs
verbs = {
	'save' : 'SAVE',
	'kill' : 'KILL',
	'swing' : 'SWING',
	'enter' : 'ENTER',
	'go' : 'GO'
}

directions = {
	'north' : 'NORTH',
	'south' : 'SOUTH',
	'east' : 'EAST',
	'west' : 'WEST'
}

# A pre-defined dictionary to distiguish articles
articles = {
	'a' : 'A',
	'the' : 'THE'
}

# A pre-defined dictionary to distiguish prepositions
prepositions = {
	'in' : 'IN',
	'on' : 'ON',
	'at' : 'AT',
	'through' : 'THROUGH'
}

# List of tokens for the lexer to compare user input to
# Adds lists of the nouns, verbs, articles, and prepositions dictionaries as
# reserved words
tokens = [
	'WORD',
	'NUMBER',
	'NOUN',
	'VERB',
	'DIRECTION',
	'ARTICLE',
	'PREPOSITION'
] + list(nouns.values()) + list(verbs.values()) + list(directions.values()) + list(articles.values()) + list(prepositions.values())
#tokens = ('LETTER', 'NUMBER', 'PLUS', 'TIMES', 'EQUAL', 'NOUN')

# Defining a word to the lexer
def t_WORD(t):
	r'[a-zA-Z]+'
	t.value = str(t.value)
	if t.value in list(nouns.values()):
		t.type = nouns.get(t.value, 'NOUN') # Convert type from a word to a noun
	if t.value in list(verbs.values()):
		t.type = verbs.get(t.value, 'VERB') # Convert type from a word to a verb
	if t.value in list(directions.values()):
		t.type = directions.get(t.value, 'DIRECTION')
	if t.value in list(articles.values()):
		t.type = articles.get(t.value, 'ARTICLE') # Convert type from a word to an article
	if t.value in list(prepositions.values()):
		t.type = prepositions.get(t.value, 'PREPOSITION') # Convert type from self.assert_(boolean expression, 'message') word to a preposition
	return t

# Defining a number to the lexer
def t_NUMBER(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t

# Skips undefined characters
def t_error(t):
	print(f'Illegal character: {t.value[0]!r}')
	t.lexer.skip(1)

# Ignores whitespace
t_ignore = ' '
def parse(user_input):
	# Pass user input from the console to the lexer
	#user_input = input()
	lexer = lex()
	lexer.input(user_input.upper())

	# Append the token type (word, noun, verb, etc.) of each token int he lexer to
	# an empty list named structure
	structure = []
	for token in lexer:
		print(token)
		#print(dir(token))

		# Test to find the type of each token from the lexer
		if token.type == 'WORD':
			print("This is a WORD!\n")
		if token.type == 'NUMBER':
			print("This is a NUMBER!\n")
		if token.type == 'NOUN':
			print("This is a NOUN!\n")
		if token.type == 'VERB':
			print("This is a VERB!\n")
		if token.type == 'DIRECTION':
			print("This is a DIRECTION!\n")
		if token.type == 'ARTICLE':
			print("This is an ARTICLE!\n")
		if token.type == 'PREPOSITION':
			print("This is a PREPOSITION!\n")
		if not token:
			break

		structure.append(token.type) # Append token types to empty list
	print(structure) # Ssee if the token types were added properly

	# Makeshift grammar test
	if structure[0] == 'ARTICLE' and structure[1] == 'NOUN':
		print("This IS a noun phrase!")
	if structure[0] == 'VERB' and structure[1] == 'DIRECTION':
		print("This IS a MOVE phrase!")
		return token.value
	else:
		print("This IS NOT a noun phrase!")
