# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import time
import re
#快速模幂
def quick_algorithm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans
#转换256
def asc(a):
    index=len(a)-1
    ans=0
    for letter in a:     # 第一个实例
        ans+=ord(letter)*pow(256,index)
        index-=1
    return ans
#password=format(quick_algorithm(asc(password),65537,135261828916791946705313569652794581721330948863485438876915508683244111694485850733278569559191167660149469895899348939039437830613284874764820878002628686548956779897196112828969255650312573935871059275664474562666268163936821302832645284397530568872432109324825205567091066297960733513602409443790146687029),"x")
#print(password)
#hex() 16进制转换
"""转换字母
while e>0:
    print(chr(e%256))
    print(e%256)
    e=e//256
    g.append(chr(e%256))

for i in reversed(g):
    print(i)
"""
#根据坐标获得字母坐标值
def changeletter(a,b):
    c=""
    c+=chr(a+ord('a'))
    c+=chr(b+ord('a'))
    return c
#获取对应字母的数字
def changenum(a):
    b=ord(a)-ord('a')
    return b
#获取每一行的值
def getline(a):
    print("\"",end="")
    for i in range(changenum(a[1])-4,changenum(a[1])+5):
        if(i>=0 and i<15):
            print(h[changenum(a[0])][i],end="")
    print("\"",end="")
    print(',')
    print("\"",end="")
    b=changenum(a[0])-4
    for i in range(changenum(a[1])-4,changenum(a[1])+5):
        if(i>=0 and i<15 and b>=0 and b<15):
            print(h[b][i],end="")
        b+=1
    print("\"",end="")
    print(',')
    print("\"",end="")
    for i in range(changenum(a[0])-4,changenum(a[0])+5):
        if(i>=0 and i<15):
            print(h[i][changenum(a[1])],end="")
    print("\"",end="")
    print(',')
    print("\"",end="")
    
    b=changenum(a[0])-4
    for i in range(changenum(a[1])+4,changenum(a[1])-5,-1):
        if(i>=0 and i<15 and b>=0 and b<15):
            print(h[b][i],end="")
        b+=1
    print("\"",end="")
    print(',')
#获取每一行的值(坐标版)
def getlineplus(x,y):
    z=""
    global maxpoint
    point=0
    h[x][y]='C'
    """
    for i in range(15):
            print()
            for j in range(15):
                print(h[i][j],end="")
    """
    #print()
    #print("\"",end="")
    for i in range(y-5,y+6):
        if(i>=0 and i<15):
            #print(h[x][i],end="")
            z+=str(h[x][i])
    #print("\"",end="")
    #print(',')
    point+=pointcheck(z)
    #print(pointcheck(z))
    z=""
    #print("\"",end="")
    b=x-5
    for i in range(y-5,y+6):
        if(i>=0 and i<15 and b>=0 and b<15):
            #print(h[b][i],end="")
            z+=str(h[b][i])
        b+=1
    #print("\"",end="")
    #print(',')
    point+=pointcheck(z)
    #print(pointcheck(z))
    z=""
    #print("\"",end="")
    for i in range(x-5,x+6):
        if(i>=0 and i<15):
            #print(h[i][y],end="")
            z+=str(h[i][y])
    #print("\"",end="")
    #print(',')
    point+=pointcheck(z)
    #print(pointcheck(z))
    z=""
    #print("\"",end="")
    b=x-5
    for i in range(y+5,y-6,-1):
        if(i>=0 and i<15 and b>=0 and b<15):
            #print(h[b][i],end="")
            z+=str(h[b][i])
        b+=1
    #print("\"",end="")
    #print(',')
    point+=pointcheck(z)
    if(maxpoint<point):
        maxpointpos.clear()
        maxpoint=point
        maxpointpos.append(changeletter(x,y))
    elif(maxpoint==point):
        maxpointpos.append(changeletter(x,y))
    #print(pointcheck(z))
    z=""
    #print(maxpoint)
    #print(maxpointpos)
    h[x][y]="."
