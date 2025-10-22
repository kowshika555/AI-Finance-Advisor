const backendUrl = "http://127.0.0.1:8000";

document.getElementById("addBtn").addEventListener("click", async () => {
  const amount = parseFloat(document.getElementById("amount").value);
  const category = document.getElementById("category").value;
  const type = document.getElementById("type").value;

  if (!amount || !category) {
    alert("Please fill all fields!");
    return;
  }

  const res = await fetch(`${backendUrl}/add_transaction`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, category, type }),
  });
  const data = await res.json();
  alert(data.message);
  loadTransactions();
});

async function loadTransactions() {
  const res = await fetch(`${backendUrl}/get_transactions`);
  const data = await res.json();

  const list = document.getElementById("txList");
  list.innerHTML = "";
  data.forEach((tx) => {
    const li = document.createElement("li");
    li.textContent = `${tx.type.toUpperCase()}: ₹${tx.amount} - ${tx.category}`;
    list.appendChild(li);
  });
}

document.getElementById("getSuggestionBtn").addEventListener("click", async () => {
  const res = await fetch(`${backendUrl}/get_suggestion`);
  const data = await res.json();
  document.getElementById("suggestion").textContent = data.suggestion;
});

loadTransactions();

document.getElementById("financeForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const income = parseFloat(document.getElementById("income").value);
  const expenses = parseFloat(document.getElementById("expenses").value);
  const goal = document.getElementById("goal").value;
  const suggestionBox = document.getElementById("resultBox");
  const suggestionText = document.getElementById("suggestionText");

  suggestionBox.classList.remove("hidden");
  suggestionText.textContent = "Analyzing your finances... Please wait ⏳";

  try {
    const response = await fetch("http://127.0.0.1:8000/ai-advice", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ income, expenses, goal })
    });

    const data = await response.json();
    suggestionText.textContent = data.suggestion;
  } catch (error) {
    suggestionText.textContent = "Error connecting to backend ❌";
  }
});
