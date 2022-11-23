import sys
import gym
import numpy as np
from collections import defaultdict
from tqdm import tqdm
env = gym.make('Blackjack-v1')

############# monte carlo  <Contoral - OFF Policy> ############


def random_policy(nA):              ## 랜덤 POLICY 생성  (Behavior policy 생성)
    A = np.ones(nA, dtype=float) / nA  ## action을 실행할 확률을 공평하게 1/n씩 지정함. , hit/stand로 0.5/0.5
    def policy_fn(observation):
        # print(A)   # 출력 : [0.5 0.5]
        return A
    return policy_fn

def greedy_policy(Q):  ## Q테이블에서 리턴값이 큰 action을 선택하도록 함
    print(Q)
    def policy_fn(state):
        A = np.zeros_like(Q[state], dtype=float)  # 괄호안의 형태(리스트, 튜플 등) 그대로 0만 채워 출력함,
                                                  # print(np.zeros_like((2,3,3,10), dtype=float)) => (0,0,0,0)
        # print(Q[state])    # 출력 : [-0.05882353  0.06666667] or [- 0.38888889 -1.        ] or ~~
        best_action = np.argmax(Q[state])
        A[best_action] = 1.0                     # 확률값에 1을 부여
        return A
    return policy_fn

def mc_off_policy(env, num_episodes, behavior_policy, max_time=100, discount_factor=1.0):
    Q = defaultdict(lambda:np.zeros(env.action_space.n))
    C = defaultdict(lambda:np.zeros(env.action_space.n))  # C값은 처음에 0으로 시작
    # print(env.action_space.n)  # 출력 : 2
    # print(np.zeros(env.action_space.n))  # 출력 : [0. 0.]
    # print(Q)  # : 출력 -> defaultdict(<function mc_off_policy.<locals>.<lambda> at 0x0000021BE81EBD30>, {})

    target_policy = greedy_policy(Q)

    for i_episode in range(1, num_episodes+1):
        if i_episode % 1000 == 0:
            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
            sys.stdout.flush()

        episode = []
        state = env.reset()
        state = state[0]
        for t in range(max_time):  ## behavior policy에 따라 에피소드를 생성하고, 정보를 episode에 저장함
            probs = behavior_policy(state)  ## behavior_policy :  'random_policy' 함수에서 생성된 random policy
            # print(probs)  # 출력 -> [0.5 0.5]
            action = np.random.choice(np.arange(len(probs)), p=probs) # probs에서 주어진 확률대로 action을 random choice함
            next_state, reward, done, terminated , info  = env.step(action)
            episode.append((state, action, reward))
            if done:
                break
            state = next_state

        G = 0.0  # 각 (state, action)에 대한 리턴값 (에피소드 최종스텝부터 시작하여 최초스텝으로 이동하며, G = discount_factor * G + reward 계산을 통해 업데이트됨)
        W = 1.0  # WEIGHTED IMPORTANCE SAMPLING RATIO, 초기값은 1로 시작
                 # behavior와 target policy 모두 에피소드 종료를 일으키는 (STATE, ACTION)은 그 다음 ACTION이 종료밖에 없으므로 behavior와 target policy의 policy 비율이 마지막 스텝에는 같다고 할수 있다.
        for t in range(len(episode))[::-1]:  # step에 대해 거꾸로 계산함 (최종 스텝부터 계산) => 계산량 줄이기 위해
            state, action, reward = episode[t]
            G = discount_factor * G + reward    # 이 예제에서는 discount_factor를 1로 지정, 필요시 0~1사이로 변경
            C[state][action] += W               # C[state][action]에서의 C에 대해  C_1 = W_1,  C_2 = W_1 + W_2,  C_3 = ~
            Q[state][action] += (W / C[state][action]) * (G - Q[state][action])  # 공식 적용하여 Q-table(Q[state][action])업데이트
            if action != np.argmax(target_policy(state)): # behavior의 acion과 target policy의 action이 같을때만, W를 갱신하도록함
                break                                     # 만일, action이 다르다면 for문 탈출 -> next episode 실행
            W = W * 1./behavior_policy(state)[action]  # WEIGHTED IMPORTANCE SAMPLING UPDATE, W = W / b(a/s)
                                                       # Target policy의 확률은 1이다. (action을 argmax로 뽑았으므로)
            # print('behavior_policy(state)[action]: ', behavior_policy(state)[action])   # 출력 : behavior_policy(state)[action]:  0.5

    return Q, target_policy

def evaluate_policy(env, policy):
    num_episodes = 5000
    num_timesteps = 100
    num_wins = 0
    num_draws = 0
    num_losses = 0
    num_total = 0
    for i in tqdm(range(num_episodes)):
        state = env.reset()
        state = state[0]
        for t in range(num_timesteps):
            action = np.argmax(policy(state))
            next_state, reward, done, terminated , info = env.step(action)
            if done:
                if reward == 1:
                    num_wins += 1
                elif reward == 0:
                    num_draws += 1
                elif reward == -1:
                    num_losses += 1
                num_total += 1
                break
            state = next_state

    print("wins: %d (%.2f%%), draws: %d (%.2f%%), losses: %d (%.2f%%)"%(num_wins, num_wins/num_total*100, num_draws, num_draws/num_total*100, num_losses, num_losses/num_total*100))

random_policy = random_policy(env.action_space.n)
# print(random_policy)  # 출력 : defaultdict(<function mc_off_policy.<locals>.<lambda> at 0x0000021BE81EBD30>, {})
Q, policy = mc_off_policy(env, num_episodes=5000, behavior_policy=random_policy)  ## 마구잡이로 선택된(랜덤 확률로 선택된) policy를 behavior_policy로 입력
evaluate_policy(env, policy)
