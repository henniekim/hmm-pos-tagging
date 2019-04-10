from HMM import *
from fileIO import *

mode = None #'manual'

file = Files() # 파일 입출력 및 smash 관련 객체 생성
hmm = HMM()

if mode == 'manual' : # 문장을 직접 입력하는 모드
    file.writeInput() # 분석할 문장을 입력한다.
    file.openSmash() # 스매쉬 실행해서 결과 저장 및 출력

file.openResult() # 결과 파일 불러오기
file.loadCorpus() # 학습할 말뭉치를 불러온다.
file.parseCorpus() # 말뭉치를 가공하기 좋게 파싱

hmm.setCorpus(file.parsedCorpus) # Corpus 세팅
hmm.setState() # 세종 형태소 종류를 세팅한다.
hmm.train() # 학습을 한다.

#TODO
#hmm.viterbi()
#hmm.displaySolution() # 추론 결과를 도출한다.
#file.saveResult(hmm.result) # 결과를 저장한다.



