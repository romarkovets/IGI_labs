let currentPage = 1;
        const rowsPerPage = 3;

        function paginateTable() {
            let rows = document.querySelectorAll("#tableBody tr:not(.hidden)");
            let totalRows = rows.length;
            let totalPages = Math.ceil(totalRows / rowsPerPage);

            document.getElementById("pagination").innerHTML = "";
            for (let i = 1; i <= totalPages; i++) {
                let btn = document.createElement("button");
                btn.innerText = i;
                btn.onclick = function() { changePage(i); };
                document.getElementById("pagination").appendChild(btn);
            }
            changePage(1);
        }

        function changePage(page) {
            currentPage = page;
            let rows = document.querySelectorAll("#tableBody tr:not(.hidden)");
            let start = (page - 1) * rowsPerPage;
            let end = start + rowsPerPage;

            document.querySelectorAll("#tableBody tr").forEach(row => row.style.display = "none");
            rows.forEach((row, index) => {
                if (index >= start && index < end) row.style.display = "";
            });
        }

        function sortTable(colIndex) {
            let table = document.getElementById("employeeTable");
            let rows = Array.from(document.querySelectorAll("#tableBody tr"));
            let ascending = table.getAttribute("data-sort-order") !== "asc";
            rows.sort((rowA, rowB) => {
                let a = rowA.cells[colIndex - 1].innerText.toLowerCase();
                let b = rowB.cells[colIndex - 1].innerText.toLowerCase();
                return ascending ? a.localeCompare(b) : b.localeCompare(a);
            });
            table.setAttribute("data-sort-order", ascending ? "asc" : "desc");
            let tbody = document.getElementById("tableBody");
            rows.forEach(row => tbody.appendChild(row));
            paginateTable();
        }

        function filterTable() {
            let search = document.getElementById("searchBox").value.toLowerCase();
            let rows = document.querySelectorAll("#tableBody tr");
            rows.forEach(row => {
                row.classList.toggle("hidden", !row.innerText.toLowerCase().includes(search));
            });
            paginateTable();
        }

        function selectAll(source) {
            document.querySelectorAll(".select-employee").forEach(cb => cb.checked = source.checked);
        }

        function rewardEmployees() {
            let selected = Array.from(document.querySelectorAll(".select-employee:checked"))
                .map(cb => cb.closest("tr").cells[1].innerText);  // Изменено на индекс 1 для отображения ФИО
            document.getElementById("rewardMessage").textContent = "Премированы: " + selected.join(", ");
        }

        // Функция для отображения деталей сотрудника по клику на строку
        function showDetails(row) {
            document.getElementById("employeeDetails").style.display = "none";
            document.getElementById("preloader").style.display = "block";

            setTimeout(function() {
                document.getElementById("preloader").style.display = "none";
                let cells = row.cells;
                document.getElementById("detailPhoto").src = cells[0].querySelector('img').src;
                document.getElementById("detailFullName").innerText = cells[1].innerText;
                document.getElementById("detailJobs").innerText = cells[2].innerText;
                document.getElementById("detailEmail").innerText = cells[3].innerText;
                document.getElementById("detailPhone").innerText = cells[4].innerText;
                document.getElementById("detailSchedule").innerText = cells[5].innerText;  // График работы передается сюда

                // Показать блок с деталями
                document.getElementById("employeeDetails").style.display = "block";
            }, 3000);



        }

        // Скрыть блок с деталями, если кликнуть в любое место вне таблицы или после нового клика
        document.addEventListener("click", function(event) {
            if (!event.target.closest("#employeeTable") && !event.target.closest("#employeeDetails")) {
                document.getElementById("employeeDetails").style.display = "none";
            }
        });

        document.addEventListener("DOMContentLoaded", paginateTable);