//example for playing rock, paper, scissors - final project for CS 131

#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

//this will hold the computer choose which would be randomly chosen
string GatherCompChoice() {
	string choices[] = { "rock", "paper", "scissors" };
	return choices[rand() % 3];		//this will return the random choice of the computer
}
 
string Winner(string UserChoice,string CompChoice) {
	if (UserChoice == CompChoice) {
		return "It's a tie!";
	}
	else if ((UserChoice == "rock" && CompChoice == "scissors") || (UserChoice == "paper" && CompChoice == "rock") || (UserChoice == "scissors" && CompChoice == "paper")) {
		return "Congrations! You win!";
	}
	else {
		return "The Computer wins!";
	}
}

int main() {
	string UserChoice;
	char PlayAgain;
	srand(time(0));		//seed a random number generator

	cout << "  Welcome! Let's play Rock, Paper, Scissors! " << endl;
	cout << "----------------------------------------------" << endl;
	cout << "    Will you be the one to win today? " << endl;

	do {
		cout << endl;
		cout << "Enter rock, paper, scissors: ";
		cin >> UserChoice;

		string CompChoice = GatherCompChoice();
		cout << "\nComputer choice: " << CompChoice << endl;
		cout << Winner(UserChoice, CompChoice) << endl;

		cout << "Do you want to play again? (Y/N) : ";
		cin >> PlayAgain;
	} while (PlayAgain == 'y' || PlayAgain == 'Y');
	cout << "\nThank you for playing! " << endl << "Hope to see you soon! " << endl;

	return 0;
}
