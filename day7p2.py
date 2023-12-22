import collections

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
handStorage = {"High":[],"One":[],"Two":[],"Three":[],"Full":[],"Four":[],"Five":[]}
with open("Inputs/day7.txt") as file: pairs = dict([line.rstrip('\n').split(" ") for line in file])

def findBestHand(hand):
    
    if hand == "JJJJJ": #Stupid one case that breaks everything I hate it
        return 'Five'
    
    handNoJs = list(filter(('J').__ne__, hand))
    mostCommonNonJ = collections.Counter(handNoJs).most_common(1)[0][0]
    hand = hand.replace("J", mostCommonNonJ)

    possibleHands = ['High']
    for card in hand:
        match hand.count(card):
            case 5:
                possibleHands.append('Five')
                break
            case 4:
                possibleHands.append('Four')
                break
            case 3:
                possibleHands.append('Three')
            case 2:
                possibleHands.append('One')

                
    if 'One' in possibleHands: possibleHands.remove('One')
    if possibleHands.count('One') == 3:
        possibleHands = list(filter(('One').__ne__, possibleHands))
        possibleHands.append('Two')

    if 'Three' in possibleHands and 'One' in possibleHands:
        possibleHands.append('Full')
        
    possibleHands.sort(key = lambda i: list(handStorage).index(i), reverse=True)

    return possibleHands[0]

for hand in pairs:

    bestHand = findBestHand(hand)

    handStorage[bestHand].append(hand)


total = 0
multiplier = 1
for key in handStorage:
    handStorage[key].sort(key=lambda i: [cards.index(c) for c in i], reverse=True)
    for hand in handStorage[key]:
        print(key + "  " + str(multiplier) + "  " + hand + "  " + str(total) + "   J=" + collections.Counter(hand).most_common(1)[0][0])
        total += int(pairs[hand]) * multiplier
        multiplier += 1

print(total)