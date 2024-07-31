async function apiGetAllCards() {
    const response = await fetch("/api/cards/");
    const payload = await response.json();
    if (!payload.errors) {
      return payload.data;
    } else {
      console.error(
        "API call to GET /api/cards/ failed:",
        JSON.stringify(payload.errors),
      );
      return [];
    }
  }

  async function apiCreateCard(title, content) {
    const payload_in = { data: { title, content: content ?? null } };
    const response = await fetch("/api/cards/", {
      method: "POST",
      body: JSON.stringify(payload_in),
    });
    const payload_out = await response.json();
    if (!payload_out.errors) {
      return payload_out.data;
    } else {
      console.error(
        "API call to POST /api/cards/ failed:",
        JSON.stringify(payload_out.errors),
      );
      return null;
    }
  }

  function buildCardComponent(card) {
    const p = document.createElement("p");
    p.classList.add("card-text");
    p.innerText = card.content;

    const h5 = document.createElement("h5");
    h5.classList.add("card-title");
    h5.innerText = card.title;

    const divCardBody = document.createElement("div");
    divCardBody.classList.add("card-body");
    [h5, p].forEach((child) => {
      divCardBody.appendChild(child);
    });

    const divComponent = document.createElement("div");
    ["card", "m-2"].forEach((cssClass) => {
      divComponent.classList.add(cssClass);
    });
    divComponent.style.width = "18rem";
    divComponent.appendChild(divCardBody);

    return divComponent;
  }

  async function createCard() {
    const inputTitle = document.getElementById("idTitleInput");
    const inputContent = document.getElementById("idContentInput");

    const title = inputTitle.value;
    if (!title) {
      alert("Title must be set!");
      return;
    }

    const content = inputContent.value ?? null;

    const newCard = await apiCreateCard(title, content);
    console.debug("created a new card:", JSON.stringify(newCard));

    const newCardComponent = buildCardComponent(newCard);
    const cardsContainer = document.getElementById("idCardsContainer");
    cardsContainer.appendChild(newCardComponent);

    inputTitle.value = "";
    inputContent.value = "";
  }

  async function populateCards() {
    const cardsContainer = document.getElementById("idCardsContainer");
    cardsContainer.innerHTML = "";

    const cards = await apiGetAllCards();
    cards.forEach((card) => {
      const cardComponent = buildCardComponent(card);
      cardsContainer.appendChild(cardComponent);
    });
  }

  function setUpCards() {
    const button = document.getElementById("idAddCardButton");
    button.addEventListener("click", createCard);

    populateCards();

    setInterval(populateCards, 10000);
  }
