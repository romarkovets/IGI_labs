// Базовый класс Subscriber
function Subscriber(name, newspapers, magazines) {
    this.name = name;
    this.newspapers = newspapers;
    this.magazines = magazines;
}

Subscriber.prototype = {
    // Геттеры
    getName: function() {
        return this.name;
    },
    getNewspapers: function() {
        return this.newspapers;
    },
    getMagazines: function() {
        return this.magazines;
    },

    // Сеттеры
    setName: function(name) {
        this.name = name;
    },
    setNewspapers: function(newspapers) {
        this.newspapers = newspapers;
    },
    setMagazines: function(magazines) {
        this.magazines = magazines;
    },

    // Метод для добавления подписчика
    addSubscriber: function(name, newspapers, magazines) {
        this.name = name;
        this.newspapers = newspapers;
        this.magazines = magazines;
    }
};

// Класс-наследник ExtendedSubscriber
function ExtendedSubscriber(name, newspapers, magazines, address) {
    // Вызов конструктора базового класса
    Subscriber.call(this, name, newspapers, magazines);
    this.address = address;
}

// Прототипное наследование
ExtendedSubscriber.prototype = Object.create(Subscriber.prototype);
ExtendedSubscriber.prototype.constructor = ExtendedSubscriber;

// Геттеры и сеттеры для адреса
ExtendedSubscriber.prototype.getAddress = function() {
    return this.address;
};

ExtendedSubscriber.prototype.setAddress = function(address) {
    this.address = address;
};

// Метод для добавления подписчика с адресом
ExtendedSubscriber.prototype.addSubscriber = function(name, newspapers, magazines, address) {
    Subscriber.prototype.addSubscriber.call(this, name, newspapers, magazines);
    this.address = address;
};

// Метод для вывода всех подписчиков
ExtendedSubscriber.prototype.displayAllSubscribers = function(subscribersArray) {
    let result = '';
    subscribersArray.forEach(subscriber => {
        result += `<p>Имя: ${subscriber.getName()}, Газет: ${subscriber.getNewspapers()}, Журналов: ${subscriber.getMagazines()}, Адрес: ${subscriber.getAddress()}</p>`;
    });
    return result;
};

// Метод для фильтрации подписчиков (газеты >= 3 и журналы >= 2)
ExtendedSubscriber.prototype.displayFilteredSubscribers = function(subscribersArray) {
    let result = '';
    subscribersArray.forEach(subscriber => {
        if (subscriber.getNewspapers() >= 3 && subscriber.getMagazines() >= 2) {
            result += `<p>Имя: ${subscriber.getName()}, Газет: ${subscriber.getNewspapers()}, Журналов: ${subscriber.getMagazines()}, Адрес: ${subscriber.getAddress()}</p>`;
        }
    });
    return result || "<p>Нет подписчиков, соответствующих критериям.</p>";
};

// Массив для хранения подписчиков
let subscribers = [];

// Функция для добавления подписчика через форму
function addSubscriber() {
    const name = document.getElementById("name").value;
    const address = document.getElementById("address").value;
    const newspapers = parseInt(document.getElementById("newspapers").value);
    const magazines = parseInt(document.getElementById("magazines").value);

    // Проверка на неотрицательные числа
    if (newspapers < 0 || magazines < 0) {
        alert("Число газет и журналов не может быть отрицательным!");
        return;
    }

    // Создание подписчика (можно использовать как обычного подписчика, так и расширенный)
    const newSubscriber = new ExtendedSubscriber(name, newspapers, magazines, address);

    // Добавление подписчика в массив
    subscribers.push(newSubscriber);

    // Очистка формы
    document.getElementById("addSubscriberForm").reset();

    // Вывод всех подписчиков на страницу
    displayAllSubscribers();
}

// Функция для отображения всех подписчиков
function displayAllSubscribers() {
    const resultDiv = document.getElementById("result");
    const subscriberInstance = new ExtendedSubscriber();

    resultDiv.innerHTML = subscriberInstance.displayAllSubscribers(subscribers);
}

// Функция для фильтрации подписчиков (газеты >= 3 и журналы >= 2)
function displayFilteredSubscribers() {
    const resultDiv = document.getElementById("result");
    const subscriberInstance = new ExtendedSubscriber();

    resultDiv.innerHTML = subscriberInstance.displayFilteredSubscribers(subscribers);
}

