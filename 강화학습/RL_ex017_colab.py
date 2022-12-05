import torch
import gym
from collections import namedtuple
import matplotlib.pyplot as plt

###  policyGradient  ###


class PolicyNet(torch.nn.Module):
    def __init__(self, input_size, output_size, hidden_layer_size=64):
        super(PolicyNet, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_layer_size)   # MLP
        self.fc2 = torch.nn.Linear(hidden_layer_size, output_size)  # MLP
        self.softmax = torch.nn.Softmax(dim=0)                      # 소프트맥스 필요, 출력 값이 각 action을 실행할 '확률'이라서

    def forward(self, x):
        x = torch.from_numpy(x).float()
        return self.softmax(self.fc2(torch.nn.functional.relu(self.fc1(x))))

    def get_action_and_logp(self, x):
        action_prob = self.forward(x)  # action_prob : 각 action을 실행할 '확률'값들에 대한 tensor ,  ex) [0.1, 0.5, 0.2, 0.2]
        m = torch.distributions.Categorical(action_prob)  # Categorical한 대상에 대해 확률분포를 생성함. ex) action_prob=[0.1, 0.5, 0.2, 0.2]라면, 0번째 action을 뽑을 확률 0.1, 1번째 action을 뽑을 확률 0.5
        action = m.sample()                               # 출력값은 tensor(3) or tensor(1), or tensor(0) 등 index로 출력함
        # print(m.sample())                                 # 출력값은 tensor(3) or tensor(1), or tensor(0) 등 index로 출력함
        logp = m.log_prob(action)                         # log_prob은 확률값을 log로 변환시키는 함수 , log(tensor(0))과 동일 즉, log(0번째 action의 확률)과 동일
        # print(logp)                                     # 출력 : tensor(-2.3026)   // np.log(0.1)  = -2.3025850929940455
        return action.item(), logp                        # action_index , log 취한 action 선택 확률

    def act(self, x):
        action, _ = self.get_action_and_logp(x)
        return action

class ValueNet(torch.nn.Module):
    def __init__(self, input_size, hidden_layer_size=64):
        super(ValueNet, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_layer_size)
        self.fc2 = torch.nn.Linear(hidden_layer_size, 1)

    def forward(self, x):
        x = torch.from_numpy(x).float()
        return self.fc2(torch.nn.functional.relu(self.fc1(x)))

