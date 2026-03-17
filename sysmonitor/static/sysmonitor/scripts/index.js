const cpu = document.getElementById('cpu');
const ram = document.getElementById('ram');
const drive = document.getElementById('drive');
const os = document.getElementById('os');

cpu.addEventListener('click', () => {
    window.location.href = "cpu_view/";
});

ram.addEventListener('click', () => {
    window.location.href = "ram_view/";
});

drive.addEventListener('click', () => {
    window.location.href = "drives_view/";
});

os.addEventListener('click', () => {
    window.location.href = "sys_view/";
});

setInterval(function () {
    fetch("updated_values/")
        .then(response => {
            if (!response.ok) {
                throw new Error("Network error");
            }
            else {
                return response.json();
            }
        })
        .then(data => {
            updateHTML(data);
        })
        .catch(error => {
            console.Error("Error calling Django function: ", error);
        });
}, 1000);

function updateHTML(data) {
    cpu.innerHTML = `<img src="https://www.svgrepo.com/show/529533/cpu.svg" alt="CPU" class="icon">
                <h2>CPU</h2>
                <p>Usage: ` + data.cpuUsage + `%</p>
                <p>Physical Cores: ` + data.physCores + `</p>
                <p>Logical Cores: ` + data.logicalCores + `</p>`;

    ram.innerHTML = `<img src="https://www.svgrepo.com/show/510479/ram.svg" alt="RAM" class="icon">
                <h2>RAM</h2>
                <p>Total Memory: ` + data.memory + `GB</p>
                <p>Free Memory: ` + data.freeMem + `GB</p>
                <p>Usage: ` + data.memUsage + `%</p>`;

    drive.innerHTML = `<img src="https://www.svgrepo.com/show/509902/drive.svg" alt="Drive" class="icon">
                <h2>Drive</h2>
                <p>Total Storage: ` + data.totalStorage + `GB</p>
                <p>Free Storage: ` + data.freeStorage + `GB</p>
                <p>Usage: ` + data.driveUsage + `%</p>`;
}