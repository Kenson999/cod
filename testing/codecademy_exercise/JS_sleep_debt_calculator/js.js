const getSleepHours = (day) => {
  if (day === 'mon'){
    return 8;
  } else if (day === 'tue'){
      return 8;
  } else if (day === 'wed'){
      return 8;
  } else if (day === 'thu'){
      return 8;
  } else if (day === 'fir'){
      return 8;
  } else if (day === 'sat'){
      return 4;
  } else if (day === 'sun'){
      return 4;
}
}

const getActualSleepHours = () => getSleepHours('mon') + getSleepHours('tue') + getSleepHours('wed') + getSleepHours('thu') + getSleepHours('fir') + getSleepHours('sat') + getSleepHours('sun');

const getIdealSleepHours = () => {
  let idealHours = 7.5;
  return idealHours * 7;
};

console.log(getIdealSleepHours())

const calculateSleepDebt = () =>{
let actualSleepHours = getActualSleepHours();
let idealSleepHours  = getIdealSleepHours();
  if(actualSleepHours == idealSleepHours){
  console.log(`${actualSleepHours}perfect amount of sleep.`)
  } else if(actualSleepHours > idealSleepHours){
  console.log(`${actualSleepHours}user got more sleep than needed.`)
  } else if(actualSleepHours < idealSleepHours){
  console.log(`${actualSleepHours}user should get some rest`)
  }
  
 };
calculateSleepDebt();

