import random
def shutudai():
   l=[]
   alp=[]
   for i in range(65,91):
       alp.append(chr(i))
   l=random.sample(alp,7)
   a=random.sample(l,2)
   print(f"対象文字列:\n{l}")
   print(f"欠損文字:\n{a}")
   for i in a:
       l.remove(i)
   print(f"表示文字:\n{l}")
   return a

def kaito(seikai):
    num=int(input("欠損文字はいくつあるでしょうか？："))
    if num !=2:
        print("不正解です")
    else:
        print("正解です．では，具体的に欠損文字を1つずつ入力してください．")
        for i in range(num):
            c = input(f"{i+1}文字目を入力してください：")
            if c not in seikai:
                print("不正解です．またチャレンジしてください．")
                return False
            else:
                seikai.remove(c)
        print("欠損文字も含めて完全正解です！！！")
        return True
    return False
        

if __name__ == "__main__":
    alph=shutudai()
    print(alph)
    kaito(alph)


#To do
#時間はまだ測れません
#文字の括弧は外し方がわかりませんでした。
#コード汚くてすまん!!


    
     


