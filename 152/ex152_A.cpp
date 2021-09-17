/*
高橋君は、プログラミングコンテストAXC001に参加しており、
問題Aにコードを提出しました。

この問題にはN個のテストケースがあり、全てのテストケースに
正解した場合ににみ提出はACとなります。

高橋君の提出は、N個のテストケースのうちM個のテストケースに
正解しました。
高橋君の提出が、ACとなるか判定してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
	int N,M;

	cin>>N>>M;
	
	if(N==M){
		cout<<"Yes"<<endl;
	}else{
		cout<<"No"<<endl;
	}
	return 0;
}
	
