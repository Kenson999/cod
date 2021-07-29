let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];
console.log(secretMessage.length);//output24
secretMessage.pop();
console.log(secretMessage.length);//output23
secretMessage.push('to','Program');
console.log(secretMessage);
//secretMessage[7] = 'right';
let newSecrtMessage = secretMessage.map ( item =>{
    if (item === 'easily') {
        return 'right'
    }   else {
        return item
    }
})
console.log(secretMessage);
secretMessage.shift();//remove the first string 
console.log(secretMessage);
secretMessage.unshift('Programming');
console.log(secretMessage);
console.log(secretMessage.length);
//secretMessage.splice(6, 5, 'know')
//let removingWords = new Set('get', 'right', 'the','first', 'time')
//secretMessage.map (item => {
//    if (removingWords.has(item)) {
//        return 'know'
// } else {
//        return item
//    
//    }
//})
console.log(secretMessage);
console.log(secretMessage.length);
console.log(secretMessage.join(' '));