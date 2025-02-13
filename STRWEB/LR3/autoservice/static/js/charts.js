
function factorial(n) {
    if (n === 0 || n === 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Функция для вычисления cos(x) с использованием ряда Тейлора
function cosTaylor(x, precision = 10) {
    let result = 0;
    for (let n = 0; n < precision; n++) {
        const term = Math.pow(-1, n) * Math.pow(x, 2 * n) / factorial(2 * n);
        result += term;
    }
    return result;
}

// Создаем данные для графика
const labels = [];
const taylorData = [];
const actualData = [];

const start = -2 * Math.PI;
const end = 2 * Math.PI;
const step = 0.1;

for (let x = start; x <= end; x += step) {
    labels.push(x.toFixed(2));
    taylorData.push(cosTaylor(x, 7)); // Ряд Тейлора с точностью 7
    actualData.push(Math.cos(x)); // Фактическое значение cos(x)
}

// Создаем график
const ctx = document.getElementById('cosChart').getContext('2d');
const cosChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Ряд Тейлора (cos(x))',
                data: taylorData,
                borderColor: 'blue',
                borderWidth: 2,
                fill: false,
            },
            {
                label: 'Фактическое значение (cos(x))',
                data: actualData,
                borderColor: 'red',
                borderWidth: 2,
                fill: false,
            },
        ],
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'x',
                },
            },
            y: {
                title: {
                    display: true,
                    text: 'cos(x)',
                },
            },
        },
    },
});


document.getElementById('saveChart').addEventListener('click', () => {
    // Получаем base64-код графика
    const image = cosChart.toBase64Image('chart');

    // Создаем временную ссылку для скачивания
    const link = document.createElement('a');
    link.href = image;
    link.download = 'super_chart_oh_my_god_staribog.png'; // Имя файла
    link.click(); // Программное нажатие на ссылку
});