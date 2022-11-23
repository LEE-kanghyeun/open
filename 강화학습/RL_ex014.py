from RL_ex010 import BanditTwoArmedHighLowFixed
import numpy as np

#####  Thomson Sampling  #####

np.set_printoptions(suppress = True)   ### 소수점 모두 출력하게하는 옵션
env = BanditTwoArmedHighLowFixed()

count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2)
alpha = np.ones(2)
beta = np.ones(2)

def thompson_sampling(alpha, beta):  ###  Thomson Sampling 하여  선택된 arm을 출력하는 함수
    samples = [np.random.beta(alpha[i]+1, beta[i]+1) for i in range(2)]   ###  베타 분포에서 값을 1개씩 랜덤하게 뽑음, 리스트 원소로 넣음
    # print(samples)    # 출력 :  [0.8011545886670516, 0.09990572262485706]
    return np.argmax(samples)    # 값이 큰 arm을 출력함

num_rounds = 100000
for i in range(num_rounds):
    arm = thompson_sampling(alpha,beta)    
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm] += reward
    Q[arm] = sum_rewards[arm] / count[arm]
    if reward == 1:
        alpha[arm] = alpha[arm] + 1  ## 이기면 해당 arm의 알파값 상승
    else:
        beta[arm] = beta[arm] + 1    ## 지면 해당 arm의 베타값 상승

print(count)  # [99993.     7.]
print(Q)      # [0.80038004 0.2       ]
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))