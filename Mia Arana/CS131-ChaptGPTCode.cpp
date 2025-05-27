//ChatGPT code 
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

string getComputerChoice() {
    int choice = rand() % 3;
    switch (choice) {
    case 0: return "rock";
    case 1: return "paper";
    case 2: return "scissors";
    default: return "rock";
    }
}

string getWinner(string user, string computer) {
    if (user == computer) return "draw";
    if ((user == "rock" && computer == "scissors") ||
        (user == "paper" && computer == "rock") ||
        (user == "scissors" && computer == "paper")) {
        return "user";
    }
    else {
        return "computer";
    }
}

bool isValidChoice(string choice) {
    return choice == "rock" || choice == "paper" || choice == "scissors";
}

int main() {
    srand(time(0));
    string userChoice, computerChoice, winner;
    char playAgain;

    cout << "Welcome to Rock, Paper, Scissors!" << endl;

    do {
        cout << "\nEnter your choice (rock, paper, or scissors): ";
        cin >> userChoice;

        while (!isValidChoice(userChoice)) {
            cout << "Invalid choice. Try again (rock, paper, or scissors): ";
            cin >> userChoice;
        }

        computerChoice = getComputerChoice();
        cout << "Computer chose: " << computerChoice << endl;

        winner = getWinner(userChoice, computerChoice);

        if (winner == "draw") {
            cout << "It's a draw!" << endl;
        }
        else if (winner == "user") {
            cout << "You win!" << endl;
        }
        else {
            cout << "Computer wins!" << endl;
        }

        cout << "Do you want to play again? (y/n): ";
        cin >> playAgain;

    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "Thanks for playing!" << endl;
    return 0;
}
