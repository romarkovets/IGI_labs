const cards = document.querySelectorAll('.service-item');

cards.forEach(card => {

  card.addEventListener('mousemove', (e) => {
    // Get the card's size
    const cardRect = card.getBoundingClientRect();

    // Calculate the position of the mouse relative to the card's top-left corner
    const x = e.clientX - cardRect.left;
    const y = e.clientY - cardRect.top;

    // center of the card
    const centerX = cardRect.width / 2;
    const centerY = cardRect.height / 2;

    // Calculate the rotation angles based on mouse position
    const rotateX = ((y - centerY) / centerY) * 30;
    const rotateY = ((centerX - x) / centerX) * 30;

    // Apply the calculated rotation to the card
    card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
  });

  // when the mouse leaves the card area
  card.addEventListener('mouseleave', () => {
    // Reset the card's rotation when the mouse leaves
    card.style.transform = 'rotateX(0) rotateY(0)';
  });
});


document.addEventListener("DOMContentLoaded", () => {
    const servicesGrid = document.querySelector(".services-grid");
    const paginationContainer = document.querySelector(".pagination");
    const itemsPerPage = 3;
    let currentPage = 1;

    const items = Array.from(servicesGrid.querySelectorAll(".service-item"));

    function displayItems(page) {
        const start = (page - 1) * itemsPerPage;
        const end = start + itemsPerPage;

        items.forEach((item, index) => {
            if (index >= start && index < end) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    }

    function createPagination() {
        const totalPages = Math.ceil(items.length / itemsPerPage);
        paginationContainer.innerHTML = "";

        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("button");
            button.textContent = i;
            button.addEventListener("click", () => {
                currentPage = i;
                displayItems(currentPage);
                updatePaginationButtons();
            });
            paginationContainer.appendChild(button);
        }

        updatePaginationButtons();
    }

    function updatePaginationButtons() {
        const buttons = paginationContainer.querySelectorAll("button");
        buttons.forEach((button, index) => {
            if (index + 1 === currentPage) {
                button.classList.add("active");
            } else {
                button.classList.remove("active");
            }
        });
    }

    displayItems(currentPage);
    createPagination();
});