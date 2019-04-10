import os

class Files :
    def __init__(self):
        self.sentence = []
        self.word = []
        self.corpus = []
        self.result = []
        self.parsedCorpus = []

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





