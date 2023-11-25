// script.js

// Добавляем варианты времени в селект
var timeSelect = document.getElementById("time");
for (var i = 9; i <= 17; i++) {
    for (var j = 0; j < 2; j++) {
        var timeString = (i < 10 ? "0" : "") + i + ":" + (j === 0 ? "00" : "30");
        var option = new Option(timeString, timeString);
        timeSelect.add(option);
    }
}

// Функция для обновления филиалов в зависимости от выбранного города
function updateBranches() {
    var citySelect = document.getElementById("city");
    var branchSelect = document.getElementById("branch");

    // Удаляем все текущие варианты
    while (branchSelect.options.length > 0) {
        branchSelect.remove(0);
    }

    // Добавляем новые варианты в зависимости от выбранного города
    switch (citySelect.value) {
        case "bishkek":
            branchSelect.add(new Option("ул. Киевская, 77", "kiev"));
            branchSelect.add(new Option("ул. Юнусалиева, 142", "yunus"));
            break;
        case "osh":
            branchSelect.add(new Option("ул. Раззакова, 50", "razzakova"));
            branchSelect.add(new Option("ул. Масалиева, 100", "masalieva"));
            break;
        case "talas":
            branchSelect.add(new Option("ул. Бердике Баатыра 198", "berdike"));
            break;
        case "naryn":
            branchSelect.add(new Option("ул. Ленина, 43а", "lenina43a"));
            branchSelect.add(new Option("ул. Ленина, 244", "lenina244"));
            break;
        case "batken":
            branchSelect.add(new Option("ул. Садыкова, 5", "sadykova"));
            break;
        case "cholpon_ata":
            branchSelect.add(new Option("ул. Советская, 22", "sovietskaya"));
            break;
        case "jalalabad":
            branchSelect.add(new Option("ул. Ленина, 43", "lenina43"));
            branchSelect.add(new Option("ул. Строителей, 48", "stroiteley"));
            break;
    }
}

// Обработчик изменения города
document.getElementById("city").addEventListener("change", updateBranches);

// Инициализация вариантов филиалов при загрузке страницы
updateBranches();

var confirmationCode,city, service,date,time,branch
// Добавляем функцию открытия модального окна
function openModal() {
    var modal = document.getElementById("myModal");
    var modalContent = document.getElementById("modalContent");
     confirmationCode = Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000;

    // Получаем данные из формы
     city = document.getElementById("city").options[document.getElementById("city").selectedIndex].innerText;
     service = document.getElementById("service").options[document.getElementById("service").selectedIndex].innerText;
     date = document.getElementById("date").value;
     time = document.getElementById("time").value;
     branch = document.getElementById("branch").options[document.getElementById("branch").selectedIndex].innerText;
    

    // Формируем текст для отображения в модальном окне
    var modalText = "Город: " + city + "<br>" +
                    "Услуга: " + service + "<br>" +
                    "Дата: " + date + "<br>" +
                    "Время: " + time + "<br>" +
                    "Филиал: " + branch + "<br>" +
                    "Код подтверждения: " + confirmationCode;

    // Устанавливаем текст в модальном окне
    modalContent.innerHTML = modalText;

    // Отображаем модальное окно
    modal.style.display = "block";
}

// Функция закрытия модального окна
function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Функция подтверждения данных
function confirmQueue() {
    // Здесь можно добавить логику для подтверждения данных
    alert("Очередь подтверждена!");
    closeModal();
}

// Функция редактирования данных
function editQueue() {
    // Здесь можно добавить логику для редактирования данных
    alert("Редактирование данных...");
    closeModal();
}

// Функция отмены очереди
function cancelQueue() {
    // Здесь можно добавить логику для отмены очереди
    alert("Очередь отменена.");
    closeModal();
}


async function fetchData() {
    
    let customer_id = "user1";

    const url = "http:www.localhost/127.0.0.1:5000/";
    const data = {
        customer_id: customer_id,
        in_queue_date: date,
        in_queue_time: time,
        service_type: service,
        queue_type: "ONLINE",
        branch: branch,
        city: city,
        pin: confirmationCode
    };

    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
            },
        });

        const json = await response.json();
        console.log("Успех:", JSON.stringify(json));
    } catch (error) {
        console.error("Ошибка:", error);
    }
    
}

// Call the fetchData function
fetchData();