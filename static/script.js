document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("taskForm");
  const responseMsg = document.getElementById("responseMsg");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      title: document.getElementById("title").value,
      description: document.getElementById("description").value,
      dueDate: document.getElementById("dueDate").value,
    };

    try {
      responseMsg.textContent = "Submitting...";
      responseMsg.style.color = "black";

      const res = await fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const result = await res.json();

      responseMsg.textContent = result.message;

      if (res.ok) {
        form.reset();
        responseMsg.style.color = "green";
      } else {
        responseMsg.style.color = "red";
      }
    } catch (err) {
      responseMsg.textContent = "Error: " + err.message;
      responseMsg.style.color = "red";
    }
  });
});
