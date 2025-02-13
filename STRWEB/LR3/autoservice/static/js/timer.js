function startTimer(duration, display) {
    let timer = duration;
    let minutes, seconds;

    const intervalId = setInterval(() => {
        minutes = Math.floor(timer / 60);
        seconds = timer % 60;


        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = `${minutes}:${seconds}`;

        if (--timer < 0) {
            clearInterval(intervalId);
            display.textContent = "Время вышло!";
        }
    }, 1000);
}


document.addEventListener("DOMContentLoaded", () => {
    const display = document.getElementById("timer"); // Элемент для отображения таймера
    const duration = 60 * 60 - 1; // 1 час в секундах
    startTimer(duration, display); // Запускаем таймер

});