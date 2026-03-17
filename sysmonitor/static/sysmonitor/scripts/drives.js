const usedStorage = document.getElementById('usedStorage');
const freeStorage = document.getElementById('freeStorage');
const usage = document.getElementById('currentUsage');

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
    usedStorage.innerText = 'Almacenamiento Usado: ' + data.usedStorage + 'GB';
    freeStorage.innerText = 'Almacenamiento Disponible: ' + data.freeStorage + 'GB';
    usage.innerText = 'Uso de la Unidad: ' + data.driveUsage + '%';
}