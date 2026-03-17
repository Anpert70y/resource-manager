const usedMem = document.getElementById('usedMem');
const freeMem = document.getElementById('freeMem');
const usage = document.getElementById('memUsage');

setInterval(function () {
    fetch("../updated_values/")
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
    usedMem.innerText = 'Memoria Usada: ' + data.usedMem + 'GB';
    freeMem.innerText = 'Memoria Disponible: ' + data.freeMem + 'GB';
    usage.innerText = 'Uso: ' + data.memUsage + '%';
}