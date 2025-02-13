// Функция для отображения/скрытия формы
function toggleForm() {
    const form = document.getElementById("addForm");
    form.classList.toggle("hidden");
}

// Функция для проверки валидности URL
function validateUrl() {
    const urlInput = document.getElementById("photoUrl");
    const url = urlInput.value;
    const urlPattern = /^(http:\/\/|https:\/\/).+\.(php|html)$/;
    const isValid = urlPattern.test(url);

    if (!isValid) {
        urlInput.classList.add("error");
        document.getElementById("validationMessage").textContent = "URL должен начинаться с http:// или https:// и заканчиваться на .php или .html.";
    } else {
        urlInput.classList.remove("error");
        document.getElementById("validationMessage").textContent = "";
    }

    checkFormValidity();
}

// Функция для проверки валидности номера телефона
function validatePhone() {
    const phoneInput = document.getElementById("phone");
    const phone = phoneInput.value;
    const phonePattern = /^(\+375|8)\s?\(?\d{2}\)?\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/;
    const isValid = phonePattern.test(phone);

    if (!isValid) {
        phoneInput.classList.add("error");
        document.getElementById("validationMessage").textContent = "Номер телефона должен начинаться с +375 или 8 и соответствовать формату.";
    } else {
        phoneInput.classList.remove("error");
        document.getElementById("validationMessage").textContent = "";
    }

    checkFormValidity();
}

// Функция для проверки заполненности всех полей
function checkFormValidity() {
    const fullName = document.getElementById("fullName").value;
    const photoUrl = document.getElementById("photoUrl").value;
    const jobs = document.getElementById("jobs").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;

    const urlValid = !document.getElementById("photoUrl").classList.contains("error");
    const phoneValid = !document.getElementById("phone").classList.contains("error");

    if (fullName && photoUrl && jobs && phone && email && urlValid && phoneValid) {
        document.getElementById("addButton").disabled = false;
    } else {
        document.getElementById("addButton").disabled = true;
    }
}

// Функция для добавления строки в таблицу
function addRow() {
    const fullName = document.getElementById("fullName").value;
    const photoUrl = document.getElementById("photoUrl").value;
    const jobs = document.getElementById("jobs").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;

    const tableBody = document.getElementById("tableBody");
    const newRow = document.createElement("tr");

    newRow.innerHTML = `
        <td><img src="${photoUrl}" alt="Employee image" width="50" height="50"></td>
        <td>${fullName}</td>
        <td>${jobs}</td>
        <td>${email}</td>
        <td>${phone}</td>
        <td hidden>График работы</td> <!-- Скрытое поле для расписания -->
        <td><input type="checkbox" class="select-employee"></td>
    `;

    tableBody.appendChild(newRow);

    // Очистка формы
    document.getElementById("fullName").value = "";
    document.getElementById("photoUrl").value = "";
    document.getElementById("jobs").value = "";
    document.getElementById("phone").value = "";
    document.getElementById("email").value = "";

    // Скрытие формы
    toggleForm();

    // Обновление пагинации
    paginateTable();
}

// Добавляем обработчики для проверки формы
document.getElementById("fullName").addEventListener("input", checkFormValidity);
document.getElementById("jobs").addEventListener("input", checkFormValidity);
document.getElementById("email").addEventListener("input", checkFormValidity);