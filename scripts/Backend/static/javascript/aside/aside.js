function createAsideButtions(){
    const readLine = require('readline');
    const f = require('fs');
    var file = './scripts/Backend/static/javascript/aside/list_of_buttons.txt';
    var rl = readLine.createInterface({
        input : f.createReadStream(file),
        output : process.stdout,
        terminal: false
    });
    rl.on('line', function (text) {
        console.log(text);
    });
}