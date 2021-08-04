// let arr3 = ['A', 'B', 'C', 'D', 'E']
// console.log(arr3[Math.floor(Math.random()*arr3.length)])
//////////////////////////////////////////////////////////////
const arr = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', ]
function randArr(Input) {
    for (let i = 0; i < Input; i++) {
        let iRand = parseInt(Input * Math.random()); 
        let temp = arr[i];                         
        arr[i] = arr[iRand];                       
        arr[iRand] = temp;                        
    }
    return arr;                                    
}

const arrr = randArr(arr.length);

setTimeout( () => {console.log('Top:' + randArr(arr.length)[0])}, 1000)
setTimeout( () => {console.log('-20:' + arrr[0])}, 2000);
setTimeout( () => {console.log('-19:' + arrr[1])}, 2200);
setTimeout( () => {console.log('-18:' + arrr[2])}, 2400);
setTimeout( () => {console.log('-17:' + arrr[3])}, 2600);
setTimeout( () => {console.log('-16:' + arrr[4])}, 2800);
setTimeout( () => {console.log('-15:' + arrr[5])}, 3000);
setTimeout( () => {console.log('-14:' + arrr[6])}, 3200);
setTimeout( () => {console.log('-13:' + arrr[7])}, 3500);
setTimeout( () => {console.log('-12:' + arrr[8])}, 3800);
setTimeout( () => {console.log('-11:' + arrr[9])}, 4100);
setTimeout( () => {console.log('-10:' + arrr[10])}, 4400);
setTimeout( () => {console.log('-9:' + arrr[11])}, 4700);
setTimeout( () => {console.log('-8:' + arrr[12])}, 5000);
setTimeout( () => {console.log('-7:' + arrr[13])}, 5500);
setTimeout( () => {console.log('-6:' + arrr[14])}, 6000);
setTimeout( () => {console.log('-5:' + arrr[15])}, 6500);
setTimeout( () => {console.log('-4:' + arrr[16])}, 7000);
setTimeout( () => {console.log('-3:' + arrr[17])}, 7500);
setTimeout( () => {console.log('-2:' + arrr[18])}, 8000);
setTimeout( () => {console.log('------')        }, 8500);
setTimeout( () => {console.log('------------')  }, 9000);
setTimeout( () => {console.log('------------------' )}, 9500);
setTimeout( () => {console.log('---------Winner:' + arrr[19] + '---------')}, 10000);

setTimeout( () => {console.log('Random list:' + arrr)}, 10500);
setTimeout( () => {console.log(`Random list:${arrr}`)}, 10500);
setTimeout( () => {console.log(arrr)}, 10500);
