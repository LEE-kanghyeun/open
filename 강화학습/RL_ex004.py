import gym
import pandas as pd
from collections import defaultdict
from tqdm import tqdm

############# monte carlo  <Prediction> ############

env = gym.make('Blackjack-v1')
num_timesteps = 100

def policy(state):
    # print(state) # 출력 : ((6, 5, False), {})
    # state : ( my sum, dealer's sum, Ace 카드 여부) , {}  ???
    return 0 if state[0] >= 17 else 1  # policy : 현재 state에서 내 sum 값이 17보다 크거나 같으면, 0(stand/stop) 하고,  작으면 1(ghit/go) 한다.



def generate_episode(policy):
    episode = []
    state = env.reset() # 리셋후 시작은 랜덤하게 state를 생성
    # print('c_state:,',state)   #출력 -> c_state:, ((18, 6, False), {})
    state = state[0]
    for t in range(num_timesteps): # num_timesteps = 100, 최대 step을 100번 진행함
        action = policy(state)  # policy 함수에서의 조건에 따라, action을 취함 (hit or stand) -> prediction이므로 policy는 고정임.
        # next_state, reward, done, info = env.step(action)
        # print(next_state, reward, done, info)
        next_state, reward,  done, terminated , info = env.step(action)
        # print(next_state, reward,  done, terminated , info)
        # print('next:',next_state)
        episode.append((state, action, reward))

        if done:   # episode가 종료될때까지 for문을 통해 step을 진행
            break
        state = next_state
    # print('episode:', episode) # episode: [((16, 6, False), 1, 0.0), ((19, 6, False), 0, 1.0)]  => 이긴 경우
                               # episode: [((13, 1, True), 1, 0.0), ((13, 1, False), 1, 0.0), ((15, 1, False), 1, 0.0), ((17, 1, False), 0, -1.0)]  => 진 경우
                               # episode: [((7, 6, False), 1, 0.0), ((18, 6, True), 0, 0.0)]  => 비긴 경우
    return episode

total_return = defaultdict(float)  # dictionary 값을 기본 0.0으로 세팅
N = defaultdict(int)  # dictionary 값을 기본 0으로 세팅

num_iterations = 50000
for i in tqdm(range(num_iterations)):    # Progress 진행바 설정
    episode = generate_episode(policy)   # episode.append((state, action, reward)) -> (state, action, reward)의 정보를 담고 있는 리스트
    states, actions, rewards = zip(*episode)  # 각 에피소드에 저장된 (state, action, reward)를 각각의 리스트로 풀어냄
    # print(states)  # 출력 -> ((12, 2, False), (14, 2, False), (15, 2, False)) 한 에피소드에서의 state의 변화를 차례대로 출력함.

    for t, state in enumerate(states): # step에 따른 state의 변화를 차례로 꺼냄.
        # if state not in states[0:t]:  # first visit일때 해당 코드 추가(한줄만 추가하면 됨)
        R = (sum(rewards[t:]))  ## 각 State 별로 적용할 Return 값을 계산 V(S0) = rewards[0:], V(S1) = rewards[1:], V(S2) = rewards[2:]
        total_return[state] = total_return[state] + R  # 각 state ( my sum, dealer's sum, Ace 카드 여부)에 해당되는 리턴값을 더해줌
                                                       # (every visit이면 나중에 방문한 횟수로 나눠줌, first visit이면 첫번째만 방문한 값만 합산함)
        N[state] = N[state] + 1  # 해당 state에 대해 방문한 횟수 카운트

