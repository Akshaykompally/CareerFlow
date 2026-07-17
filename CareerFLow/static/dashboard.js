const chartData = document.getElementById("chart-data");

const labels = JSON.parse(chartData.dataset.labels);
const data = JSON.parse(chartData.dataset.data);

const roundLabels = JSON.parse(chartData.dataset.roundLabels);
const roundData = JSON.parse(chartData.dataset.roundData);

// Pie Chart
const ctx = document.getElementById("statusChart");

const colors = labels.map(label => {
    switch (label.toLowerCase()) {
        case "selected":
            return "#22c55e";   // Green
        case "rejected":
            return "#ef4444";   // Red
        case "pending":
            return "#facc15";   // Yellow
        default:
            return "#9ca3af";   // Gray
    }
});


if (ctx) {
    new Chart(ctx, {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor:colors
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        usePointStyle: true,
                        pointStyle: "circle"
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Bar Chart
const ctx2 = document.getElementById("roundChart");

if (ctx2) {
    new Chart(ctx2, {
        type: "bar",
        data: {
            labels: roundLabels,
            datasets: [{
                label: "Rounds Attended",
                data: roundData,
                backgroundColor: "#3b82f6",
                barThickness: 50,
                borderRadius: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    categoryPercentage: 0.6,
                    barPercentage: 0.6
                }
            }
        }
    });
}