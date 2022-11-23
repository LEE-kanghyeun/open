# libraries
import gym
import collections
import random

# pytorch library is used for deep learning
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# hyperparameters
learning_rate = 0.0005
gamma = 0.98
buffer_limit = 50000        # size of replay buffer, 버퍼에 저장할 데이터 개수
batch_size = 32

class ReplayBuffer():
    def __init__(self):
        self.buffer = collections.deque(maxlen=buffer_limit)    # double-ended queue(deque)를 저장소로 선택,
                                                                # buffer_size는 50000으로 설정,
                                                                # 50000개가 차면 그 이후부터는 가장 오래된 데이터를 삭제하고 새 데이터를 보관
    
    def put(self, transition):  # transition 데이터 넣기 메소드
        self.buffer.append(transition)

    def sample(self, n):     # transition 데이터 추출 메소드 (train할떄 batch만들듯이 random으로 데이터 추출해감)
        mini_batch = random.sample(self.buffer, n)  # n개만큼 데이터 추출
        s_lst, a_lst, r_lst, s_prime_lst, done_mask_lst = [], [], [], [], [] # (s,a,r,s')과 종료여부

        for transition in mini_batch:
            s, a, r, s_prime, done_mask = transition  # buffer에서 추출된 mini_batch에서 transition 데이터 추출
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r])
            s_prime_lst.append(s_prime)
            done_mask_lst.append([done_mask])

        return torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
               torch.tensor(r_lst), torch.tensor(s_prime_lst, dtype=torch.float), \
               torch.tensor(done_mask_lst)

    def size(self):  # buffer의 사이즈 확인하는 용도의 메소드
        return len(self.buffer)


class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__() # 초기화
        self.fc1 = nn.Linear(4, 128)  # 가중치 3개(히든 레이어 2개 적용) 입력값(state)은 4개 (cart position, cart 속도, pole 각도, pole 속도)
        self.fc2 = nn.Linear(128, 128) # 가중치 3개(히든 레이어 2개 적용)
        self.fc3 = nn.Linear(128, 2) # 가중치 3개(히든 레이어 2개 적용), output(Q(s,a))은 2개

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
      
    def sample_action(self, obs, epsilon):  # epsilon-greedy로 action 선택하는 함수,  obs : state input 값
        out = self.forward(obs)  # forward를 진행 (신경망 통과), out은 tensor 형태
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,1)
        else : 
            return out.argmax().item()   

def train(q, q_target, memory, optimizer):
    for i in range(10):
        s,a,r,s_prime,done_mask = memory.sample(batch_size)  # memory에서 데이터 sampling(추출하기), 배치 사이즈만큼

        q_out = q(s)  # q_out.shape = (batch_size, 2)  // 2는 액션의 개수
        q_a = q_out.gather(1,a)  # action_list인 a를 활용하여, Q테이블에서 각 state에 맞는 action 값을 취함.
                                 # => 그에 대한 value 값을 q_a에 텐서로 저장

        # DQN
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)  # 타겟넷에 대한 output 값에 대해 dim=1의 max값을 취함

        # # Double DQN
        # argmax_Q = q(s_prime).max(1)[1].unsqueeze(1)
        # max_q_prime = q_target(s_prime).gather(1, argmax_Q)

        target = r + gamma * max_q_prime * done_mask # terminate stae면 done_mask가 0이므로 뒤의 항 없어짐
        
        # MSE Loss
        loss = F.mse_loss(q_a, target)

        # Smooth L1 Loss
        #loss = F.smooth_l1_loss(q_a, target)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def main():
    env = gym.make('CartPole-v1')
    q = Qnet()            # 메인 넷
    q_target = Qnet()     # 타겟 넷  , 별개로 학습
    q_target.load_state_dict(q.state_dict())
    memory = ReplayBuffer()  ## transition을 담고 있는 테이블에 대한 객체 선언

    print_interval = 20   #
    score = 0.0           #
    optimizer = optim.Adam(q.parameters(), lr=learning_rate)

    for n_epi in range(3000):
        epsilon = max(0.01, 0.08 - 0.01*(n_epi/200)) #Linear annealing from 8% to 1%, epsilon 값을 0.01이 되기 전까지 점점 줄여가도록 함.
        s = env.reset()
        done = False
        
        while not done:  # 종료 state가 아니라면
            a = q.sample_action(torch.from_numpy(s).float(), epsilon)  # action을 policy(eplsilon-grredy)에 따라 선택
            s_prime, r, done, info = env.step(a)  # 단계 진행
            done_mask = 0.0 if done else 1.0
            memory.put((s,a,r/100.0,s_prime, done_mask))  # r값이 너무 크면, train이 잘 안되서 줄엿음 (왜? 튜닝/테크닉의 영역이라는 교수님의 말씀)
                                                          # replace_buffer 객체에 transition 데이터 저장
            s = s_prime

            score += r
            if done:
                break

        if memory.size()>2000:  # 메모리 사이즈가 2000까지 차기 전에는 train(x), 데이터가 적을때는 훈련이 무의미하므로
            train(q, q_target, memory, optimizer)

        if n_epi%print_interval==0 and n_epi!=0:  # 20번쨰 episode마다 메인넷(q)의 가중치값을 타겟넷(q_target)으로 카피함.
            q_target.load_state_dict(q.state_dict())
            print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%".format(
                                                            n_epi, score/print_interval, memory.size(), epsilon*100))
            score = 0.0

    env.close()

if __name__ == '__main__':
    main()