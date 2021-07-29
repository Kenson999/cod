const getUserChoice = userInput => {
    if (userInput === 'rock' || userInput === 'cut' || userInput === 'paper') {
        return userInput;
    } else {
        console.log('Error,pls type: rock ,paper or cut')
    }
}


const getComputerChoice = () => {
    const randomNumber = Math.floor(Math.random() * 3) ;
    switch (randomNumber) {
        case 0:
            return 'rock';
        case 1:
            return 'paper';
        case 2:
            return 'cut';
    }
};


const determaineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice) {
        return 'This game is a tie!';
    }
    if (userChoice === 'rock') {
        if (computerChoice === 'paper') {
            return 'Sorry, computer won!';
        } else {
            return 'Congratulations, you won!1';
        }
    }
if (userChoice === 'paper') {
    if (computerChoice === 'cut') {
        return 'Sorry,computer won!';
    } else {
        return 'Congratulations, you won!2'
    }
  }

if (userChoice === 'cut') {
    if (computerChoice === 'rock') {
        return 'Sorry ,computer won!'
    } else {
        return 'Congratulations, you won!3'
    }
}
}
const playGame = () => {
    const userChoice = getUserChoice('cut');
    const computerChoice = getComputerChoice();
    console.log('You threw:'+ userChoice);
    console.log('The computer threw: '+ computerChoice);
    console.log(determaineWinner(userChoice, computerChoice))
};


playGame()
