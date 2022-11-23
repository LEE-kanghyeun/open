import gym
import pandas as pd
from tqdm import tqdm
env = gym.make('FrozenLake-v1')

def random_policy():
    return env.action_space.sample()

V = {}
for s in range(env.observation_space.n):   # Vaule table 생성 (그냥 0으로 채우기)
    V[s] = 0.0
# print('V : ', V) #출력  V :  {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0}

alpha = 0.1
gamma = 0.9

num_episodes = 10000
num_timesteps = 1000

for i in tqdm(range(num_episodes)):
    s, _ = env.reset()    # episode에서 한 Step씩 나아가다가 epsiode가 끝나서 재시작해야할 때, 초기 State를 리셋하고 반환한다.
    for t in range(num_timesteps):
        a = random_policy()          ## 임의 Actin을 랜덤하게 할당시킴 (지정된 policy가 없을때)
        s_, r, terminated, truncated, _ = env.step(a)  # s_ : next state
        V[s] += alpha * (r + gamma * V[s_] - V[s])    # TD update rule
        s = s_
        if terminated or truncated:
            break

#pd.set_option('display.float_format', lambda x: '%.3f'%x)
# print('V.items(): ', V.items())  # 출력 ->  V.items():  dict_items([(0, 0.0024369553312781887), (1, 0.004069398107868947), (2, 0.013906760991055514), (3, 0.004889940607636027), (4, 0.0022524453358898767), (5, 0.0), (6, 0.030441851164597463), (7, 0.0), (8, 0.005262112529968263), (9, 0.04177930281814457), (10, 0.14661308992966146), (11, 0.0), (12, 0.0), (13, 0.09053327156469114), (14, 0.4063544271232676), (15, 0.0)])
df = pd.DataFrame(list(V.items()), columns=['state', 'value'])
print(df)