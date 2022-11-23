from RL_ex010 import BanditTwoArmedHighLowFixed
import numpy as np


##### Epsilon-Greedy 방식 #####


env = BanditTwoArmedHighLowFixed()

count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2)

num_rounds = 100000

def epsilon_greedy(epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(Q)

for i in range(num_rounds):
    arm = epsilon_greedy(epsilon=0.5)
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm] += reward
    Q[arm] = sum_rewards[arm] / count[arm]

print(Q)          # [0.80153842 0.20013607]
print(count)      # [75012. 24988.]
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))  # The optimal arm is arm 1