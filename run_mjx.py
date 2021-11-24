import sys
import mjx
from mjx.agent import TsumogiriAgent, ShantenAgent


N = int(sys.argv[1])
agent_type = sys.argv[2]

if agent_type == "tsumogiri":
    agents = {
        "player_0": TsumogiriAgent(),
        "player_1": TsumogiriAgent(),
        "player_2": TsumogiriAgent(),
        "player_3": TsumogiriAgent(),
    }
else:
    agents = {
        "player_0": ShantenAgent(),
        "player_1": ShantenAgent(),
        "player_2": ShantenAgent(),
        "player_3": ShantenAgent(),
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
