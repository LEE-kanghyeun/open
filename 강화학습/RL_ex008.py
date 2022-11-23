import numpy as np
import gym
env = gym.make('FrozenLake-v1')
from tqdm import tqdm

######### TD Control : SARSA ########


def action_epsilon_greedy(q, s, epsilon=0.05):
    if np.random.rand() > epsilon:
        return np.argmax(q[s])
    return np.random.randint(4)

def evaluate_policy(q, n=500):
    acc_returns = 0
    for i in range(n):
        terminated = False
        truncated = False
        s, _ = env.reset()
        while not (terminated or truncated):
            a = action_epsilon_greedy(q, s, epsilon=0.)  # epsilon=0. 이므로 greedy하게
            s, reward, terminated, truncated, _ = env.step(a)
            acc_returns += reward
    return acc_returns / n

def sarsa(alpha=0.02, gamma=1., epsilon=0.05, q=None, env=env):
    
    if q is None:
        q = np.zeros((16,4)).astype(np.float32)   # q table 없으면 0값으로 채워넣음

    nb_episodes = 100000
    steps = 2000
    progress = []
    for i in tqdm(range(nb_episodes)):
        terminated = False
        truncated = False
        s, _ = env.reset()
        a = action_epsilon_greedy(q, s, epsilon=epsilon)  # Q테이블과 현재 state을 적용하여 epsilon_greedy policy로 현재 state의 action을 선택
        while not (terminated or truncated):  # 에피소드가 종료되지 않았다면, 루프(step) 지속됨
            new_s, reward, terminated, truncated, _ = env.step(a)
            new_a = action_epsilon_greedy(q, new_s, epsilon=epsilon)   # Q테이블과 다음 state을 적용하여 epsilon_greedy policy로 다음 state의 action을 선택
            q[s,a] = q[s,a] + alpha * (reward + gamma * q[new_s,new_a] - q[s,a])   # 공식 적용
            s = new_s
            a = new_a   ## (현재 state, action)을 업데이트하기 위해 epsilon_greedy policy로 선택한 next state에서의 action을 그대로 다음 step에서 적용함 (on-policy)

        if i%steps == 0:
            progress.append(evaluate_policy(q, n=500))

    return q, progress

q, progress = sarsa(alpha=0.02, epsilon=0.05, gamma=0.999)

print('evaluate_policy(q, n=10000):  ', evaluate_policy(q, n=10000))  # 출력 : evaluate_policy(q, n=10000):   0.7379
print('progress: ', progress)    # 출력 : progress:  [0.0, 0.0, 0.0, 0.0, 0.258, 0.722, 0.712, 0.716, 0.668, 0.688, 0.698, 0.71, 0.746, 0.736, 0.734, 0.728, 0.734, 0.72, 0.748, 0.776, 0.704, 0.742, 0.76, 0.778, 0.74, 0.72, 0.738, 0.692, 0.754, 0.724, 0.734, 0.724, 0.754, 0.718, 0.728, 0.684, 0.736, 0.74, 0.762, 0.738, 0.73, 0.734, 0.742, 0.734, 0.702, 0.732, 0.728, 0.722, 0.756, 0.724]

print('Q:', q)
# Q: [[0.5409103  0.5212513  0.52212614 0.5207516 ]
#  [0.32719818 0.28225318 0.26329356 0.4706359 ]
#  [0.40607736 0.28713128 0.28344145 0.34355846]
#  [0.18739237 0.03672693 0.01511011 0.02773778]
#  [0.5496462  0.3867717  0.42977637 0.33193833]
#  [0.         0.         0.         0.        ]
#  [0.31840268 0.18518308 0.25953874 0.1285109 ]
#  [0.         0.         0.         0.        ]
#  [0.38484418 0.40890798 0.41068035 0.5757267 ]
#  [0.46454424 0.63271517 0.43037492 0.38454133]
#  [0.6008966  0.4823743  0.36863008 0.33328828]
#  [0.         0.         0.         0.        ]
#  [0.         0.         0.         0.        ]
#  [0.45586377 0.49212265 0.7555321  0.48373687]
#  [0.72621876 0.84593636 0.8065562  0.7630749 ]
#  [0.         0.         0.         0.        ]]