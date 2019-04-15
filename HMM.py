
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

from set import *

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
        self.calcTransitionBetweenWord() # 어절 간 변이 확률 구하기
        self.calcTransitionInWord() # 한 어절 내부에서 상태 변이 확률 구하기
        self.calcObservationProb() # 각 상태에서 해당 단어가 나올 확률 구하기
        pass

    def setState(self):
        # 어떤 품사가 있는지 정의해준다.
        self.state = {'NNG': 0, 'NNP': 1, 'NNB': 2, 'NR': 3, 'NP': 4,  # 5
                      'VV': 5, 'VA': 6, 'VX': 7, 'VCP': 8, 'VCN': 9,  # 5
                      'MM': 10,  # 1
                      'MAG': 11, 'MAJ': 12,  # 2
                      'IC': 13,  # 1
                      'JKS': 14, 'JKC': 15, 'JKG': 16, 'JKO': 17, 'JKB': 18, 'JKV': 19, 'JKQ': 20, 'JX': 21, 'JC': 22,  # 9
                      'EP': 23,  # 1
                      'EF': 24, 'EC': 25, 'ETN': 26, 'ETM': 27,  # 4
                      'XPN': 28,  # 1
                      'XSN': 29, 'XSV': 30, 'XSA': 31,  # 3
                      'XR': 32,  # 1
                      'SF': 33, 'SP': 34, 'SS': 35, 'SE': 36, 'SO': 37, 'SW': 38,  # 6
                      'NF': 39, 'NV': 40, 'NA': 41,  # 3
                      'SL': 42, 'SH': 43, 'SN': 44,  # 2
                      'START': 45, 'END': 46}  # 2

    def calcInitProb(self) :
        # 특정 품사로 시작할 확률을 구한다
        # 47 x 1 매트릭스
        self.start = []
        sum = 0
        probSum = 0.0

        for sentenceIdx in range (0, len(self.corpus)-2):
            self.start.append(self.corpus[sentenceIdx][0][0])
            self.start[sentenceIdx] = self.start[sentenceIdx].split('/')[1]

        for stateIdx in self.state :
            currentCount = self.start.count(stateIdx) + 1  # plus 1 smoothing for initial state
            self.count.append(currentCount)
            sum += currentCount # 전체 개수를 구하고

        # for stateIdx in range(len(self.state)):
        #     self.count[stateIdx] /= sum # 여기서 전체 개수로 나누어서 각 확률을 계산해준다
        #     probSum += self.count[stateIdx]

        if __debug__ :
            print("초기 확률의 합은 {} 입니다.".format(sum))

        print("초기 확률을 계산하였습니다.") # 완료 메시지
        pass

    def viterbi(self) :
        # Viterbi 알고리즘
        pass

    def calcObservationProb(self) :
        # 관측확률 계산 (특정 state에서 특정 단어가 나올 확률)
        # emission probability
        # output probability
        # 46 x (corpus에 존재하는 단어/형태소 개수) 매트릭스가 나오면 된다.

        self.countMorpheme()

        pass

        # def countItem(self, key):
        #     count = 0
        #     for countIdx in range(len(self.contents)):
        #         if self.contents[countIdx] == key :
        #             count += 1
        #         else :
        #             pass
        #     return count

    def countMorpheme(self):
        morphemeSet = Set()
        for sentenceIdx in range (len(self.corpus)-2):
            for wordIdx in range (len(self.corpus[sentenceIdx])):
                for morphemeIdx in range (len(self.corpus[sentenceIdx][wordIdx])):
                    morphemeSet.addElement(self.corpus[sentenceIdx][wordIdx][morphemeIdx].split('/')[0])

        pass

    def calcTransitionBetweenWord(self) :
        # 어절 간 변환 확률
        # 뭔가 따로 계산해야 될 것 같다.
        # 전이확률 계산 (state1에서 state2로 넘어갈 확률, 여기서는 품사1에서 품사2로 넘어갈 확률)
        # 내가 이해한 것이 맞다면
        # 47 x 47 매트릭스가 나오면 된다... -> 45개의 품사 + $tart + &nd
        # self.transition[currentState][nextState]
        #    0  1  2  3
        # 0                : 0 state i번째 state로  넘어갈 확률 : 요 줄의 합은 1이 되어야 한다.
        # 1
        # 2
        # 3

        self.transitionBetweenWord = self.initTable(len(self.state), 1) # 초기화

        # 각 state 별로 parsing 시작
        for sentenceIdx in range (len(self.corpus)-2):
            for wordIdx in range (len(self.corpus[sentenceIdx])-1):
                currentLastWordState = self.corpus[sentenceIdx][wordIdx][-1].split('/')[-1]
                nextFirstWordState = self.corpus[sentenceIdx][wordIdx+1][0].split('/')[-1]
                # 이거를 dictionary key value로 사용하기
                if currentLastWordState == '' or nextFirstWordState == '':
                    continue
                else:
                    self.transitionBetweenWord[self.state[currentLastWordState.upper()]][self.state[nextFirstWordState.upper()]] += 1
        pass

    def calcTransitionInWord(self):
        self.transitionInWord = self.initTable(len(self.state), 1)  # 초기화
        # 단어 내부 간 변환 확률
        for sentenceIdx in range (len(self.corpus)-2):
            for wordIdx in range (len(self.corpus[sentenceIdx])-1):
                for internalIdx in range (len(self.corpus[sentenceIdx][wordIdx])-1):
                    currentWordState = self.corpus[sentenceIdx][wordIdx][internalIdx].split('/')[-1]
                    nextWordState = self.corpus[sentenceIdx][wordIdx][internalIdx+1].split('/')[-1]
                    if currentWordState == '' or nextWordState == '' :
                        continue
                    else:
                        self.transitionInWord[self.state[currentWordState.upper()]][self.state[nextWordState.upper()]] += 1
        pass

    def initTable(self, numberOfState, initialValue):
        resultTable = []
        for stateIdx in range(numberOfState):
            resultTableRow = []
            for stateIdx in range(numberOfState):
                resultTableRow.append(initialValue)
            resultTable.append(resultTableRow)

        return resultTable





