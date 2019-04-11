
# HMM 이론

###############################################
## Followings from Jurafsky book appendix A. ##
###############################################

# Q = q1q2...qN : a set of N states
# A = a11...aij...aNN : a transition probability matrix A,
    # each aij representing the probability of moving from state i to state j
# O = o1o2...oT : a sequence of T observations, each one drawn from a vocabulary V = v1,v2,...,vV
# B = bi(ot) : a sequence of observation likelihood, also called emission probabilities,
    # each expressing the probability of an observation ot being generated from a state i
# pi = pi1,pi2,...,piN : an initial probability distribution over states.
    # pi_i is the probability the Markov chain will start in state i. Some states j may have pi_j = 0,
    # meaning that they cannot be initial states.

# Q : state N 개 여기서 state 는 어떤 품사인지를 나타낸다.
# A : 한 state에서 다른 state로 넘어갈 확률, 명사 -> 동사 로 넘어갈 확률
# O : 단어가 어떻게 나열되어있는지, 한국어에서는 어절 단위로 분석해야함
# B : 방출 확률, 특정 품사로 부터 해당 단어가 나올 확률
# pi : 해당 품사가 처음에 등장할 확률



class HMM :
    def __init__(self):
        self.count = []
        # 생성자

    def setCorpus(self, inputCorpus):
        self.corpus = inputCorpus
        print("corpus를 setting하였습니다.")
        # 참고용
        # parsedCorpus[몇번째 문장인지][해당 문장에서 몇번째 어절인지][해당 어절에서 몇 번째 형태소인지]
        # parsedCorpus[corpusIdx][wordIdx][morphemeIdx]

    def train(self):
        self.calcInitProb()

    # 특정 state로 시작할 확률을 구한다
    def calcInitProb(self) :
        self.start = []
        sum = 0
        probSum = 0.0
        for sentenceIdx in range (0, len(self.corpus)-2):
            self.start.append(self.corpus[sentenceIdx][0][0])
            self.start[sentenceIdx] = self.start[sentenceIdx].split('/')[1]

        for stateIdx in self.state :
            currentCount = self.start.count(stateIdx) + 1
            self.count.append(currentCount)
            sum += currentCount # 전체 개수를 구하고

        for stateIdx in range(len(self.state)):
            self.count[stateIdx] /= sum # 여기서 전체 개수로 나누어서 각 확률을 계산해준다
            probSum += self.count[stateIdx]

        print(sum)
            # plus 1 smoothing for initial state

        # 주어진 품사로 시작할 확률을 구한다.

    def setState(self) :
        # 어떤 품사가 있는지 정의해준다.
        self.state = ['NNG', 'NNP', 'NNB', 'NR', 'NP',
                 'VV', 'VA', 'VX', 'VCP', 'VCN',
                 'MM',
                 'MAG', 'MAJ',
                 'IC',
                 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC',
                 'EP',
                 'EF', 'ETN', 'ETM',
                 'XPN',
                 'XSN', 'XSV', 'XSA',
                 'XR',
                 'SF', 'SP', 'SS', 'SE', 'SO', 'SW',
                 'NF', 'NV', 'NA',
                 'SL', 'SH', 'SN']

    # Viterbi 알고리즘
    def viterbi(self) :
        pass

    def setObservationProb(self) :
        pass

    # 관측확률 계산
    def calcObservationProb(self) :
        pass

    # 전이확률 계산 (state1에서 state2로 넘어갈 확률, 여기서는 품사1에서 품사2로 넘어갈 확률)
    def calcTransitionProb(self) :
        pass

