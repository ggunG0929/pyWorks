setInterval(setWatch,1000);
    function setWatch(){
        const date = new Date();
        let now = date.toLocaleTimeString();    // 시간 형식
        document.getElementById("demo").innerHTML = now;
    }