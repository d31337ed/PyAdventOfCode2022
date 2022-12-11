import requests

input_url = 'http://adventofcode.com/2022/day/1/input'
with open('sessionID.txt', 'r') as file:
    session_id = file.read().rstrip()

response = requests.get(input_url,
                        cookies={'session': session_id},
                        headers={'User-Agent': 'hohoho'}).text
response = response.rstrip(response[-1])


def find_fattest_elf(elves):
    elves = response.split('\n\n')
    calories = []
    for elf in elves:
        elf = list(filter(None, elf.split('\n')))
        calories_by_elf = sum([eval(fruit) for fruit in elf])

        calories.append(calories_by_elf)
    print(calories)
    return max(calories)


find_fattest_elf(response)

# print(find_fattest_elf(response))




