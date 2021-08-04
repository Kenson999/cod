// let arr3 = ['A', 'B', 'C', 'D', 'E']
// console.log(arr3[Math.floor(Math.random()*arr3.length)])
//////////////////////////////////////////////////////////////
const arr = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', ]
const s2 = 100; //speed ++
function randArr(num) {
    for (let i = 0; i < num; i++) {
        let iRand = parseInt(num * Math.random()); 
        let temp = arr[i];                         
        arr[i] = arr[iRand];                       
        arr[iRand] = temp;                        
    }
    return arr;                                    
}

const arrr = randArr(arr.length);



function s1 () {
    let s = 0;
    s1 = function () {
      return s++;
    };
    return s++;
  }

//const s1 = s2*s1(); //CANT WORK
//   console.log(s1());
//   console.log(s1());
//   console.log(s1());
//   console.log(s1());

function z () {
  let z1 = 0;
  z = function () {
    return z1++;
  };
  return z1++;
}

  function c1 () {
    let c = arr.length -1;
    c1 = function () {
      return c--;
    };
    return c--;
  }
//   console.log(c1());
//   console.log(c1());
//   console.log(c1());


setTimeout( () => {console.log('Top:' + randArr(arr.length)[0])}, s2*s1())
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(':')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log(c1()+(' :')+arrr[z()])}, s2*s1());
setTimeout( () => {console.log('------------------')}, s2*s1());
setTimeout( () => {console.log('------------------')}, s2*s1());
setTimeout( () => {console.log('------------------')}, s2*s1());
setTimeout( () => {console.log(('bomb:')+arrr[z()])}, s2*s1());

// setTimeout( () => {console.log('Random list:' + arrr)}, s2*s1());
// setTimeout( () => {console.log(`Random list:${arrr}`)}, s2*s1());
setTimeout( () => {console.log(arrr)}, s2*s1());
