from ply.lex import lex
from ply.yacc import yacc

types = []
values = []
returnedValue = ""

# A pre-defined dictionary to distiguish nouns
nouns = {
	'door' : 'DOOR',
	'room' : 'ROOM',
	'sword' : 'SWORD',
	'potion' : 'POTION',
	'bag' : 'BAG',
	'torch' : 'TORCH',
	'ring' : 'RING',
	'mirror' : 'MIRROR',
	'key' : 'KEY',
	'scarf' : 'SCARF',
	'dagger' : 'DAGGER',
	'gauntlets' : 'GAUNTLETS',
	'knife' : 'KNIFE',
	'bracelet' : 'BRACELET',
	'shield' : 'SHIELD',
	'wand' : 'WAND'
}

# A pre-defined dictionary to distiguish articles
articles = {
	'a' : 'A',
	'an' : 'AN',
	'the' : 'THE'
}

# A pre-defined dictionary to distiguish words that deal with moving
moving = {
	'go' : 'GO',
	'head' : 'HEAD',
	'travel' : 'TRAVEL',
	'move' : 'MOVE',
	'enter' : 'ENTER',
	'leave' : 'LEAVE'
}

# A pre-defined dictionary to distiguish words that deal with attacking
attacking = {
	'kill' : 'KILL',
	'swing' : 'SWING',
	'stab' : 'STAB',
	'kick' : 'KICK',
	'punch' : 'PUNCH',
	'swipe' : 'SWIPE',
	'slice' : 'SLICE',
	'dice' : 'DICE',
	'shove' : 'SHOVE',
	'push' : 'PUSH',
	'headbutt' : 'HEADBUTT',
	'shoot' : 'SHOOT',
	'choke' : 'CHOKE',
	'strangle' : 'STRANGLE',
	'charge' : 'CHARGE',
	'impale' : 'IMPALE',
	'beat' : 'BEAT',
	'attack' : 'ATTACK'
}

# A pre-defined dictionary to distiguish words that deal with sneaking
sneaking = {
	'sneak' : 'SNEAK',
	'slither' : 'SLITHER',
	'sleuth' : 'SLEUTH',
	'seduce' : 'SEDUCE',
	'bribe' : 'BRIBE',
	'distract' : 'DISTRACT',
	'stealth' : 'STEALTH'
}

# A pre-defined dictionary to distiguish words that deal with grabbing
grabbing = {
	'grab' : 'GRAB',
	'seize' : 'SEIZE',
	'grasp' : 'GRASP',
	'snatch' : 'SNATCH',
}

# A pre-defined dictionary to distiguish words that deal with dropping
dropping = {
	'drop' : 'DROP',
	'relinquish' : 'RELINQUISH',
	'set' : 'SET',
	'place' : 'PLACE',
	'release' : 'RELEASE',
	'unhand' : 'UNHAND',
	'put' : 'PUT',
	'lay' : 'LAY'
}

# A pre-defined dictionary to distiguish words that deal with using
using = {
	'use' : 'USE',
	'utilize' : 'UTILIZE',
	'operate' : 'OPERATE',
	'apply' : 'APPLY',
	'wield' : 'WIELD',
	'open' : 'OPEN'
}

# A pre-defined dictionary to distiguish words that deal with directions
directions = {
	'north' : 'NORTH',
	'south' : 'SOUTH',
	'east' : 'EAST',
	'west' : 'WEST'
}

# A pre-defined dictionary to distiguish words that deal with adjectives
adjectives = {
	'golden' : 'GOLDEN',
	'enchanted' : 'ENCHANTED',
	'rusty' : 'RUSTY',
	'rickety' : 'RICKETY',
	'large' : 'LARGE',
	'small' : 'SMALL',
	'medium' : 'MEDIUM'
}

# List of Tokens used by the Lexer
tokens = [
	'WORD',
	'NOUN',
	'DIRECTION',
	'ARTICLE',
	'NPC',
	'ATTACKING',
	'MOVING',
	'ADJECTIVE',
	'SNEAKING',
	'GRABBING',
	'DROPPING',
	'USING'
]

# Define what a word is
def t_WORD(t):
	r'[a-zA-Z]+'
	t.value = str(t.value)
	if t.value in list(nouns.values()):
		t.type = nouns.get(t.value, 'NOUN') # Convert type from a word to a noun
	if t.value in list(directions.values()):
		t.type = directions.get(t.value, 'DIRECTION')  # Convert type from a word to a direction
	if t.value in list(articles.values()):
		t.type = articles.get(t.value, 'ARTICLE')  # Convert type from a word to an article
	if t.value in list(attacking.values()):
		t.type = attacking.get(t.value, 'ATTACKING')  # Convert type from a word to an attack command
	if t.value in list(moving.values()):
		t.type = moving.get(t.value, 'MOVING')  # Convert type from a word to a movement
	if t.value in list(adjectives.values()):
		t.type = adjectives.get(t.value, 'ADJECTIVE')  # Convert type from a word to an adjective
	if t.value in list(sneaking.values()):
		t.type = sneaking.get(t.value, 'SNEAKING')  # Convert type from a word to a sneak command
	if t.value in list(grabbing.values()):
		t.type = grabbing.get(t.value, 'GRABBING')  # Convert type from a word to a grab command
	if t.value in list(dropping.values()):
		t.type = dropping.get(t.value, 'DROPPING')  # Convert type from a word to a drop command
	if t.value in list(using.values()):
		t.type = using.get(t.value, 'USING')  # Convert type from a word to a use command
	return t

def t_error(t):
	print(f'Illegal character: {t.value[0]!r}')
	t.lexer.skip(1)

# Ignore whitespace
t_ignore = ' '

user_input = input()
lexer = lex()
lexer.input(user_input.upper())

for token in lexer:
	print(token)
	values.append(token.value) # Append token value to a usable list
	types.append(token.type) # Append token type to a usable list

def p_action(p):
	'''
	command : fuller NOUN
			| fuller NPC
			| command DIRECTION
			| fuller WORD
	'''
	p[0] = p[2]

def p_fuller(p):
	'''
	fuller : full WORD
		   | full ADJECTIVE
		   | full ARTICLE
	'''
	p[0] = p[2]

def p_full(p):
	'''
	full : command WORD
		 | command ADJECTIVE
		 | command ARTICLE
	'''
	p[0] = p[2]

# Use command
def p_use(p):
	'''
	command : USING
	'''
	p[0] = {"USE", p[1]}
	global returnedValue
	returnedValue = "USE"

# Grab command
def p_grab(p):
	'''
	command : GRABBING
	'''
	p[0] = {"GRAB", p[1]}
	global returnedValue
	returnedValue = "GRAB"

# Drop command
def p_drop(p):
	'''
	command : DROPPING
	'''
	p[0] = {"DROP", p[1]}
	global returnedValue
	returnedValue = "DROP"

# Sneak command
def p_sneak(p):
	'''
	command : SNEAKING
	'''
	p[0] = {"SNEAK", p[1]}
	global returnedValue
	returnedValue = "SNEAK"

# Attack command
def p_attack(p):
	'''
	command : ATTACKING
	'''
	p[0] = {"ATTACK", p[1]}
	global returnedValue
	returnedValue = "ATTACK"

# Move command
def p_move(p):
	'''
	command : MOVING
	'''
	p[0] = {"MOVE", p[1]}
	global returnedValue
	returnedValue = "MOVE"

def p_error(p):
    return

output = yacc().parse(user_input.upper())

def main():
	return returnedValue

if __name__ == '__main__':
	main()
