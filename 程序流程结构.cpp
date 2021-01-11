#include<iostream>
#include<string>
using namespace std;
int main()
{
//	int score;
//	cout << "请输入你的高考分数：" << endl;
//	cin >> score;
//	cout << "你输入的分数为：" << score << endl;
//	if (score > 600)
//	{
//		if (score > 700)
//		{
//			cout << "不错啊，应该可以上北大清华了！" << endl;
//		}
//		else if (score > 650)
//		{
//			cout << "你可以考进人大了！" << endl;
//		}
//		else
//		{
//			cout << "你可以考入一个好的一本大学！" << endl;
//		}
//
//	}
//	else if (score > 500)
//	{
//		cout << "你这个分数应该可以上一个二本！" << endl;
//	}
//	else if (score > 400)
//	{
//		cout << "你这个分数应该可以上一个三本！" << endl;
//	}
//	else
//	{
//		cout << "很遗憾，你的分数没有上400，可能上不了本科！" << endl;
//	}
//三只小猪称体重小游戏
int pig1;
int pig2;
int pig3;
int demo;
cout << "请输入三只小猪各自的体重：" << endl;
cout << "小猪1：" << endl;
cin >> pig1;
cout << "小猪2：" << endl;
cin >> pig2;
cout << "小猪3：" << endl;
cin >> pig3;
if (pig1 > pig2)//小猪1比小猪2重
{
	if (pig1 > pig3)//小猪1比小猪3重
	{
		cout << "小猪1最重!" << endl;
	}
	else//小猪1没有小猪3重
	{
		cout << "小猪3最重！" << endl;
	}
}
else//小猪2比小猪1重
{
	if (pig2 > pig3)//小猪2比小猪3重
	{
		cout << "小猪2最重！" << endl;
	}
	else//小猪2没有小猪3重
	{
		cout << "小猪3最重！" << endl;
	}
}
	system("pause");
	return 0;
}
