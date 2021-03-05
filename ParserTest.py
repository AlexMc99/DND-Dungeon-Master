from ply.lex import lex
from ply.yacc import yacc

# A pre-defined dictionary to distiguish nouns
nouns = {
	'dragon' : 'DRAGON',
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
	'grab' : 'GRAB',
	'drop' : 'DROP'
}

directions = {
	'north' : 'NORTH',
	'south' : 'SOUTH',
	'east' : 'EAST',
	'west' : 'WEST'
}

npcs = {
	'goblin' : 'GOBLIN',
	'princess' : 'PRINCESS',
}

objects = {
	'sword' : 'SWORD',
	'potion' : 'POTION'
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
	'ARTICLE',
	'NPC',
	'OBJECT'
] + list(nouns.values()) + list(verbs.values()) + list(directions.values()) + list(articles.values()) + list(npcs.values()) + list(objects.values())

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
		t.type = articles.get(t.value, 'ARTICLE')
	if t.value in list(npcs.values()):
		t.type = npcs.get(t.value, 'NPC')
	if t.value in list(objects.values()):
		t.type = objects.get(t.value, 'OBJECT')
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

def p_command(p):
	'''
	command : VERB ARTICLE
			| VERB WORD ARTICLE
	'''
	if p[2] == 'TO':
		p[0] = ('VERB', p[1], 'WORD', p[2], 'ARTICLE', p[3])

	elif p[2] == 'THE':
		p[0] = ('VERB', p[1], 'ARTICLE', p[2])

	print(p[0])

def p_moveCommand(p):
	'''
	moveCommand : command DIRECTION
	'''
	p[0] = ('COMMAND', p[1], 'DIRECTION', p[2])
	print("This is a MOVE COMMAND")

def p_attackCommand(p):
	'''
	attackCommand : command NPC
	'''
	p[0] = ('COMMAND', p[1], 'NPC', p[2])
	print("This is an ATTACK COMMAND")

def p_itemCommand(p):
	'''
	itemCommand : command OBJECT
	'''
	p[0] = ('COMMAND', p[1], 'OBJECT', p[2])

	if p[1][1] == 'DROP':
		print("This is a DROP COMMAND")

	elif p[1][1] == 'GRAB':
		print("This is a GRAB COMMAND")

parser = yacc()
output = parser.parse(user_input.upper())
