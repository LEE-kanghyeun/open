import numpy as np
import gym
env = gym.make('FrozenLake-v1', is_slippery=False)

########## value_iteration  ###########

def value_iteration(env):

    num_iterations = 2000
    threshold = 1e-20
    gamma = 0.99

    value_table = np.zeros(env.observation_space.n)  # [0, 0, 0, , ~~ , 0] 16개

    for i in range(num_iterations):
        
        updated_value_table = np.copy(value_table)
        # print(env.observation_space.n ,env.observation_space) # 출력 : 16, Discrete(16) // state 개수 조회
        for s in range(env.observation_space.n):  # 출력 : 16, Discrete(16) // state 개수 조회
            # print(s)
            Q_values = [sum([prob*(r + gamma * updated_value_table[s_]) 
                             for prob, s_, r, _ in env.P[s][a]]) # 출력 : [(1.0, 6, 0.0, False)] -> s state에서 a action을 취할때의 transition prob, next state, reward, 종료여부 출력됨
                                   for a in range(env.action_space.n)] # 가능한 액션 횟수를 조회, env.action_space.n -> 출력 : 4, 4가지의 action을 취할수 있음
            # print(env.P[s][1]) # 출력 : [(1.0, 6, 0.0, False)] -> transition prob, next state, reward, 종료여부 출력됨
            # print('Q_values:', Q_values) # 출력 : Q_values: [0.9702989999999999, 0.99, 0.0, 0.9702989999999999], action 0~3에 따른 값 value(리턴) 값 출력
            value_table[s] = max(Q_values) # action 중 최대 value값을 갖는 action에 대해 value_table에 저장, V(s) 지정

        if np.sum(np.fabs(updated_value_table - value_table)) <= threshold:
            break

    return value_table

def extract_policy(value_table):  # value table을 토대로 Q-Table을 다시 생성하여, Policy를 추출함.

    gamma = 0.99
    policy = np.zeros(env.observation_space.n)  # state 개수해 맞춰 policy용 list(array) 생성 ,  일단 0값으로 넣어둠
    for s in range(env.observation_space.n):

        Q_values = [sum([prob*(r + gamma * value_table[s_]) 
                             for prob, s_, r, _ in env.P[s][a]]) 
                                   for a in range(env.action_space.n)]
        # print('Q_values:', Q_values) # 출력 -> Q_values: [0.5435294117528799, 0.5435294117552107, 0.5435294117542429, 0.8152941176311668]

        policy[s] = np.argmax(np.array(Q_values)) # argmax를 통해 최대값을 갖게하는 action을 순서대로 저장 -> policy 생성됨
    
    return policy

def evaluate_policy(policy):
    num_episodes = 1000
    num_timesteps = 1000
    total_reward = 0
    total_timestep = 0
    success_episode = 0

    for i in range(num_episodes):
        state = env.reset()
        
        for t in range(num_timesteps):
            if policy is None:
                action = env.action_space.sample()  ## 임의 Actin을 랜덤하게 할당시킴 (지정된 policy가 없을때)
            else:
                # print(state, policy) # 출력 : (0, {'prob': 1}) ,  [1. 2. 1. 0. 1. 0. 1. 0. 2. 1. 1. 0. 0. 2. 2. 0.]
                action = policy[state[0]]
            new_state, reward, done, terminated , info = env.step(action)
            # print(new_state, reward, done, terminated , info)   # 출력 : 5, 0, True, False, {'prob': 1.0}
            # terminated : terminal state인지 아닌지,
            # done : episode가 끝났는지에 대한 불리언 값

            total_reward += reward

            if new_state == 15:
                print('now_iteration:', i)
                print('new_state:', new_state)
                print(new_state, reward, done, terminated , info)
                success_episode += 1

            if done:  # episode가 종료되었다면
                break

        total_timestep += t
    print('Number of success_episode:', success_episode)
    print("Number of successful episodes: %d / %d"%(total_reward, num_episodes))
    print("Average number of timesteps per episode: %.2f"%(total_timestep/num_episodes))

optimal_value_function = value_iteration(env) # value_iteration 실행
# print('value_table: ','\n', optimal_value_function)
## value_table 출력 ->  (각 16개 state 별 value
#  [0.95099005 0.96059601 0.970299   0.96059601 0.96059601 0.
#  0.9801     0.         0.970299   0.9801     0.99       0.
#  0.         0.99       1.         0.        ]

optimal_policy = extract_policy(optimal_value_function)
# print(optimal_policy)  # 출력 : [1. 2. 1. 0. 1. 0. 1. 0. 2. 1. 1. 0. 0. 2. 2. 0.]

evaluate_policy(None)
evaluate_policy(optimal_policy)