def policyGradient(env, max_num_steps=500, gamma=0.98, lr=0.01,
                   num_traj=10, num_iter=200):
    input_size = env.observation_space.shape[0]  ## STATE SPACE (STATE의 개수)
    print('STATE SPACE (STATE의 개수) : ', env.observation_space.shape)
    output_size = env.action_space.n             ## ACTION의 개수
    Trajectory = namedtuple('Trajectory', 'states actions rewards dones logp')    # 'Trajectory'에 states actions rewards dones logp 튜플을 할당함


    def collect_trajectory():  # Trajectory 모으는 함수 (1 episode 돌리는 함수)
        state_list = []
        action_list = []
        reward_list = []
        dones_list = []
        logp_list = []
        state = env.reset()
        done = False
        steps = 0
        while not done and steps <= max_num_steps:   # done(에피소드 종료) 될때까지 루프 
            action, logp = policy.get_action_and_logp(state)  # policy = PolicyNet(input_size, output_size)
            newstate, reward, done, _ = env.step(action)    # s_, r, terminated, truncated, _
            state_list.append(state)
            action_list.append(action)
            reward_list.append(reward)
            dones_list.append(done)
            logp_list.append(logp)
            steps += 1
            state = newstate

        traj = Trajectory(states=state_list, actions=action_list,
                          rewards=reward_list, logp=logp_list, dones=dones_list)
      # print(traj)  # Trajectory(states=[array([ 9.5363184e-06,  9.3068667e-03,  3.0773466e-02, -4.3019545e-03],
      # dtype=float32), array([ 1.9567365e-04, -1.8624260e-01,  3.0687427e-02,  2.9792932e-01],
      # dtype=float32), array([-0.00352918,  0.00842878,  0.03664601,  0.01508044], dtype=float32), array([-0.0033606 ,  0.20300654,  0.03694762, -0.26581872], dtype=float32), array([ 0.00069953,  0.3975822 ,  0.03163125, -0.54662293], dtype=float32), array([ 0.00865117,  0.5922458 ,  0.02069879, -0.82917416], dtype=float32), array([ 0.02049609,  0.3968471 ,  0.00411531, -0.5300539 ], dtype=float32), array([ 0.02843303,  0.5919109 , -0.00648577, -0.82143724], dtype=float32), array([ 0.04027125,  0.3968783 , -0.02291452, -0.5308013 ], dtype=float32), array([ 0.04820881,  0.59231496, -0.03353054, -0.8306156 ], dtype=float32), array([ 0.06005511,  0.39766696, -0.05014285, -0.54866385], dtype=float32), array([ 0.06800845,  0.20328394, -0.06111613, -0.27219164], dtype=float32), array([ 0.07207413,  0.0090849 , -0.06655996,  0.00060612], dtype=float32), array([ 0.07225583, -0.18502247, -0.06654784,  0.27156827], dtype=float32), array([ 0.06855538, -0.37913483, -0.06111648,  0.5425417 ], dtype=float32), array([ 0.06097268, -0.18320957, -0.05026564,  0.23124543], dtype=float32), array([ 0.05730849,  0.01259326, -0.04564074, -0.07685973], dtype=float32), array([ 0.05756036, -0.1818457 , -0.04717793,  0.20108126], dtype=float32), array([ 0.05392344, -0.37626228, -0.0431563 ,  0.4785165 ], dtype=float32), array([ 0.0463982 , -0.5707492 , -0.03358598,  0.75729126], dtype=float32), array([ 0.03498321, -0.37518087, -0.01844015,  0.45423177], dtype=float32), array([ 0.02747959, -0.5700373 , -0.00935551,  0.7410456 ], dtype=float32), array([ 0.01607885, -0.37478745,  0.0054654 ,  0.44543317], dtype=float32), array([ 0.0085831 , -0.5699863 ,  0.01437406,  0.7398339 ], dtype=float32), array([-0.00281663, -0.76530373,  0.02917074,  1.0370055 ], dtype=float32), array([-0.0181227 , -0.57058144,  0.04991085,  0.75362134], dtype=float32), array([-0.02953433, -0.7663547 ,  0.06498328,  1.0615833 ], dtype=float32), array([-0.04486142, -0.5721506 ,  0.08621494,  0.78998363], dtype=float32), array([-0.05630443, -0.768344  ,  0.10201462,  1.1084964 ], dtype=float32), array([-0.07167131, -0.5746998 ,  0.12418454,  0.8494806 ], dtype=float32), array([-0.08316531, -0.38147032,  0.14117415,  0.59828496], dtype=float32), array([-0.09079471, -0.18857652,  0.15313986,  0.35319027], dtype=float32), array([-0.09456625,  0.00407392,  0.16020367,  0.11244383], dtype=float32), array([-0.09448477,  0.19658096,  0.16245253, -0.12572043], dtype=float32), array([-0.09055315,  0.38904798,  0.15993813, -0.36306855], dtype=float32), array([-0.08277219,  0.58157825,  0.15267676, -0.60135657], dtype=float32), array([-0.07114062,  0.774272  ,  0.14064963, -0.8423221 ], dtype=float32), array([-0.05565519,  0.5775394 ,  0.12380318, -0.50892246], dtype=float32), array([-0.0441044 ,  0.3809106 ,  0.11362474, -0.17993148], dtype=float32), array([-0.03648619,  0.18436155,  0.11002611,  0.14632481], dtype=float32), array([-0.03279895, -0.01214998,  0.1129526 ,  0.47159216], dtype=float32), array([-0.03304195, -0.20867096,  0.12238444,  0.79763263], dtype=float32), array([-0.03721537, -0.01542167,  0.1383371 ,  0.54581815], dtype=float32), array([-0.03752381,  0.17751318,  0.14925346,  0.29972214], dtype=float32), array([-0.03397354, -0.01938604,  0.15524791,  0.6355052 ], dtype=float32), array([-0.03436126,  0.17326893,  0.167958  ,  0.395458  ], dtype=float32), array([-0.03089589,  0.36565927,  0.17586717,  0.16008124], dtype=float32), array([-0.0235827 ,  0.5578845 ,  0.17906879, -0.07237025], dtype=float32), array([-0.01242501,  0.75004774,  0.1776214 , -0.30364075], dtype=float32), array([0.00257595, 0.55289793, 0.17154858, 0.0393778 ], dtype=float32), array([ 0.0136339 ,  0.74519783,  0.17233613, -0.19464979], dtype=float32), array([0.02853786, 0.5480834 , 0.16844313, 0.14705835], dtype=float32), array([ 0.03949953,  0.74044305,  0.1713843 , -0.08810893], dtype=float32), array([0.05430839, 0.54333186, 0.16962212, 0.25336695], dtype=float32), array([0.06517503, 0.73567706, 0.17468946, 0.01861984], dtype=float32), array([ 0.07988857,  0.9279195 ,  0.17506185, -0.21425721], dtype=float32), array([0.09844696, 0.7307833 , 0.17077671, 0.12813324], dtype=float32), array([0.11306263, 0.53367877, 0.17333938, 0.46945378], dtype=float32), array([0.1237362 , 0.33658645, 0.18272845, 0.8113689 ], dtype=float32), array([0.13046794, 0.13949473, 0.19895583, 1.1555083 ], dtype=float32)], actions=[0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1], rewards=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], dones=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True], logp=[tensor(-0.7011, grad_fn=<SqueezeBackward1>), tensor(-0.4942, grad_fn=<SqueezeBackward1>), tensor(-0.6693, grad_fn=<SqueezeBackward1>), tensor(-0.8719, grad_fn=<SqueezeBackward1>), tensor(-1.0927, grad_fn=<SqueezeBackward1>), tensor(-0.3000, grad_fn=<SqueezeBackward1>), tensor(-1.0943, grad_fn=<SqueezeBackward1>), tensor(-0.2976, grad_fn=<SqueezeBackward1>), tensor(-1.1101, grad_fn=<SqueezeBackward1>), tensor(-0.2912, grad_fn=<SqueezeBackward1>), tensor(-0.3850, grad_fn=<SqueezeBackward1>), tensor(-0.5034, grad_fn=<SqueezeBackward1>), tensor(-0.6458, grad_fn=<SqueezeBackward1>), tensor(-0.8513, grad_fn=<SqueezeBackward1>), tensor(-0.3972, grad_fn=<SqueezeBackward1>), tensor(-0.5714, grad_fn=<SqueezeBackward1>), tensor(-0.6144, grad_fn=<SqueezeBackward1>), tensor(-0.8118, grad_fn=<SqueezeBackward1>), tensor(-1.0638, grad_fn=<SqueezeBackward1>), tensor(-0.2649, grad_fn=<SqueezeBackward1>), tensor(-1.0635, grad_fn=<SqueezeBackward1>), tensor(-0.2634, grad_fn=<SqueezeBackward1>), tensor(-1.0795, grad_fn=<SqueezeBackward1>), tensor(-1.4881, grad_fn=<SqueezeBackward1>), tensor(-0.1490, grad_fn=<SqueezeBackward1>), tensor(-1.5465, grad_fn=<SqueezeBackward1>), tensor(-0.1374, grad_fn=<SqueezeBackward1>), tensor(-1.6341, grad_fn=<SqueezeBackward1>), tensor(-0.1220, grad_fn=<SqueezeBackward1>), tensor(-0.1897, grad_fn=<SqueezeBackward1>), tensor(-0.2872, grad_fn=<SqueezeBackward1>), tensor(-0.4043, grad_fn=<SqueezeBackward1>), tensor(-0.5435, grad_fn=<SqueezeBackward1>), tensor(-0.7004, grad_fn=<SqueezeBackward1>), tensor(-0.9015, grad_fn=<SqueezeBackward1>), tensor(-1.0939, grad_fn=<SqueezeBackward1>), tensor(-0.3111, grad_fn=<SqueezeBackward1>), tensor(-0.4323, grad_fn=<SqueezeBackward1>), tensor(-0.5986, grad_fn=<SqueezeBackward1>), tensor(-0.8267, grad_fn=<SqueezeBackward1>), tensor(-1.1433, grad_fn=<SqueezeBackward1>), tensor(-0.2386, grad_fn=<SqueezeBackward1>), tensor(-0.3441, grad_fn=<SqueezeBackward1>), tensor(-0.9646, grad_fn=<SqueezeBackward1>), tensor(-0.3061, grad_fn=<SqueezeBackward1>), tensor(-0.4233, grad_fn=<SqueezeBackward1>), tensor(-0.5728, grad_fn=<SqueezeBackward1>), tensor(-0.7365, grad_fn=<SqueezeBackward1>), tensor(-0.5085, grad_fn=<SqueezeBackward1>), tensor(-0.6748, grad_fn=<SqueezeBackward1>), tensor(-0.5544, grad_fn=<SqueezeBackward1>), tensor(-0.6252, grad_fn=<SqueezeBackward1>), tensor(-0.6050, grad_fn=<SqueezeBackward1>), tensor(-0.5652, grad_fn=<SqueezeBackward1>), tensor(-0.7268, grad_fn=<SqueezeBackward1>), tensor(-0.5218, grad_fn=<SqueezeBackward1>), tensor(-0.7160, grad_fn=<SqueezeBackward1>), tensor(-1.0044, grad_fn=<SqueezeBackward1>), tensor(-1.3989, grad_fn=<SqueezeBackward1>), tensor(-0.1645, grad_fn=<SqueezeBackward1>)])

        return traj

    def calc_returns(rewards):
        dis_rewards = [gamma**i * r for i, r in enumerate(rewards)]  ## [ gamma**0 * r, gamma**1 * r, gamma**2 * r, gamma**3 * r, ...]
        return [sum(dis_rewards[i:]) for i in range(len(dis_rewards))]  ## [R(0~end), R(1~end), R(2~end), ...]

    policy = PolicyNet(input_size, output_size)
    policy_optimizer = torch.optim.Adam(policy.parameters(), lr=lr)

    value = ValueNet(input_size)
    value_optimizer = torch.optim.Adam(value.parameters(), lr=lr)

    mean_return_list = []
    for it in range(num_iter):
        traj_list = [collect_trajectory() for _ in range(num_traj)]    #
        returns = [calc_returns(traj.rewards) for traj in traj_list]   # traj.rewards는 traj(Trajectory에서 tuple 요소중 rewards를 뽑아냄)
                                                                       # returns는 2차원 : [[Return(0~end), Return(1~end), Return(2~end), ...],  [Return(0~end), Return(1~end), Return(2~end), ...], ... , [Return(0~end), Return(1~end), Return(2~end), ...] ]

        # ====================================#
        # policy gradient                    #
        # ====================================#
        # policy_loss_terms = [-1. * traj.logp[j] * (torch.Tensor([returns[i][0]]))                   # returns[i][0] :   Return(0~end)로만 참고함 ([Return(0~end), Return(0~end), Return(0~end), ..., ...])   Expectation of Return이 목적함수(로스 펑션으로 만들기 위해 -1 추가)
        #                     for i, traj in enumerate(traj_list) for j in range(len(traj.actions))]  # policy gradient, policyNet에서의 로스 펑션, 값이 작을수록 Loss가 적은 형태로 식을 만들기 위해 앞에 -1 붙임

        # ====================================#
        # policy gradient with reward-to-go  #
        # ====================================#
        # policy_loss_terms = [-1. * traj.logp[j] * (torch.Tensor([returns[i][j]]))                   # returns[i][j]] :   Return(j~end)로 참고함 => [Return(0~end), Return(1~end), Return(2~end), ~, Return(end-1~end) , ..., ... , ]    Expectation of Return이 목적함수
        #                     for i, traj in enumerate(traj_list) for j in range(len(traj.actions))]  # policy gradient, policyNet에서의 로스 펑션, 값이 작을수록 Loss가 적은 형태로 식을 만들기 위해 앞에 -1 붙임

        #====================================#
        # policy gradient with base function #
        #====================================#
        policy_loss_terms = [-1. * traj.logp[j] * (returns[i][j] - value(traj.states[j]))             # returns[i][j] - value(traj.states[j]  :   리턴값에 대해 표준화 적용 (평균값을 빼줌), 평균값은 곧 기대값이고 V(s)를 통해 구함. V(s)는 ValueNet에서 구함.
                             for i, traj in enumerate(traj_list) for j in range(len(traj.actions))]   # policy gradient, policyNet에서의 로스 펑션, 값이 작을수록 Loss가 적은 형태로 식을 만들기 위해 앞에 -1 붙임


        policy_loss = 1. / num_traj * torch.cat(policy_loss_terms).sum()                              # 각  returns의 원소들을 합산하고 나눔  =>  Expectation of Return 계산
        policy_optimizer.zero_grad()
        policy_loss.backward()
        policy_optimizer.step()

        value_loss_terms = [1. / len(traj.actions) * (value(traj.states[j]) - returns[i][j])**2.      # ValueNet에서의 로스 펑션, MSE 적용
                            for i, traj in enumerate(traj_list) for j in range(len(traj.actions))]
        value_loss = 1. / num_traj * torch.cat(value_loss_terms).sum()
        value_optimizer.zero_grad()
        value_loss.backward()
        value_optimizer.step()

        mean_return = 1. / num_traj * \
            sum([traj_returns[0] for traj_returns in returns])
        mean_return_list.append(mean_return)
        if it % 10 == 0:
            print('Iteration {}: Mean Return = {}'.format(it, mean_return))

    return policy, mean_return_list

env = gym.make('CartPole-v1')
env._max_episode_steps=500
agent, mean_return_list = policyGradient(env, num_iter=500, max_num_steps=500, gamma=1.0, num_traj=5)

plt.plot(mean_return_list)
plt.xlabel('Iteration')
plt.ylabel('Mean Return')
plt.savefig('pg1_returns.png', format='png', dpi=300)