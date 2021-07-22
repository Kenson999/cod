let raceNumber = Math.floor(Math.random() * 1000);
let earlyRegister = true;
let age = 17;

if(age > 18 && earlyRegister){
  raceNumber = raceNumber + 1000
}
if(age > 18 && earlyRegister){
  console.log(`${raceNumber}: Race start at 9:30am`)
}else if(age > 18 && !earlyRegister){
    console.log(`${raceNumber}: Race start at 11:00am`)
}else if (age < 18) {
      console.log(`${raceNumber}: Race start at 12:30am`)
}else {
  console.log(`Please go to registration desk`)
}
