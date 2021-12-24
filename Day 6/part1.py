with open("fish_initial_state.txt", "r") as f:
    initial_state = f.readline().split(",")

fish_states = [int(state) for state in initial_state]

DAYS = 80
for i in range(DAYS):
    new_fish = []
    for index, state in enumerate(fish_states):
        if state == 0:
            fish_states[index] = 6
            new_fish.append(8)
        else:
            fish_states[index] -= 1
    fish_states += new_fish

print(len(fish_states))

