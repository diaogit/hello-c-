#include<iostream>
#include<string>
using namespace std;
int main()
{
//	int score;
//	cout << "��������ĸ߿�������" << endl;
//	cin >> score;
//	cout << "������ķ���Ϊ��" << score << endl;
//	if (score > 600)
//	{
//		if (score > 700)
//		{
//			cout << "������Ӧ�ÿ����ϱ����廪�ˣ�" << endl;
//		}
//		else if (score > 650)
//		{
//			cout << "����Կ����˴��ˣ�" << endl;
//		}
//		else
//		{
//			cout << "����Կ���һ���õ�һ����ѧ��" << endl;
//		}
//
//	}
//	else if (score > 500)
//	{
//		cout << "���������Ӧ�ÿ�����һ��������" << endl;
//	}
//	else if (score > 400)
//	{
//		cout << "���������Ӧ�ÿ�����һ��������" << endl;
//	}
//	else
//	{
//		cout << "���ź�����ķ���û����400�������ϲ��˱��ƣ�" << endl;
//	}
//��ֻС�������С��Ϸ
int pig1;
int pig2;
int pig3;
int demo;
cout << "��������ֻС����Ե����أ�" << endl;
cout << "С��1��" << endl;
cin >> pig1;
cout << "С��2��" << endl;
cin >> pig2;
cout << "С��3��" << endl;
cin >> pig3;
if (pig1 > pig2)//С��1��С��2��
{
	if (pig1 > pig3)//С��1��С��3��
	{
		cout << "С��1����!" << endl;
	}
	else//С��1û��С��3��
	{
		cout << "С��3���أ�" << endl;
	}
}
else//С��2��С��1��
{
	if (pig2 > pig3)//С��2��С��3��
	{
		cout << "С��2���أ�" << endl;
	}
	else//С��2û��С��3��
	{
		cout << "С��3���أ�" << endl;
	}
}
	system("pause");
	return 0;
}
