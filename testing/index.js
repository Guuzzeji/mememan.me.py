let fetch = require('node-fetch');

const fs = require('fs');
const contents = fs.readFileSync('./test.jpg', { encoding: 'base64' });

// console.log(contents);

let body = {
    data: 'data:image/png;base64,' + contents
};

// let body = {
//     data: contents
// };

// for (let x = 0; x < 100;) {
//     fetch('http://127.0.0.1:5000/API/upload', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(body)

//     }).then(function (res) {
//         x++;
//         console.log(res);
//         return res.json();
//     });
// }

fetch('http://127.0.0.1:3000/API/upload', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)

}).then(function (res) {
    console.log(res);
    return res.json();
}).then(function (data) {
    console.log(data);
    fs.writeFileSync('out.txt', data.img, function (err) {
        console.log(err);
    });
});