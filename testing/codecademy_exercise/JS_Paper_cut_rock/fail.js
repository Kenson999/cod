
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'cut') {
    return userInput;
  } else {
    console.log('E04')
  }
}

const getComputerChoice = () => {
 const rDn = (Math.floor(Math.random() * 3 ));
 switch (rDn) {
   case 0 :
   return 'rock';
   case 1 :
   return 'paper';
   case 2 :
   return 'cut';
  }
}







const determineWinner = (userChoice, computerChoice) => {
  if ( userChoice === computerChoice ) {
    return 'This is a tie'
  }else if ( userChoice === 'cut' && computerChoice === 'paper' ){
    return 'User win'
  }else if ( userChoice === 'paper' && computerChoice === 'cut' ) {
    return 'COM win'
  }else if ( userChoice === 'rock' && computerChoice === 'paper' ) {
        return 'COM win'
  }else if ( userChoice === 'paper' && computerChoice === 'rock' ) {
        return 'User win'
 }else if ( userChoice === 'cut' && computerChoice === 'rock' ){
    return 'COM win'
  }else if ( userChoice === 'rock' && computerChoice === 'cut' ){
    return 'User win'
}
}

const playGame = () => {
  const userChoice = getUserChoice('Rock');
  const computerChoice = getComputerChoice();
  console.log(`User: ${userChoice}`)
  console.log(`COM:　${computerChoice}`)
  console.log(determineWinner())
}

playGame();