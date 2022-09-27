import random
def shutudai():
    QA={"サザエの旦那の名前は？":["マスオ","ますお"],"カツオの妹の名前は？":["ワカメ","わかめ"],"タラオはカツオから見てどんな関係？":["甥","おい","甥っ子","おいっこ"]}　#辞書を使って質問と答えを紐づけました
    RQA=random.choice(list(QA.items()))
    print(RQA[0])
    ans=RQA[1]
    return ans
    

def kaitou(ans):
   ANS=input("答えるんだ：")
   if ANS in ans:
    print("正解!!")
   else:
    print("出直してこい") 



if __name__ == "__main__":
    Q=shutudai()
    kaitou(Q)
    


