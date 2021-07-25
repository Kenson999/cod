const geT = () => {
    const randomNumber = Math.floor(Math.random() * 5) ;
    switch (randomNumber) {
        case 0:
            return 'TOM';
        case 1:
            return 'PETER';
        case 2:
            return 'MARY';
        case 3:
            return 'AMY';
         case 4:
            return 'ALEX';
            
    }
};
const go = geT();
console.log(go)


function getRandomNum(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  getRandomNum(5, 10) // 隨機回傳 5 - 10 之間的整數
  let arr = ['Dylan', 'Jack', 'Ralph', 'Tom', 'Rex']
  console.log(arr[getRandomNum(0, arr.length - 1)]) // 回傳 arr 中隨機成員