from RL_ex010 import BanditTwoArmedHighLowFixed
import numpy as np


##### Soft Max 방식 #####

env = BanditTwoArmedHighLowFixed()

# the table
count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2)

def softmax(T):
    denom = sum([np.exp(i/T) for i in Q])
    probs = [np.exp(i/T)/denom for i in Q]  # Soft max가 적용된 획률 (Q값을 softmax에 적용)
    arm = np.random.choice(env.action_space.n, p=probs)
    return arm        ## Soft max의 확률대로 Arm이 선택되어져서 출력됨

num_rounds = 100000
T = 50
for i in range(num_rounds):
    arm = softmax(T)  ## Soft max의 확률대로 Arm이 선택되어져서 출력됨
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm] += reward
    Q[arm] = sum_rewards[arm] / count[arm]
    T = T * 0.9999   ## Step(Round)이 진행될수록 T값을 줄인다.

print(Q)      # [0.80159316 0.19711404]
print(count)  # [78586. 21414.]
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))

