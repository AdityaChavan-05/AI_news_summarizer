// =========================
// THEME BUTTON
// =========================

const themeButton = document.getElementById("themeButton");

themeButton.addEventListener("click", () => {

    document.body.classList.toggle("light-mode");

    if (document.body.classList.contains("light-mode")) {
        themeButton.textContent = "☀️";
    } else {
        themeButton.textContent = "🌙";
    }

});


// =========================
// CATEGORY BUTTONS
// =========================

const categoryButtons =
    document.querySelectorAll(".category");

categoryButtons.forEach(button => {

    button.addEventListener("click", () => {

        // Remove active from all buttons
        categoryButtons.forEach(btn => {
            btn.classList.remove("active");
        });

        // Add active to clicked button
        button.classList.add("active");

        const category = button.textContent.trim();

        console.log(
            "Loading category:",
            category
        );

        loadNews(category);

    });

});


// =========================
// SEARCH BUTTON
// =========================

const searchButton =
    document.getElementById("searchButton");

const searchInput =
    document.getElementById("searchInput");

searchButton.addEventListener("click", () => {

    const query = searchInput.value.trim();

    if (query === "") {

        alert("Please enter something to search.");

        return;
    }

    console.log("Searching for:", query);

    alert(
        `Searching engineering news for: ${query}`
    );

});


// =========================
// REFRESH BUTTON
// =========================

const refreshButton =
    document.getElementById("refreshButton");

refreshButton.addEventListener("click", () => {

    refreshButton.textContent = "↻ Loading...";

    setTimeout(() => {

        refreshButton.textContent = "↻ Refresh";

        alert("News refreshed!");

    }, 1000);

});
// =========================
// LOAD REAL NEWS
// =========================

async function loadNews(category = "Artificial Intelligence") {

    const newsGrid =
        document.getElementById("newsGrid");

    // Show loading message
    newsGrid.innerHTML = `
        <p style="color: #9ba7c0;">
            Loading latest news... 📰
        </p>
    `;

    try {

        const response = await fetch(
    `/api/news?category=${encodeURIComponent(category)}`
);

        const articles = await response.json();

        newsGrid.innerHTML = "";

        articles.forEach(article => {

            const card = document.createElement("article");

            card.className = "news-card";

            card.innerHTML = `
                <div class="news-image">
                    🤖
                </div>

                <div class="news-content">

                    <div class="news-meta">
                        <span>Artificial Intelligence</span>
                        <span>Latest</span>
                    </div>

                    <h3>
                        ${article.title}
                    </h3>

                    <p class="description">
                        ${article.description}
                    </p>

                    <div class="ai-summary">

    <div class="ai-title">
        🤖 AI Summary
    </div>

    <div class="summary-text">
        ${article.summary}
    </div>

</div>

                    <div class="card-footer">

                        <span>
                            ${article.source}
                        </span>

                        <a
                            href="${article.link}"
                            target="_blank"
                        >
                            Read article →
                        </a>

                    </div>

                </div>
            `;

            newsGrid.appendChild(card);

        });

    } catch (error) {

        console.error(
            "Could not load news:",
            error
        );

        newsGrid.innerHTML = `
            <p style="color: #ff8a8a;">
                Could not load news.
                Make sure the Flask server is running.
            </p>
        `;
    }
}


// Load news when the page opens
loadNews();