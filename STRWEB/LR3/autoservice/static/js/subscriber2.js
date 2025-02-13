class Subscriber2 {
    constructor(name, newspapers, magazines) {
        this.name = name;
        this.newspapers = newspapers;
        this.magazines = magazines;
    }

    // Геттеры
    getName2() {
        return this.name;
    }

    getNewspapers2() {
        return this.newspapers;
    }

    getMagazines2() {
        return this.magazines;
    }

    // Сеттеры
    setName2(name) {
        this.name = name;
    }

    setNewspapers2(newspapers) {
        this.newspapers = newspapers;
    }

    setMagazines2(magazines) {
        this.magazines = magazines;
    }

    // Метод для добавления подписчика
    addSubscriber2(name, newspapers, magazines) {
        this.name = name;
        this.newspapers = newspapers;
        this.magazines = magazines;
    }
}


class ExtendedSubscriber2 extends Subscriber2 {
    constructor(name, newspapers, magazines, address) {
        super(name, newspapers, magazines); // Вызов конструктора родителя
        this.address = address;
    }


    getAddress2() {
        return this.address;
    }

    setAddress2(address) {
        this.address = address;
    }


    addSubscriber2(name, newspapers, magazines, address) {
        super.addSubscriber2(name, newspapers, magazines);
        this.address = address;
    }


    displayAllSubscribers2(subscribersArray) {
        let result = '';
        subscribersArray.forEach(subscriber => {
            result += `<p>Имя: ${subscriber.getName2()}, Газет: ${subscriber.getNewspapers2()}, Журналов: ${subscriber.getMagazines2()}, Адрес: ${subscriber.getAddress2()}</p>`;
        });
        return result;
    }


    displayFilteredSubscribers2(subscribersArray) {
        let result = '';
        subscribersArray.forEach(subscriber => {
            if (subscriber.getNewspapers2() >= 3 && subscriber.getMagazines2() >= 2) {
                result += `<p>Имя: ${subscriber.getName2()}, Газет: ${subscriber.getNewspapers2()}, Журналов: ${subscriber.getMagazines2()}, Адрес: ${subscriber.getAddress2()}</p>`;
            }
        });
        return result || "<p>Нет подписчиков, соответствующих критериям.</p>";
    }
}

// Массив для хранения подписчиков
let subscribersList = [];

// Функция для добавления подписчика
function addSubscriber2() {
    const name = document.getElementById("name2").value;
    const address = document.getElementById("address2").value;
    const newspapers = parseInt(document.getElementById("newspapers2").value);
    const magazines = parseInt(document.getElementById("magazines2").value);

    // Проверка на неотрицательные числа
    if (newspapers < 0 || magazines < 0) {
        alert("Число газет и журналов не может быть отрицательным!");
        return;
    }

    // Создание подписчика
    const newSubscriber = new ExtendedSubscriber2(name, newspapers, magazines, address);

    // Добавление подписчика в массив
    subscribersList.push(newSubscriber);

    // Очистка формы
    document.getElementById("addSubscriberForm2").reset();

    // Вывод всех подписчиков на страницу
    displayAllSubscribers2();
}

// Функция для отображения всех подписчиков
function displayAllSubscribers2() {
    const resultDiv = document.getElementById("result2");
    const subscriberInstance = new ExtendedSubscriber2();

    resultDiv.innerHTML = subscriberInstance.displayAllSubscribers2(subscribersList);
}

// Функция для фильтрации подписчиков (газеты >= 3 и журналы >= 2)
function displayFilteredSubscribers2() {
    const resultDiv = document.getElementById("result2");
    const subscriberInstance = new ExtendedSubscriber2();

    resultDiv.innerHTML = subscriberInstance.displayFilteredSubscribers2(subscribersList);
}

