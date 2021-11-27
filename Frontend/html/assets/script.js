'use strict';

console.log('loaded');

const apiRoot = 'http://192.168.0.85';
const getImg = apiRoot + '/api/img';
const getData = apiRoot + '/api/data';
const setStatus = apiRoot + '/api/status/on';

const eImgA = document.getElementById('imgA');
const eImgB = document.getElementById('imgB');
const etagA = document.getElementById('tagA');
const etagB = document.getElementById('tagB');
const eLong = document.getElementById('long');
const eAngle = document.getElementById('angle');
const eMsg = document.getElementById('msg');
const eTags = document.getElementById('tags');

let timer = -1;

function start() {
    fetch(setStatus)
        .then(async response => {
            if (response.status === 200) {
                eMsg.innerText = '连接成功';
            } else {
                console.error(response);
                eMsg.innerText = '连接失败';
            }
        })
        .catch(error => {
            console.error(error);
            eMsg.innerText = '连接失败';
        });
    if (timer === -1) {
        timer = setInterval(function () {
            updateData();
        }, 1500);
    }
}

function updateImg() {
    fetch(getImg)
        .then(async response => {
            if (response.status === 200) {
                let { imgA, imgB } = await response.json();
                eImgA.src = imgA;
                eImgB.src = imgB;
                eMsg.innerText = '连接成功';
            } else {
                console.error(response);
                eImgA.src = '';
                eImgB.src = '';
                eMsg.innerText = '连接失败';
            }
        })
        .catch(error => {
            console.error(error);
            eImgA.src = '';
            eImgB.src = '';
            eMsg.innerText = '连接失败';
        });
}

function updateData() {
    fetch(getData)
        .then(async response => {
            if (response.status === 200) {
                let { long, angle, readyA, readyB } = await response.json();
                eLong.innerText = long;
                eAngle.innerText = angle;
                etagA.innerText = '视角A：' + (readyA ? '闲置' : '测量中');
                etagB.innerText = '视角B：' + (readyA ? '闲置' : '测量中');
                eMsg.innerText = '连接成功';
            } else {
                console.error(response);
                eLong.innerText = '计算中';
                eAngle.innerText = '计算中';
                eMsg.innerText = '连接失败';
            }
        })
        .catch(error => {
            console.error(error);
            eLong.innerText = '计算中';
            eAngle.innerText = '计算中';
            eMsg.innerText = '连接失败';
        });
}

setInterval(function () {
    updateImg();
}, 200);

timer = setInterval(function () {
    updateData();
}, 1500);

eTags.addEventListener('click', start);

eImgA.addEventListener('click', () => {
    if (timer === -1) {
        timer = setInterval(function () {
            updateData();
        }, 1500);
    }
});

eImgB.addEventListener('click', () => {
    if (timer !== -1) {
        clearInterval(timer);
        timer = -1;
    }
});
