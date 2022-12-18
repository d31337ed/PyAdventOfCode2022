import requests

input_url = 'http://adventofcode.com/2022/day/2/input'
with open('sessionID.txt', 'r') as file:
    session_id = file.read().rstrip()

response = requests.get(input_url,
                        cookies={'session': session_id},
                        headers={'User-Agent': 'hohoho'}).text
response = response.rstrip(response[-1])


def outcome_score(turn1, turn2) -> int:
    turn_1_num = int(turn1)
    turn_2_num = int(turn2) - 23  # 26 - X position

    if turn_1_num > turn_2_num:
        return 6
    elif turn_1_num == turn_2_num:
        return 3
    else:
        return 0


def eval_round(turn1, turn2) -> int:
    score = int(turn2) + eval_round(turn1, turn2)
    return score


print(response)