# print(total_return.items())  # 출력 -> dict_items([((21, 10, True), 63.0), ((14, 10, False), -102.0), ((12, 2, False), -16.0), ((19, 6, True), 5.0), ((15, 10, False), -110.0), ((17, 10, False), -84.0), ((13, 10, False), -70.0), ((20, 10, False), 113.0), ((19, 1, False), -10.0), ((18, 10, False), -28.0), ((16, 7, False), -22.0), ((10, 3, False), 8.0), ((19, 3, False), 16.0), ((20, 9, False), 39.0), ((20, 10, True), 16.0), ((5, 2, False), 0.0), ((10, 2, False), 9.0), ((19, 2, False), 8.0), ((21, 1, True), 8.0), ((21, 9, True), 26.0), ((12, 1, False), -24.0), ((12, 10, False), -77.0), ((16, 10, False), -127.0), ((21, 2, True), 18.0), ((18, 4, True), 1.0), ((13, 10, True), -3.0), ((18, 10, True), -3.0), ((8, 9, False), -1.0), ((19, 9, True), 1.0), ((16, 6, False), -28.0), ((17, 5, False), 4.0), ((19, 4, False), 13.0), ((14, 9, False), -28.0), ((14, 3, False), -18.0), ((9, 4, False), 1.0), ((15, 4, False), -21.0), ((21, 4, False), 17.0), ((8, 2, False), -5.0), ((18, 2, False), 3.0), ((20, 4, False), 41.0), ((12, 7, False), -3.0), ((13, 9, False), -24.0), ((16, 9, False), -32.0), ((16, 2, False), -18.0), ((15, 1, False), -20.0), ((6, 10, False), -5.0), ((20, 2, False), 27.0), ((17, 8, False), -20.0), ((9, 10, False), -10.0), ((11, 10, False), 8.0), ((21, 10, False), 94.0), ((17, 8, True), -4.0), ((19, 10, False), -11.0), ((14, 8, False), -19.0), ((21, 8, False), 24.0), ((18, 6, False), 15.0), ((8, 10, False), -21.0), ((12, 6, False), -12.0), ((19, 6, False), 14.0), ((7, 7, False), -1.0), ((15, 7, False), -19.0), ((10, 9, False), 1.0), ((17, 7, False), -6.0), ((12, 3, False), -14.0), ((7, 10, False), -9.0), ((20, 3, False), 38.0), ((15, 5, False), -26.0), ((15, 6, False), -23.0), ((20, 6, False), 40.0), ((16, 1, False), -29.0), ((11, 8, False), 4.0), ((16, 8, False), -29.0), ((13, 5, False), -13.0), ((8, 1, False), -7.0), ((18, 1, False), -12.0), ((16, 5, False), -25.0), ((12, 9, False), -22.0), ((16, 4, False), -27.0), ((18, 1, True), -2.0), ((18, 5, False), -5.0), ((17, 3, False), -1.0), ((17, 1, False), -24.0), ((20, 7, False), 43.0), ((15, 9, False), -28.0), ((21, 4, True), 19.0), ((8, 3, False), 4.0), ((13, 3, False), -7.0), ((9, 1, False), -6.0), ((10, 5, False), 5.0), ((5, 9, False), 0.0), ((18, 7, False), 19.0), ((15, 10, True), -8.0), ((16, 10, True), -5.0), ((13, 2, False), -14.0), ((21, 2, False), 20.0), ((9, 7, False), 2.0), ((18, 9, True), 2.0), ((13, 1, False), -29.0), ((16, 2, True), -4.0), ((17, 2, True), -3.0), ((18, 9, False), -7.0), ((17, 4, False), -5.0), ((5, 10, False), -14.0), ((21, 6, False), 17.0), ((11, 9, False), 8.0), ((19, 9, False), 3.0), ((14, 1, False), -14.0), ((12, 4, False), -21.0), ((13, 4, False), -23.0), ((20, 5, False), 47.0), ((17, 1, True), -6.0), ((17, 10, True), -8.0), ((13, 4, True), 2.0), ((20, 4, True), 5.0), ((8, 4, False), -2.0), ((11, 4, False), 3.0), ((14, 4, False), -23.0), ((21, 7, True), 33.0), ((17, 6, True), 2.0), ((11, 1, False), -9.0), ((15, 2, False), -24.0), ((10, 8, False), 5.0), ((20, 8, False), 61.0), ((21, 9, False), 27.0), ((10, 6, False), 7.0), ((14, 6, False), -21.0), ((20, 1, False), 3.0), ((16, 9, True), 0.0), ((14, 2, True), 1.0), ((14, 2, False), -21.0), ((9, 8, False), 1.0), ((19, 8, False), 22.0), ((14, 7, True), 5.0), ((19, 7, True), 6.0), ((19, 7, False), 27.0), ((10, 10, False), -10.0), ((21, 1, False), 18.0), ((11, 7, False), -1.0), ((15, 3, False), -11.0), ((17, 2, False), -1.0), ((16, 3, False), -28.0), ((8, 6, False), 0.0), ((16, 6, True), -3.0), ((18, 4, False), 2.0), ((20, 1, True), 4.0), ((17, 9, False), -18.0), ((6, 7, False), -2.0), ((14, 6, True), 0.0), ((20, 3, True), 3.0), ((21, 8, True), 25.0), ((12, 3, True), -1.0), ((13, 3, True), 1.0), ((18, 3, True), 2.0), ((14, 5, True), -1.0), ((15, 5, True), 4.0), ((14, 5, False), -19.0), ((20, 7, True), 6.0), ((14, 7, False), -16.0), ((18, 3, False), 0.0), ((12, 5, False), -8.0), ((15, 8, True), -4.0), ((16, 8, True), 0.0), ((18, 8, False), 1.0), ((9, 6, False), 3.0), ((17, 3, True), -1.0), ((6, 4, False), -8.0), ((12, 8, False), -20.0), ((6, 8, False), -1.0), ((9, 3, False), 0.0), ((8, 7, False), 2.0), ((9, 9, False), -2.0), ((20, 9, True), 7.0), ((13, 8, False), -18.0), ((14, 8, True), -2.0), ((20, 6, True), 6.0), ((7, 1, False), -3.0), ((4, 10, False), -2.0), ((13, 7, False), 1.0), ((11, 6, False), 9.0), ((16, 1, True), 4.0), ((19, 10, True), -7.0), ((6, 5, False), -2.0), ((8, 5, False), -1.0), ((8, 8, False), 0.0), ((19, 8, True), 4.0), ((13, 7, True), 1.0), ((13, 6, False), -8.0), ((20, 2, True), 1.0), ((14, 10, True), -5.0), ((17, 6, False), 14.0), ((11, 2, False), 5.0), ((21, 6, True), 23.0), ((13, 8, True), 4.0), ((18, 8, True), 0.0), ((7, 6, False), 3.0), ((7, 5, False), 4.0), ((18, 5, True), 4.0), ((19, 5, False), 22.0), ((11, 5, False), 9.0), ((21, 5, False), 28.0), ((21, 7, False), 15.0), ((9, 5, False), 3.0), ((15, 3, True), 5.0), ((19, 2, True), 4.0), ((7, 2, False), 3.0), ((19, 3, True), 3.0), ((10, 1, False), -4.0), ((11, 3, False), 2.0), ((21, 3, False), 23.0), ((21, 3, True), 16.0), ((12, 10, True), -1.0), ((12, 7, True), 3.0), ((18, 7, True), 3.0), ((7, 8, False), 5.0), ((15, 8, False), -27.0), ((20, 8, True), 2.0), ((16, 3, True), -2.0), ((18, 6, True), 3.0), ((20, 5, True), 11.0), ((13, 6, True), 0.0), ((4, 8, False), 2.0), ((14, 1, True), -2.0), ((16, 5, True), 1.0), ((14, 9, True), -5.0), ((10, 4, False), 9.0), ((6, 3, False), 2.0), ((4, 4, False), 0.0), ((15, 4, True), 0.0), ((14, 4, True), 3.0), ((10, 7, False), 7.0), ((16, 4, True), 3.0), ((19, 4, True), 7.0), ((12, 4, True), 2.0), ((6, 2, False), 3.0), ((5, 8, False), 2.0), ((6, 6, False), -5.0), ((5, 4, False), 3.0), ((13, 5, True), 2.0), ((21, 5, True), 22.0), ((5, 7, False), -4.0), ((12, 1, True), 0.0), ((13, 1, True), 0.0), ((7, 9, False), -1.0), ((12, 6, True), 0.0), ((7, 4, False), 1.0), ((5, 6, False), -1.0), ((7, 3, False), 0.0), ((5, 5, False), 0.0), ((17, 5, True), -5.0), ((13, 2, True), -1.0), ((15, 2, True), 1.0), ((6, 1, False), -5.0), ((5, 1, False), -6.0), ((17, 7, True), 4.0), ((15, 9, True), -5.0), ((17, 9, True), -2.0), ((15, 6, True), -2.0), ((9, 2, False), -2.0), ((6, 9, False), 0.0), ((15, 7, True), 4.0), ((4, 9, False), 2.0), ((19, 5, True), 4.0), ((19, 1, True), 1.0), ((4, 6, False), -1.0), ((12, 2, True), 1.0), ((14, 3, True), -1.0), ((18, 2, True), 1.0), ((4, 2, False), -1.0), ((4, 1, False), 0.0), ((15, 1, True), -2.0), ((12, 5, True), 0.0), ((17, 4, True), 0.0), ((16, 7, True), 0.0), ((13, 9, True), 1.0), ((5, 3, False), -3.0), ((12, 8, True), 1.0), ((12, 9, True), 1.0), ((4, 7, False), 2.0), ((4, 5, False), 1.0), ((4, 3, False), 3.0)])
total_return = pd.DataFrame(total_return.items(), columns=['state', 'total_return'])

N = pd.DataFrame(N.items(), columns=['state', 'N'])
df = pd.merge(total_return, N, on='state')
df['value'] = df['total_return'] / df['N']  ## 각 STATE마다 방문한 횟수로 나눠줌  => V(s)
#print(df.head(10))
#print(df[df['state']==(21,9,False)]['value'])
print(df)                     ## V(s) 테이블  (state 별 value)
print(sum(df['total_return'].values))  ## 모든 시행(에피소드)에서 얻은 Return 값
