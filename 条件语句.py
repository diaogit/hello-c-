#单分支结构
#score=70
#if score>60:
#    print('你的成绩及格了！');
#    pass
#双分支结构
#if score>90:
#    print('你的成绩大于90分了，真厉害！');
#    pass;
#else:
#    print("你的成绩没有达到90分！");
#    pass;
#多分支结构
#猜拳小游戏 0：石头 1：剪刀 2：布
import random;
print("0：石头 1：剪刀 2：布");
people=int(input('请出拳:'));
computer=random.randint(0,2);
if(people==0 and computer==1):
    print("你出的是石头，电脑出的是剪刀，你赢了！");
    pass;
elif(people==1 and computer==2):
    print("你出的是剪刀，电脑出的是布，你赢了！");
    pass;
elif(people==2 and computer==0):
    print("你出的是布，电脑出的是石头，你赢了！");
    pass;
elif(people==computer):
  print("你们出的都是一样的，平局！");
  pass;
else:
    print('你输了！');
    pass;
xf=int(input("请输入你的学分："));
if(xf>10):
    cj=int(input("请输入你的成绩："));
    if(cj>80):
        print("恭喜你，表现很好！回家不会被清炒竹笋了！");
        pass;
    else:
        print("你的学分虽然合格了，但很可惜成绩不合格，回家可能会被清炒竹笋哦！");
        pass;
    pass;
else:
    print("你小子也太差劲了吧！连学分都不合格，回家叫你家长来！");
