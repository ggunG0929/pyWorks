window.onload = function(){
    // 배경 이미지 슬라이딩
    // 경로 주의 - static 폴더에서 시작함
    let picture = [
        "../static/images/header1.jpg",
        "../static/images/header2.jpg",
        "../static/images/header3.jpg"
    ]
    let imgIdx = 0;
    showPicture(); // showPicture() 함수 호출
    function showPicture(){
        let img = document.getElementById('pic');
        img.src = picture[imgIdx]   // 첫 이미지 저장
        imgIdx++;
        if(imgIdx == picture.length){   // = imgIdx == 3와 같은 의미
            imgIdx = 0;
        }
        // 3초 간격으로 showPicture() 호출
        setTimeout(showPicture, 3000);
    }
    // 디지털 시계
    if (window.location.href == 'http://127.0.0.1:5000/'){
        setInterval(setWatch,1000);
    }
        function setWatch(){
            const date = new Date();
            let now = date.toLocaleTimeString();    // 시간 형식
            document.getElementById("demo").innerHTML = now;
        }
}