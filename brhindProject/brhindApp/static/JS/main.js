const btn = document.querySelector('.nav-link');

if (btn === true){
    btn.addEventListener('click', () => {
    btn.style.color = '#adff2fff';
    btn.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".nav-link").addEventListener('afterclick', () => {
    btn.style.color = '#fff';
    btn.style.borderTop = '0';
})
}

let btn1 = document.querySelector('.a');

if (btn1 === true){
    btn1.addEventListener('click', () => {
    btn1.style.color = '#adff2fff';
    btn1.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".a").addEventListener('afterclick', () => {
    btn1.style.color = '#fff';
    btn1.style.borderTop = '0';
})
}


const btn2 = document.querySelector('.b');

if (btn2 === true){
    btn2.addEventListener('click', () => {
    btn2.style.color = '#adff2fff';
    btn2.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".b").addEventListener('afterclick', () => {
    btn2.style.color = '#fff';
    btn2.style.borderTop = '0';
})
}

const btn3 = document.querySelector('.c');

if (btn3 === true){
    btn3.addEventListener('click', () => {
    btn3.style.color = '#adff2fff';
    btn3.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".c").addEventListener('afterclick', () => {
    btn3.style.color = '#fff';
    btn3.style.borderTop = '0';
})
}


const btn4 = document.querySelector('.d');

if (btn4 === true){
    btn4.addEventListener('click', () => {
    btn4.style.color = '#adff2fff';
    btn4.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".d").addEventListener('afterclick', () => {
        btn4.style.color = '#fff';
        btn4.style.borderTop = '0';
    })
}

const btn5 = document.querySelector('.e');

if (btn5 === true){
    btn5.addEventListener('click', () => {
    btn5.style.color = '#adff2fff';
    btn5.style.borderTop = '1px solid #adff2fff';
});
}
else {
    document.querySelector(".e").addEventListener('afterclick', () => {
    btn5.style.color = '#fff';
    btn5.style.borderTop = '0';
})
}



let color_nav = document.getElementById("nav");

window.onscroll = function () {
    let lenWindow = window.pageYOffset
    console.log(lenWindow)
    if (lenWindow > 100) {
        color_nav.style.backgroundImage = "linear-gradient(to bottom, #43ff0057, #43ff007d, #43ff009c, #43ff00ab, #43ff00)";
    }
    if (lenWindow < 99) {
        color_nav.style.backgroundImage = "none";
    }
}



const karousel = document.querySelector(".karousel");
firstImg = karousel.querySelectorAll("img")[0];
arrowIcons = document.querySelectorAll(".wrapper i");

let isDragStart = false, prevPageX,  prevScrollLeft, positionDiff;
let firstImgWidth = firstImg.clientWidth + 14;

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        karousel.scrollLeft += icon.id == "left" ? - firstImgWidth : firstImgWidth;
    });
});

const dragStart = (e) => {
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = karousel.scrollLeft;
}

const dragging = (e) => {
    if (!isDragStart) return;
    e.preventDefault();
    // isDragging = true;
    karousel.classList.add("dragging");
    positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX;
    karousel.scrollLeft = prevScrollLeft - positionDiff;
}

const dragStop = () => {
    isDragStart = false;
    karousel.classList.remove("dragging");


    // if(!isDragging) return;
    // isDragging = false;
    // autoSlide();
}

karousel.addEventListener("mousedown", dragStart);
karousel.addEventListener("touchstart", dragStart);

karousel.addEventListener("mousemove", dragging);
karousel.addEventListener("touchmove", dragging);

karousel.addEventListener("mouseup", dragStop);
karousel.addEventListener("touchend", dragStop);



function showPay(){
    var payMethod = document.getElementById('show')

    if(payMethod.style.display === 'block' ){
        payMethod.style.display = 'none'
    } else {
        payMethod.style.display = 'block'
    }
}