#获取每一行的值(坐标版)
def getlinepluss(x,y):
    z=""
    global maxpoint
    point=0
    h[x][y]='C'
    for i in range(15):
            print()
            for j in range(15):
                print(h[i][j],end="")
    print()
    print("\"",end="")
    for i in range(y-5,y+6):
        if(i>=0 and i<15):
            print(h[x][i],end="")
            z+=str(h[x][i])
    print("\"",end="")
    print(',')
    point+=pointcheck(z)
    print(pointcheck(z))
    z=""
    print("\"",end="")
    b=x-5
    for i in range(y-5,y+6):
        if(i>=0 and i<15 and b>=0 and b<15):
            print(h[b][i],end="")
            z+=str(h[b][i])
        b+=1
    print("\"",end="")
    print(',')
    point+=pointcheck(z)
    print(pointcheck(z))
    z=""
    print("\"",end="")
    for i in range(x-5,x+6):
        if(i>=0 and i<15):
            print(h[i][y],end="")
            z+=str(h[i][y])
    print("\"",end="")
    print(',')
    point+=pointcheck(z)
    print(pointcheck(z))
    z=""
    print("\"",end="")
    b=x-5
    for i in range(y+5,y-6,-1):
        if(i>=0 and i<15 and b>=0 and b<15):
            print(h[b][i],end="")
            z+=str(h[b][i])
        b+=1
    print("\"",end="")
    print(',')
    point+=pointcheck(z)
    if(maxpoint<point):
        maxpointpos.clear()
        maxpoint=point
        maxpointpos.append(changeletter(x,y))
    elif(maxpoint==point):
        maxpointpos.append(changeletter(x,y))
    print(pointcheck(z))
    z=""
    print(maxpoint)
    #print(maxpointpos)
    h[x][y]="."


#检测该点是否有棋子
def piececheck(a,b):
    if(a>14 or a<0 or b>14 or b<0):
        return False
    if(hs[a][b]=='o' or hs[a][b]=='x'):
        return True
    else:
        return False
#检测可能落子的点
def pieceposcheck(a,b):
    if((piececheck(a+1,b) or piececheck(a-1,b) or
        piececheck(a+1,b+1) or piececheck(a-1,b-1) or 
        piececheck(a-1,b+1) or piececheck(a+1,b-1) or 
        piececheck(a,b+1) or piececheck(a,b-1)) and hs[a][b]=='.'):
        return True
    else:
        return False
#棋盘敌我装换
def atkdefchange(a):
    if(a=='x'):
        for i in range(15):
            for j in range(15):
                if(h[i][j]=='x'):
                    h[i][j]='M'
                elif(h[i][j]=='o'):
                    h[i][j]='O'
    elif(a=='o'):
        for i in range(15):
            for j in range(15):
                if(h[i][j]=='x'):
                    h[i][j]='O'
                elif(h[i][j]=='o'):
                    h[i][j]='M'

#获取重复次数最多的坐标
def getposmax(a):
    maxposnum=1
    posindex=a[0]
    for b in a:
        if(maxposnum<a.count(b)):
            maxposnum=a.count(b)
            posindex=""
            posindex+=b
    return posindex
#判断落子位置
def getpos(l,chesscolor):
    m=0
    n=0
    global maxpoint
    maxpoint=-1
    
    """
    for i in range(15):
            print()
            for j in range(15):
                print(h[i][j],end="")
    print()
    for i in range(15):
            print()
            for j in range(15):
                print(hs[i][j],end="")
    print()
    """
    
    #导入棋子
    while m<len(l):
        if(n%2==0):
            h[changenum(l[m])][changenum(l[m+1])]='x'
            hs[changenum(l[m])][changenum(l[m+1])]='x'
        else:
            h[changenum(l[m])][changenum(l[m+1])]='o'
            hs[changenum(l[m])][changenum(l[m+1])]='o'
        m+=2
        n+=1
    
    #打印棋盘
    for i in range(15):
        #print()
        for j in range(15):
            if(pieceposcheck(i,j)):
                hs[i][j]='C'
            #print(hs[i][j] , end="")

    
    #print()
    atkdefchange(chesscolor)
    for i in range(15):
        for j in range(15):
            if(hs[i][j]=='C'):
                getlineplus(i,j)           
    #print()
    for i in range(15):
        for j in range(15):
            hs[i][j]='.'
    return getposmax(maxpointpos)


