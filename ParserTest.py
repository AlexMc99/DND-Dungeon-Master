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
	'go' : 'GO',
	'grab' : 'GRAB'
}

directions = {
	'north' : 'NORTH',
	'south' : 'SOUTH',
	'east' : 'EAST',
	'west' : 'WEST'
}

items = {
	'potion' : 'POTION',
	'bag' : 'BAG'
}

articles = {
	'a' : 'A',
	'the' : 'THE'
}

tokens = [
	'WORD',
	'NOUN',
	'VERB',
	'DIRECTION',
	'ITEM',
	'ARTICLE'
] + list(nouns.values()) + list(verbs.values()) + list(directions.values()) + list(items.values()) + list(articles.values())

def t_WORD(t):
	r'[a-zA-Z]+'
	t.value = str(t.value)
	if t.value in list(nouns.values()):
		t.type = nouns.get(t.value, 'NOUN') # Convert type from a word to a noun
	if t.value in list(verbs.values()):
		t.type = verbs.get(t.value, 'VERB') # Convert type from a word to a verb
	if t.value in list(directions.values()):
		t.type = directions.get(t.value, 'DIRECTION')
	if t.value in list(items.values()):
		t.type = items.get(t.value, 'ITEM')
	if t.value in list(articles.values()):
		t.type = articles.get(t.value, 'ARTICLE')
	return t

def t_error(t):
	print(f'Illegal character: {t.value[0]!r}')
	t.lexer.skip(1)

t_ignore = ' '

user_input = input()
lexer = lex()
lexer.input(user_input.upper())

for token in lexer:
	print(token)asz


def p_attack_command(p):
	'''
	attackCommand : VERB NOUN
	'''
	p[0] = ('VERB', p[1], 'NOUN', p[2])
	print(p[0])
	print('This is an ATTACK COMMAND!')


def p_move_command(p):
	'''
	moveCommand : VERB DIRECTION
	'''
	p[0] = ('VERB', p[1], 'DIRECTION', p[2])
	print(p[0])
	print('This is a MOVE COMMAND!')


def p_grab_command(p):
	'''
	grabCommand : VERB ARTICLE ITEM
	'''
	p[0] = ('VERB', p[1], 'ARTICLE', p[2], 'ITEM', p[3])
	print(p[0])
	print('This is a GRAB COMMAND!')


def p_drop_command(p):
	'''
	dropCommand : VERB NOUN
	'''
	p[0] = ('VERB', p[1], 'NOUN', p[2])
	print(p[0])
	print('This is a DROP COMMAND!')

parser = yacc()
output = parser.parse(user_input.upper())
