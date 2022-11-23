# https://stackoverflow.com/questions/73195438/openai-gyms-env-step-what-are-the-values


from tqdm import tqdm
import gym
env = gym.make("FrozenLake-v1", render_mode = 'rgb_array') # create and return a Frozen Lake environment


num_episodes = 100
num_timesteps = 50
total_reward = 0
total_timestep = 0

for i in tqdm(range(num_episodes)):
    state = env.reset()  # Step을 실행하다가 epsiode가 끝나서 이를 초기화해서 재시작해야할 때, 초기 State를 반환한다.

    for t in range(num_timesteps):
        env.render()  # visualize the environment, Graphic User Interface (GUI)로 현재 진행상황을 출력하는 함수

        random_action = env.action_space.sample()
        new_state, reward,  done, terminated , info = env.step(random_action)  # env.step(action)은 알고리즘을 통해 얻어낸 Action을 1 step 수행한 후, 현재 state와 reward 등의 정보를 반환한다.
        print(new_state, reward, done, terminated , info)
        # reward(float) : 보상
        # terminated : terminal state인지 아닌지,
        # done : episode가 끝났는지에 대한 불리언 값
        # info (dictionary): `info` contains auxiliary diagnostic information (helpful for debugging, learning, and logging).
        #                This might, for instance, contain: metrics that describe the agent's performance state, variables that are
        #                hidden from observations, or individual reward terms that are combined to produce the total reward.
        #                It also can contain information that distinguishes truncation and termination, however this is deprecated in favour
        #                of returning two booleans, and will be removed in a future version.
        #               (deprecated)
        # action : 0: left, 1: down, 2: right, 3:up

        total_reward += reward

        if done:
            # print('done:  ' , new_state, reward,  done, terminated , info)
            break

    total_timestep += t


print("Number of successful episodes: %d / %d"%(total_reward, num_episodes))
print("Average number of timesteps per episode: %.2f"%(total_timestep/num_episodes))


