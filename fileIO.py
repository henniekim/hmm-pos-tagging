import os

class Files :
    def __init__(self):
        self.corpus = [] # 불러온 corpus가 저장되는 곳
        self.sentence = [] # corpus를 문장 단위로 나누어 저장하는 list
        self.word = [] # 위에서 나눈 문장을 다시 어절 단위로 나누어 저장
        self.result = [] # Smash 출력 결과 저장
        self.parsedCorpus = [] # 최종 parse된 corpus 파일
        self.parsedResult = [] # 최종 parse된 result 파일

        pass

    def writeInput(self):
        inputSentence = input("분석할 문장을 입력하세요\n")
        fileObject = open("input.txt", 'w')
        fileObject.write(inputSentence)

    def openSmash(self):
        if(os.system("SMASH.exe")):
            print("SMASH 프로그램을 실행하지 못하였습니다. 파일 경로를 확인하세요.")
        else :
            print("SMASH 프로그램을 실행하였습니다.")

    def openResult(self):
        fileObject = open("result.txt", "r")
        self.result = fileObject.read()
        print(self.result)

    def parseResult(self):
        print("실행 결과를 parsing하는 중입니다.")
        self.result = self.result.split('\n\n\n\n')
        self.result.pop() # 맨 마지막 공백은 삭제한다.
        print("실행 결과에 있는 문장의 개수는 {} 개 입니다.".format(len(self.result)))

        currentWord = []
        currentResult = []

        for sentenceIdx in range (len(self.result)):
            # parsing 을 편하기 하기 위한 궁여지책...
            # 형태소 분석 결과가 최대 32개 까지만 나온다는 점을 이용함
            self.result[sentenceIdx] = self.result[sentenceIdx].replace("\n\n", "\n")
            self.result[sentenceIdx] = self.result[sentenceIdx].replace("\n ", "\t")
            self.result[sentenceIdx] = self.result[sentenceIdx].replace("\n1", "\t1")
            self.result[sentenceIdx] = self.result[sentenceIdx].replace("\n2", "\t2")
            self.result[sentenceIdx] = self.result[sentenceIdx].replace("\n3", "\t3")

            currentWord = self.result[sentenceIdx].split('\n')
            currentMorpheme = []
            for wordIdx in range (len(currentWord)):
                currentMorpheme.append(currentWord[wordIdx].split('\t'))
            self.parsedResult.append(currentMorpheme)

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
            # !!!! NOTICE : indexing 할 때 주의!!!! #
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
            #
            # self.parsedResult[sentenceIdx][WordIdx][문장 전체 + 형태소 분석 결과]
            #                                         - 0번째 - 1번째~최대 32
            # len으로 분석 결과 사용할 때에는 -1 해줘야 함

    def loadCorpus(self):
        fileObject = open("train.txt", "r")
        print("학습할 corpus를 불러왔습니다.")
        self.corpus = fileObject.read()

    def parseCorpus(self):
        print("Corpus를 parsing하는 중입니다.")
        self.corpus = self.corpus.split('\n\n')
        print("Corpus에 있는 문장의 개수는 {} 개 입니다".format(len(self.corpus)))

        for corpusIdx in range (len(self.corpus)) :
            self.sentence.append(self.corpus[corpusIdx].split('\n'))
            currentSentence = []
            for wordIdx in range (len(self.sentence[corpusIdx])) :
                self.word = self.sentence[corpusIdx][wordIdx].split('\t') # 각 문장을 어절 단위로 분리한다.
                if self.word[0] == '': # 마지막 line이 나왔을 경우 loop를 중단한다.
                    break
                morpheme = self.word[1].split('+') # 분리한 어절 단위를 다시 형태소 단위로 분리한다.
                currentWord = []
                for morphemeIdx in range (len(morpheme)):
                    currentWord.append(morpheme[morphemeIdx])
                currentSentence.append(currentWord)
            self.parsedCorpus.append(currentSentence)

            # parsedCorpus[몇번째 문장인지][해당 문장에서 몇번째 어절인지][해당 어절에서 몇 번째 형태소인지]
            # parsedCorpus[corpusIdx][wordIdx][morphemeIdx]

        if __debug__ :
            print("for debug : corpus를 출력하였습니다")





