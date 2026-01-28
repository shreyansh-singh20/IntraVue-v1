document.getElementById("evaluateForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const btn = document.getElementById("evaluateBtn");
    const spinner = document.getElementById("btn-spinner");
    const output = document.getElementById("output");
    const firstCard = document.querySelector(".output .card");
    if (firstCard) {
        firstCard.classList.remove("highlight-result");
        void firstCard.offsetWidth;
        firstCard.classList.add("highlight-result");
    }


    btn.disabled = true;
    spinner.classList.remove("hidden");

    const data = {
        job_role: document.getElementById("jobRole").value.trim(),
        candidate_experience_level: document.getElementById("experience").value,
        job_description: document.getElementById("jobDesc").value.trim(),
        interview_question: document.getElementById("question").value.trim(),
        candidate_answer: document.getElementById("answer").value.trim()
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/evaluate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Backend error");
        }

        const result = await response.json();
        const text = result.evaluation || "";

        function extract(section) {
            const regex = new RegExp(
                `${section}\\s*:?([\\s\\S]*?)(?=\\n\\n[A-Z]|$)`,
                "i"
            );
            const match = text.match(regex);
            return match && match[1] ? match[1].trim() : "Not available";
        }

        document.getElementById("expected").innerText = extract("Expected Knowledge");
        document.getElementById("demonstrated").innerText = extract("Demonstrated Understanding");
        document.getElementById("gaps").innerText = extract("Identified Gaps");
        document.getElementById("risk").innerText = extract("Interview Risk Assessment");
        document.getElementById("improvements").innerText = extract("Improvement Suggestions");
        document.getElementById("summary").innerText = extract("Evaluation Summary");

        updateConfidenceScore(text);

        output.classList.add("hidden");
        output.classList.remove("fade-in");

        setTimeout(() => {
        output.classList.remove("hidden");
        output.classList.add("fade-in");

        output.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
        }, 300);


    } catch (error) {
        console.error(error);
    } finally {
        btn.disabled = false;
        spinner.classList.add("hidden");
    }
});

function updateConfidenceScore(text) {
    const valueEl = document.getElementById("confidence-value");
    const barEl = document.getElementById("confidence-fill");

    if (!valueEl || !barEl) return;

    barEl.style.width = "0%";
    valueEl.innerText = "0 / 100";

    const match = text.match(/Confidence Score:\s*(\d{1,3})/i);
    let score = match ? parseInt(match[1], 10) : 0;

    if (isNaN(score)) score = 0;
    score = Math.max(0, Math.min(score, 100));

    setTimeout(() => {
        barEl.style.width = `${score}%`;
    }, 60);

    valueEl.innerText = `${score} / 100`;

    if (score < 40) {
        barEl.style.backgroundColor = "#ef4444";
    } else if (score < 70) {
        barEl.style.backgroundColor = "#f59e0b";
    } else {
        barEl.style.backgroundColor = "#22c55e";
    }
}