#初始化二维列表
win=["CMMMM","MCMMM","MMCMM","MMMCM","MMMMC"]#10000
mustdefense=["OOOOC","OCOOO","OOCOO","OOOCO","COOOO"]#6000
twowin=[".CMMM..",".MCMM.",".MMCM.","..MMMC."]#5000
twowins=["C.MMM","MMM.C"]#
twodefense=[".COOO..","..OOOC.",".OOCO.",".OCOO."]#2500
twodefenses=[".COOO.",".OOOC."]#2500
attack=["OCMMM.","OMCMM.","OMMCM.","OMMMC."
        ,".CMMMO",".MCMMO",".MMCMO",".MMMCO"
        ,".MC.MM.",".MM.CM.","..MMM.C","C.MMM.."
        ,".M.CMM.",".MMC.M."]#2000
twoattack=["..MMC..","..MCM..","..CMM.."]#400
twoattacks=[".C.MM.",".MM.C."]
defense=["..OOC..","..OCO..",".C.OO.",".OO.C.","..COO..","MOOOC.",".COOOM"]#400
noatkdef=[".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"]#200
layout=["...MC...","...CM..."]#500
hlow=["..OC..","..CO.."]#200
low=["..O.C..","..C.M..","..C.O..","..M.C.."]#100
#分数检测
def pointcheck(a):
    for b in win:
        if b in a:
            return 100000
    for b in mustdefense:
        if b in a:
            return 8000
    for b in twowin:
        if b in a:
            return 5000
    for b in twowins:
        if b in a:
            return 4900
    for b in attack:
        if b in a:
            return 3000
    for b in twodefense:
        if b in a:
            return 2500
    for b in twodefenses:
        if b in a:
            return 2000
    for b in twoattack:
        if b in a:
            return 800
    for b in twoattacks:
        if b in a:
            return 600
    for b in layout:
        if b in a:
            return 500
    for b in defense:
        if b in a:
            return 400
    for b in noatkdef:
        if b in a:
            return 300
    for b in hlow:
        if b in a:
            return 200
    for b in low:
        if b in a:
            return 100
    return 0
    
    
            
            
            
            
game_id=""
#check里面的数据
data={}
isplayed=False
wins=False

#hs为更新可落子位置的棋盘数据
##h为棋盘数据
h=[]
hs=[]
maxpointpos=[]
maxpoint=-1
for i in range(15):
    h.append([])
    hs.append([])
    for j in range(15):
        h[i].append('.')
        hs[i].append('.')
#(judge('ghfghggfehfffhhhgghfdhchefifjfigegeieeeddfgifdfjekcgficfcebdgjcicjdghkilgchbgldefcbgahejdiihiiieidjeijfmjikhjhhejgjjgk','o'))
#ghfghggfeh
#ghfghggfehfffhhhgghfdhchefifjfigegeieeeddfgifdfjekcgficfcebdgjcicjdghkilgchbgldefcbgahejdiihiiieidjeijfmjikhjhhejgjjgk
#ghfghggfehfffhhhgghfdhchefifjfigegeieeeddfgifdfjekcgficfcebdgjcicjdghkilgchbgldefcbgahejdiihiiieidjeijfmjikhjhhejgjjgkfegedccbkelefkflhjel
#judge('ghfghggfehfffhhhgghfdhchefifjfigegeieeeddfgifdfjekcgficfcebdgjcicjdghkilgchbgldefcbgahejdiihiiieidjeijfmjikhjhhejgjjgk','o')



user='阿尔法猫'
password='123321'
duankou='8000'
#连接游戏
def connect_game():
    global game_id
    payload = {'user': user,
           'password':password,
           'data_type':'json' }
    ret = requests.get('http://183.175.12.27:'+duankou+'/join_game/', params=payload)
    #print(ret.url)
    #print(ret.json())
    if(ret.json()['is_success']):
        game_id+=str(ret.json()['game_id'])
        print(game_id)
    else:
        print("game_id error")
        game_id="null"
#检查游戏状态
def check_game(data):
    if(game_id=="null"):
        print("game_id error")
        return 0
    
    ret = requests.get('http://183.175.12.27:'+duankou+'/check_game/'+game_id)
    #print(ret.url)
    #print(ret.json())
    data=ret.json()
    #print(data)
    if(data.get('winner')!='None'):
        print(data.get('winner')+"获胜")
        global wins
        wins=True
        return
    if(data.get('ready')=='False'):
        print('正在匹配对手')
    else:
        l=''
        l+=str(data.get('board'))
        check_data(data)
