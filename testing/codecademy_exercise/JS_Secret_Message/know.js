let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];
console.log(secretMessage.length);//output24
secretMessage.pop();
console.log(secretMessage.length);//output23
secretMessage.push('to','Program');
console.log(secretMessage);
secretMessage[7] = 'right';
console.log(secretMessage);
secretMessage.shift();//emove the first string 
console.log(secretMessage);
secretMessage.unshift('Programming');
console.log(secretMessage);
console.log(secretMessage.length);
secretMessage.splice(6, 5, 'know','know','know','know','know')
console.log(secretMessage);
console.log(secretMessage.length);
console.log(secretMessage.join(' '));