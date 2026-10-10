const task = document.getElementById("task");
const inputText = document.getElementById("inputText");
const submitBtn = document.getElementById("submitBtn");
const statusEl = document.getElementById("status");
const resultCard = document.getElementById("resultCard");
const resultEl = document.getElementById("result");

const placeholders = {
  qa: "Example: What is the largest ocean?",
  explain: "Example: Explain the Pythagorean theorem.",
  quiz: "Paste a topic or educational passage here.",
  summarize: "Paste a long educational passage here.",
  learn: "Example: I want to learn SQL from beginner to advanced."
};

task.addEventListener("change", () => {
  inputText.placeholder = placeholders[task.value];
});

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderResult(data) {
  if (data && data.questions) {
    resultEl.innerHTML = data.questions.map((q, i) => `
      <div class="quiz-question">
        <h3>${i + 1}. ${escapeHtml(q.question)}</h3>
        ${q.options.map(option => `<div class="option">${escapeHtml(option)}</div>`).join("")}
        <div class="answer">Correct answer: ${escapeHtml(q.answer)}</div>
      </div>
    `).join("");
    return;
  }

  resultEl.innerHTML = `<div class="result">${escapeHtml(data.result ?? "")}</div>`;
}

async function submit() {
  const text = inputText.value.trim();
  if (!text) {
    statusEl.textContent = "Please enter a question, topic, or passage.";
    return;
  }

  const endpoint = {
    qa: "/qa",
    explain: "/explain",
    quiz: "/quiz",
    summarize: "/summarize",
    learn: "/learn/recommendations"
  }[task.value];

  submitBtn.disabled = true;
  statusEl.textContent = "EduGenie is thinking...";
  resultCard.classList.add("hidden");

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });

    const contentType = response.headers.get("content-type") || "";
    const data = contentType.includes("application/json")
      ? await response.json()
      : {detail: await response.text()};

    if (!response.ok) {
      throw new Error(data.detail || "Request failed.");
    }

    renderResult(data);
    resultCard.classList.remove("hidden");
    statusEl.textContent = "Completed.";
  } catch (error) {
    statusEl.textContent = error.message;
  } finally {
    submitBtn.disabled = false;
  }
}

submitBtn.addEventListener("click", submit);
