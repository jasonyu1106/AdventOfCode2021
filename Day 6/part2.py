class Population:
    def __init__(self):
        self.adult_fish = 0
        self.adult_fish_refresh = 0
        self.baby_fish = 0
        self.baby_fish_convert = 0


with open("fish_initial_state", "r") as f:
    initial_state = f.readline().split(",")

fish_states = [int(state) for state in initial_state]
init_pop = len(fish_states)

DAYS = 256

fish_pop = [Population() for i in range(DAYS+10)]
fish_pop[0].adult_fish = init_pop

# Initialize days when first baby fish spawn
for state in fish_states:
    fish_pop[state+1].adult_fish_refresh += 1

for i in range(1, DAYS+1):
    # Today's adult fish is yesterday's adult fish and new adult fish
    fish_pop[i].adult_fish += fish_pop[i-1].adult_fish + fish_pop[i].baby_fish_convert
    # Today's baby fish is yesterday's baby fish and new baby fish (net zero baby fish from baby to adult fish)
    fish_pop[i].baby_fish += fish_pop[i-1].baby_fish + fish_pop[i].adult_fish_refresh
    # After 9 days, baby fish (spawned from adult fish and new adult fish) convert to adult fish
    fish_pop[i + 9].baby_fish_convert += fish_pop[i].adult_fish_refresh + fish_pop[i].baby_fish_convert
    # Every 7 days, each adult fish spawns a baby fish.
    # After 7 days of adulthood, each new adult fish spawns a baby fish
    fish_pop[i + 7].adult_fish_refresh += fish_pop[i].adult_fish_refresh + fish_pop[i].baby_fish_convert

print(fish_pop[DAYS].adult_fish+fish_pop[DAYS].baby_fish)
