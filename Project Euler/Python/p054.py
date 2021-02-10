RANKS = "23456789TJQKA"
SUITS = "SHCD"

with open('p054_poker.txt', 'r') as f:
	hands = f.readlines()

hands = [i.replace('\n','') for i in hands]


def player1_win(handpair):
	cards = [parse_card(i) for i in handpair.split(" ")]

	p1 = cards[:5]
	p2 = cards[5:]

	return count_score(p1) > count_score(p2)


def count_score(hand):

	ranks_count = [sum(1 for (rank, _) in hand if rank == i) for i in range(13)]
	ranks_count_hist = [ranks_count.count(i) for i in range(6)]

	min_suit = min(suit for (_, suit) in hand)
	max_suit = max(suit for (_, suit) in hand)
	flush_suit = min_suit if min_suit == max_suit else -1

	best_cards = get_5_frequent_highest_cards(ranks_count, ranks_count_hist)
	straight_high_rank = get_straight_high_rank(ranks_count)

	if straight_high_rank != -1 and flush_suit != -1:
		return 8 << 20 | straight_high_rank  	# Straight flush
	elif ranks_count_hist[4] == 1:
		return 7 << 20 | best_cards 			# Four of a kind
	elif ranks_count_hist[3] == 1 and ranks_count_hist[2] == 1:
		return 6 << 20 | best_cards 			# Full house
	elif flush_suit != -1:
		return 5 << 20 | best_cards  			# Flush
	elif straight_high_rank != -1:
		return 4 << 20 | straight_high_rank  	# Straight
	elif ranks_count_hist[3] == 1:
		return 3 << 20 | best_cards   			# Tree of a kind
	elif ranks_count_hist[2] == 2:
		return 2 << 20 | best_cards  			# Two pairs
	elif ranks_count_hist[2] == 1:
		return 1 << 20 | best_cards  			# One pair
	else:
		return 0 << 20 | best_cards  			# High card


def get_5_frequent_highest_cards(ranks, ranks_hist):
	result = 0
	count = 0

	for i in reversed(range(len(ranks_hist))):
		for j in reversed(range(len(ranks))):
			if ranks[j] == i:
				for k in range(i):
					if count >= 5:
						break
					result = result << 4 | j
					count += 1

	if count != 5:
		raise ValueError()
	return result


def get_straight_high_rank(ranks):
	for i in reversed(range(3, len(ranks))):
		for j in range(5):
			if ranks[(i-j+13) % 13] == 0:
				break
		else:
			return i
	return -1


def parse_card(card):
	return (RANKS.index(card[0]), SUITS.index(card[1]))


answer = sum(1 for handpair in hands if player1_win(handpair))
print(answer)

