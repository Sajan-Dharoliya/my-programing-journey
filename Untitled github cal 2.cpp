#include<iostream>
using namespace std;
int main(void){
   	
	int num1;
	int num2;
	char oper;
	char choice;
	
   do{
   	
   	cout<<"Enter first Number: "<<endl;
	cin>>num1;
	
	cout<<"Enter Second Number:"<<endl;
	cin>>num2;
	
	cout<<"Choose The Operation(=, -, *, /, %)"<<endl;
	cout<<"Operation : ";
	cin>>oper;
	
	int result;
	
	switch (oper){
		
		case '+':
			result=num1+num2;
			cout<<"Addition: "<<result<<endl;
			break;
			
	 	case '-':
	 		result=num1-num2;
	 		cout<<"Subtcraction: "<<result<<endl;
	 		break;
	 		
	 	case '*':
	 		result=num1*num2;
	 		cout<<"Multiplication: "<<result<<endl; 
			break;
			
		case '/':
			if(num2==0){
				cout<<"Cannot Divide By Zero!: "<<endl;
				break;
			}
			else if(num1==0){
				cout<<"Cannot Divide By Zero!: "<<endl;
			}
			result=num1/num2;
			cout<<"Division: "<<result<<endl;
			break;
			
		case '%':
			result=num1%num2;
			cout<<"Remender: "<<num1%num2<<endl;
			
		default:
			cout<<"Error: Invalid Input For Operation:"<<endl;
			break;
	}  	
	
	cout<<"Do You Want To Performe More Operations? (type Y for Yes Or Press Any Key For Exit):";
	cin>>choice;
	
   }while(choice == 'Y' || choice == 'y');
	
	
	return 0;
}
