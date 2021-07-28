const input = 'introduction-to-javascript'//26.length
const vowels = ['a','e','i','o','u']//5.length
const box = []
for (let i = 0;i < input.length;i++){      //從單字母開始check
  for (let j = 0; j < vowels.length;j++){ //
    if(input[i] == vowels[j]){
      box.push(input[i] )
     if (vowels[j] == 'u'){
       box.push(vowels[j])
     } else if (vowels[j] == 'e'){
      box.push(vowels[j])
         
      }
  }

}
}
 console.log(box.join('').toUpperCase())
console.log(vowels.length)