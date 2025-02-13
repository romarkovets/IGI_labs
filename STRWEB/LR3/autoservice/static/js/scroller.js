document.addEventListener("scroll", () => {
    const tools = document.querySelectorAll(".tool");
    const car = document.querySelector(".car");
    const scrollY = window.scrollY;

    // Вращение инструментов
    tools.forEach((tool, index) => {
        const rotation = scrollY;
        tool.style.transform = `rotate(${rotation}deg)`;
    });

    // Вращение машины
    const carRotation = scrollY * -0.4;
    car.style.transform = `rotate(${carRotation}deg)`;
});