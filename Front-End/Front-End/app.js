document.addEventListener("DOMContentLoaded", function () {
  fetch("./data_with_id.json")
    .then(response => response.json())
    .then(data => {
      console.log(data);
      const appElement = document.getElementById("app");

      data.forEach(item => {
        const card = document.createElement("div");
        card.classList.add("card");
        card.style.width = '350px';

        card.innerHTML = `
          <div class="card-body d-flex flex-column justify-content-between">
            <div class="d-flex gap-3 align-items-center mb-3">
              <img src="${item.logo}" alt="Foto Logo" style="width:50px; height:50px">
              <h5 class="card-title">${item.university}</h5>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><p id="webkitline" class="m-0">${item.periode_penerimaan}</p></li>
              <li class="list-group-item"><p id="webkitline" class="m-0">${item.name}</p></li>
              <li class="list-group-item"><p id="webkitline" class="m-0">${item.category}</p></li>
              <li class="list-group-item d-flex justify-content-md-end"><button class="btn btn-outline-dark" disabled>${item.status}</button></li>
            </ul>
          </div>
        `;
 
        // const logo = document.createElement("img");
        // logo.src = item.logo;
        // card.appendChild(logo);

        // const name = document.createElement("h2");
        // name.textContent = item.name;
        // card.appendChild(name);

        // const status = document.createElement("p");
        // status.textContent = "Status: " + item.status;
        // status.classList.add(item.status === "tutup" ? "status-closed" : "status-open");
        // card.appendChild(status);

        // const category = document.createElement("p");
        // category.textContent = "Category: " + item.category;
        // card.appendChild(category);

        // const university = document.createElement("p");
        // university.textContent = "University: " + item.university;
        // card.appendChild(university);

        // const periode = document.createElement("p");
        // periode.textContent = item.periode_penerimaan;
        // card.appendChild(periode);

        appElement.appendChild(card);
      });
    })
    .catch(error => console.error("Error fetching data:", error));
});
