import numpy as np
import gym
from tqdm import tqdm


######### TD Control : Q learning  ########

class Agent:
    def __init__(self, env):
        self.env = env
        self.episode_reward = 0.0
        self.q_val = np.zeros(16 * 4).reshape(16, 4).astype(np.float32)

    def learn(self):
        # one episode learning
        state, _ = self.env.reset()
        
        for t in range(TURN_LIMIT):
            if np.random.rand() < EPS: # explore (epsilon)
                act = self.env.action_space.sample() # random
            else: # exploit (greedy)
                act = np.argmax(self.q_val[state])
            next_state, reward, terminated, truncated, info = self.env.step(act)
            q_next_max = np.max(self.q_val[next_state])  # next_action은 최대값이 나오도록 하는 action으로 지정
            # Q <- Q + a(Q' - Q)
            # <=> Q <- (1-a)Q + a(Q')
            self.q_val[state][act] = (1 - ALPHA) * self.q_val[state][act] + ALPHA * (reward + GAMMA * q_next_max)  # Q table 업데이트, 클래스 인스턴스라서 지속됨
                                # self.q_val[state][act] + ALPHA * ( reward + GAMMA * q_next_max - self.q_val[state][act]) 와 동일
            
            if terminated or truncated:
                return reward    # 리턴 값 (터미널 스테이트로 가야지만 리워드가 1이라, 리워드만 넣어줘도 되는듯)
            else:
                state = next_state
        return 0.0 # over limit 일때  리워드 값  0 반환

    def test(self):
        state, _ = self.env.reset()
        for t in range(TURN_LIMIT):
            act = np.argmax(self.q_val[state])   ## greedy policy로 action 선택
            next_state, reward, terminated, truncated, info = self.env.step(act)
            if terminated or truncated:
                return reward
            else:
                state = next_state
        return 0.0 # over limit

def main():
    env = gym.make("FrozenLake-v1")
    agent = Agent(env)

    print("###### LEARNING #####")
    reward_total = 0.0
    for i in tqdm(range(LEARNING_COUNT)):
        reward_total += agent.learn()  # Q -learning 학습 메소드 호출
    print("episodes      : {}".format(LEARNING_COUNT))     # 출력 -> episodes      : 100000
    print("total reward  : {}".format(reward_total))       # total reward  : 36271.0
    print("average reward: {:.2f}".format(reward_total / LEARNING_COUNT))  # 출력 -> average reward: 0.36
    print("Q Value       :{}".format(agent.q_val))
    # Q Value: [[0.4978811  0.47230384 0.4822142  0.47267798]
    #          [0.35124472 0.26728904 0.26953018 0.4701997]
    #          [0.4122527 0.4034089 0.40693483 0.44183606]
    #          [~] ~ [~]]

    print("###### TEST #####")
    reward_total = 0.0
    for i in tqdm(range(TEST_COUNT)):
        reward_total += agent.test()
    print("episodes      : {}".format(TEST_COUNT))
    print("total reward  : {}".format(reward_total))                   # 출력 -> total reward  : 726.0
    print("average reward: {:.2f}".format(reward_total / TEST_COUNT))  # 출력 -> average reward: 0.73

if __name__ == "__main__":
    # Q learning params
    ALPHA = 0.1  # learning rate
    GAMMA = 0.99  # reward discount
    LEARNING_COUNT = 100000
    TEST_COUNT = 1000

    EPS = 0.1   # Epsilon

    TURN_LIMIT = 100
    main()