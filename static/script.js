const $ = (id) => document.getElementById(id);

async function loadAnalysis() {
  $("analysisStatus").textContent = "Loading...";
  $("refreshBtn").disabled = true;

  try {
    const response = await fetch("/api/sample");
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Failed to load analysis.");
    }

    $("totalEvents").textContent = data.total_events;
    $("totalFindings").textContent = data.total_findings;
    $("criticalFindings").textContent = data.findings.filter(
      (finding) => finding.severity === "Critical"
    ).length;

    $("eventCount").textContent = `${data.timeline.length} EVENTS`;
    $("analysisStatus").textContent = "Complete";

    const timelineBody = $("timelineBody");
    timelineBody.replaceChildren();

    data.timeline.forEach((event) => {
      const row = document.createElement("tr");

      const values = [
        new Date(event.timestamp).toLocaleString(),
        event.id || "—",
        event.event_type || "unknown",
        event.source_ip || "Unknown",
        event.details || "No details recorded"
      ];

      values.forEach((value, index) => {
        const cell = document.createElement("td");
        cell.textContent = value;

        if (index === 2) {
          cell.className = "event-type";
        }

        row.appendChild(cell);
      });

      row.addEventListener("click", () => {
        document.querySelectorAll("#timelineBody tr").forEach((item) => {
          item.classList.remove("selected");
        });

        row.classList.add("selected");
        $("eventInspector").textContent = JSON.stringify(event, null, 2);
      });

      timelineBody.appendChild(row);
    });

    const findingsList = $("findingsList");
    findingsList.replaceChildren();

    if (data.findings.length === 0) {
      findingsList.textContent = "No suspicious patterns detected by the rules.";
    }

    data.findings.forEach((finding) => {
      const card = document.createElement("article");
      card.className = `finding ${finding.severity}`;

      const severity = document.createElement("span");
      severity.className = "severity";
      severity.textContent = finding.severity;

      const title = document.createElement("h3");
      title.textContent = finding.title;

      const description = document.createElement("p");
      description.textContent = finding.description;

      const source = document.createElement("p");
      source.textContent = `Source: ${finding.source_ip}`;

      const recommendation = document.createElement("p");
      recommendation.className = "recommendation";
      recommendation.textContent = `Recommended next step: ${finding.recommendation}`;

      card.append(severity, title, description, source, recommendation);
      findingsList.appendChild(card);
    });
  } catch (error) {
    console.error("Analysis loading failed:", error);

    $("analysisStatus").textContent = "Error";
    $("timelineBody").innerHTML =
      '<tr><td colspan="5" class="error">Could not load evidence. Check the Flask terminal.</td></tr>';

    $("findingsList").textContent = error.message;
  } finally {
    $("refreshBtn").disabled = false;
  }
}

$("refreshBtn").addEventListener("click", loadAnalysis);
loadAnalysis();
