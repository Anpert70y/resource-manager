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
                <p>Uso: ` + data.cpuUsage + `%</p>
                <p>Nucleos Físicos: ` + data.physCores + `</p>
                <p>Nucleos Lógicos: ` + data.logicalCores + `</p>`;

    ram.innerHTML = `<img src="https://www.svgrepo.com/show/510479/ram.svg" alt="RAM" class="icon">
                <h2>RAM</h2>
                <p>Memoria Total: ` + data.memory + `GB</p>
                <p>Memoria Disponible: ` + data.freeMem + `GB</p>
                <p>Uso: ` + data.memUsage + `%</p>`;

    drive.innerHTML = `<img src="https://www.svgrepo.com/show/509902/drive.svg" alt="Drive" class="icon">
                <h2>Disco</h2>
                <p>Almacenamiento Total: ` + data.totalStorage + `GB</p>
                <p>Almacenamiento Disponible: ` + data.freeStorage + `GB</p>
                <p>Uso: ` + data.driveUsage + `%</p>`;
}