document.querySelectorAll(".video_container video").forEach(video1 =>{
    video1.onclick = () => {
        document.querySelector('.popup_video').style.display = 'block';
        document.querySelector('.popup_video video').src = video1.getAttribute('src');
    }
});

document.querySelector('.popup_video span').onclick = () => {
    document.querySelector('.popup_video').style.display = 'none';
}


document.querySelectorAll(".video_container img").forEach(img =>{
    img.onclick = () => {
        document.querySelector('.popup_image').style.display = 'block';
        document.querySelector('.popup_image img').src = img.getAttribute('src');
    }
});

document.querySelector('.popup_image span').onclick = () => {
    document.querySelector('.popup_image').style.display = 'none';
}