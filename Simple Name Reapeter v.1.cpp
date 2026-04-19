#include<iostream>
using namespace std;
int main(void){
	
	string name;
	int reap;
	
	cout<<"Enter Your Name: ";// input name:
	cin>>name;
	
	cout<<"Enter The Number You Have To Reapet Your Name: ";// Enter Number:
	cin>>reap;
	
	for(int i=1; i<=reap; i++){// Loop start: i++ will execute in last:
	    cout<<name<<i<<endl;// Print name And i for Numberic Idea: 
	}
	
	return 0;
}
