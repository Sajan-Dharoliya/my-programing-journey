#include<iostream>               
using namespace std;
int main(void){
	
	string name;
	int reap;
	
	cout<<"Enter Your Name: ";// Enter Your Name:
	cin>>name;
	

	
   if(name!="sajan"){
  
	cout<<"Enter Correct Name!"<<endl;//Enter Your Correct Name:
	
	for(int i=1; i<=reap; i++){// Loop
	    cout<<name<<i<<endl;
	    
	}
	
 	}
 	
 	else{
 		
 		cout<<"Enter The Number You Have To Reapet Your Name: ";
	    cin>>reap;//Enter number
	    
	    for(int i=1; i<=reap; i++){// Loop
	    cout<<name<<i<<endl;
	    
	}
	 }
	return 0;
}
