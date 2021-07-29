
const userInput = () => {
  const nUm = (Math.floor(Math.random() * 3 ));
  if(nUm == 0){
    return 'rock'
  }else if(nUm == 1){
    return 'paper'
  }else{
    return 'cut'
  }
  }


const getComputerChoice = () => {
 const nUm = (Math.floor(Math.random() * 3 ));
if(nUm == 0){
  return 'rock'
}else if(nUm == 1){
  return 'paper'
}else{
  return 'cut'
}
}

getComputerChoice()





const userChoice = userInput();
const computerChoice = getComputerChoice();

const determineWinner = () => {
  if (userChoice == computerChoice) {
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
  }else {
    return 'User win'
}
}

const playGame = () => {
  console.log(`User: ${userChoice}`)
  console.log(`COM:　${computerChoice}`)
  console.log(determineWinner())
}

playGame();
