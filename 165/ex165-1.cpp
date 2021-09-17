#include<iostream>
#include<stdio.h>
using namespace std;

int main(){

	int k,a,b;
	bool flag =0;

	cin>>k>>a>>b;

	for(int i= a;i<=b;i++){
		if(i%k ==0){
			flag =1;
			break;
		}
	}

	if(flag==1){
		cout<<"OK"<<endl;
	}else{
		cout<<"NO"<<endl;
	}
}
