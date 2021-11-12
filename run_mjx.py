import sys
import mjx
from mjx.agent import RandomAgent

N = int(sys.argv[1])

agents = {
    "player_0": RandomAgent(),
    "player_1": RandomAgent(),
    "player_2": RandomAgent(),
    "player_3": RandomAgent(),
}
env = mjx.MjxEnv()
for i in range(N):
    obs_dict = env.reset()
    while not env.done():
        action_dict = {player_id: agents[player_id].act(obs)
                       for player_id, obs in obs_dict.items()}
        obs_dict = env.step(action_dict)
    rewards = env.rewards()

# time python3 -O speed_benchmark.py
# python3 -O speed_benchmark.py  81.44s user 0.86s system 101% cpu 1:21.42 total
# 0.08144 sec/game