#返回落子位置
def play_game(coord):
    global game_id
    payload = {'user': user,
           'password':password,
           'coord': coord }
    ses=requests.session()
    ses.get('http://183.175.12.27:'+duankou+'/play_game/'+game_id, params=payload)
    #print(ret.url)
    #print(ret.json())
    print("落子成功"+coord)
    global isplayed
    isplayed=True
#落子判断
def check_data(data):
    print(data)
    global isplayed
    if(data.get('current_turn')==user and not isplayed):
        print("我方正在落子")
        if(data.get('board')==''):
            play_game('hh')
        else:
            play_game(getpos(data.get('board'),data.get('current_stone')))
            printboard(data.get('board'),getpos(data.get('board'),data.get('current_stone')))
            time.sleep(1)
    else:
        isplayed=False
        print("对方正在落子")
#获取每个人的最佳落点 
#打印棋盘
def printboard(l,pos):
    letter=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    m=0
    n=0
    while m<len(l):
        if(n%2==0):
            h[changenum(l[m])][changenum(l[m+1])]='x'
        else:
            h[changenum(l[m])][changenum(l[m+1])]='o'
        m+=2
        n+=1
    for i in range(16):
        print()
        if(i==0):
            for j in letter:
                print(j,end=" ")
            continue
        for j in range(15):
            if(j==0):
                print(letter[i],end=" ")
            if(j==changenum(pos[0]) and i-1==changenum(pos[1])):
                h[j][i-1]='C'
            print(h[j][i-1],end=" ")
    for i in range(15):
        for j in range(15):
            h[i][j]='.'

game_id=""
#check里面的数据
isplayed=False
wins=False
password=format(quick_algorithm(asc(password),65537,135261828916791946705313569652794581721330948863485438876915508683244111694485850733278569559191167660149469895899348939039437830613284874764820878002628686548956779897196112828969255650312573935871059275664474562666268163936821302832645284397530568872432109324825205567091066297960733513602409443790146687029),"x")
#print(getpos('hhighghfjhihiigghihjjigikilijjjkkklljgjfiklhhlgmkjljlkklmlnmkhkgielglfminjifgflm','x'))





connect_game()
while not wins:
    data={}
    check_game(data)
    time.sleep(1)




































































ls=["hhifhjigkhjghghiihjhkjjijjij",
    "hhigjhihjgiiifhgjijfkhkeli",
    "hhjhiijjkijijkjgjfkhijiflihegdlh", 
    "hhkhlhihkgjimijfnjoklgjhjgigmgnglfli", 
    "hhjhihjiijjjjgjkjliihigjkgigkflehf", 
    "edfefdgdeeefhcdffccfffdddegbgcecicjchb",
    "gheifhiihhihhiijighg", 
    "hhjhiijgghjjjkjijfkjig",
    "ggffhggfhffgiefhfeheidehdidhgheg",
    "hhjhiijgghjjjkjijfkjiggiijih",
    "hhjhiijgghjjjkjijfkjiggi", 
    "ghhihhhggiggihfhigfjiiifjh", 
    "hhggfhghifgigfgjgkhfhkhiijfgjikh", 
    "hhihgihijgiiigjffjekgghggjghijhjgkiffijekdkfgl",
    "hhjhihjiijjjjgjkjlii", 
    "hhjhihjiijjjjgjkjliihigjkgigkflehfhgifjf", 
    "ghhihhhggiggihfhigfjiiifjhkhjgjfhfgekfijkg"]
llll=['x','o','x','x','o','o','x','o','x','x','x','o','x','o','x','x','o']
#ls=["hhifhjigkhjghghiihjhkjjijjij"]
#print(judge('',llll[0]))
asdf=0
for l in ls:
    #print(judge(l,llll[asdf]))
    asdf+=1
#ki,he,ih,le,hg,ia,eh,gi,ci,hi,ke,kh,gl,gm,hi,kh,hj
"""
for i in range(15):
        print()
        for j in range(15):
            print(h[i][j],end="")
print()
"""







"""
atkdefchange(1);
for i in range(15):
        print()
        for j in range(15):
            print(hs[i][j],end="")
for i in range(15):
        for j in range(15):
            if(hs[i][j]=='C'):
                getlineplus(i,j)
"""














"""
o= ["nk", "ok", "bn", "ef", "lk", "im", "gb", "fd", "ha"]
#getline("fd")
#print(quick_algorithm(5,8,11))

for p in o:
    getline(p)
"""