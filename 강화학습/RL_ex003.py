import numpy as np
import gym
env = gym.make("FrozenLake-v1")

########## policy_iteration  ###########

def compute_value_function(policy):

    num_iterations = 1000
    threshold = 1e-20
    gamma = 1.0
    
    value_table = np.zeros(env.observation_space.n) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

    for i in range(num_iterations):
        updated_value_table = np.copy(value_table)

        for s in range(env.observation_space.n):
            a = policy[s]                         # 주어진 policy대로 action이 지정되어 있음.

            value_table[s] = sum(
                [prob * (r + gamma * updated_value_table[s_])
                    for prob, s_, r, _ in env.P[s][a]]) # env.P[15][0]] 출력 -> [(1.0, 15, 0, True)], [(transition prob, Next_state, Reward, is_Terminal?)]
                                                        # value iteration은 여기서 for문 2개 필요하나, policy iteration은 action이 지정되어있으므로 1개만 필요
        if np.sum(np.fabs(updated_value_table - value_table)) <= threshold:
            break

    return value_table

def extract_policy(value_table):  # converged된 value_table을 기반으로 Q tabled을 만들고 policy를 추출,
                                  # value iteration에서의 extract_policy 함수와 동일
    gamma = 0.99
    policy = np.zeros(env.observation_space.n)
    for s in range(env.observation_space.n):

        Q_values = [sum([prob*(r + gamma * value_table[s_])
                             for prob, s_, r, _ in env.P[s][a]]) 
                                   for a in range(env.action_space.n)]
        # print('Q_values:', Q_values) # 출력 -> Q_values: [0.5435294117528799, 0.5435294117552107, 0.5435294117542429, 0.8152941176311668]

        policy[s] = np.argmax(np.array(Q_values))  # argmax를 통해 최대값을 갖게하는 action을 순서대로 저장 -> policy 생성됨
    
    return policy

def policy_iteration(env):  ## polict iteration 함수, value_table 채택하는 과정과 new_policy를 추출하는 과정을 반복하여 실행 (policy의 변화가 없을때까지)

    num_iterations = 1000
    
    policy = np.zeros(env.observation_space.n)  # 맨 처음 policy 생성 (전부 액션 0으로)
    # print(policy)  # 출력 : [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

    for i in range(num_iterations):
        
        value_function = compute_value_function(policy)  # 주어진 Policy를 적용하여, Value table을 수렴시킴

        new_policy = extract_policy(value_function)     # 수렴한 Value table을 통해, Q table을 생성하고 New Policy를 추출함.

        if np.all(policy == new_policy):
            break

        policy = new_policy 

    return policy

optimal_policy = policy_iteration(env)
print(optimal_policy)


