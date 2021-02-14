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

tokens = [
	'WORD',
	'NOUN',
	'VERB',
	'DIRECTION'
] + list(nouns.values()) + list(verbs.values()) + list(directions.values())

def t_WORD(t):
	r'[a-zA-Z]+'
	t.value = str(t.value)
	if t.value in list(nouns.values()):
		t.type = nouns.get(t.value, 'NOUN') # Convert type from a word to a noun
	if t.value in list(verbs.values()):
		t.type = verbs.get(t.value, 'VERB') # Convert type from a word to a verb
	if t.value in list(directions.values()):
		t.type = directions.get(t.value, 'DIRECTION')
	return t

def t_error(t):
	print(f'Illegal character: {t.value[0]!r}')
	t.lexer.skip(1)

t_ignore = ' '

user_input = input()
lexer = lex()
lexer.input(user_input.upper())

for token in lexer:
	print(token)

def p_move_command(p):
	'''
	moveCommand : VERB DIRECTION
	'''
	p[0] = ('VERB', p[1], 'DIRECTION', p[2])
	print(p[0])
	print('This is a MOVE COMMAND!')

parser = yacc()
output = parser.parse(user_input.upper())

if 'NORTH' in output:
	print ("You decide to head NORTH!")
if 'SOUTH' in output:
	print ("You decide to head SOUTH!")
if 'EAST' in output:
	print ("You decide to head EAST!")
if 'WEST' in output:
	print ("You decide to head WEST!")
