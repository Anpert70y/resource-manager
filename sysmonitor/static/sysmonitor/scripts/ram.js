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
    usedMem.innerText = 'Used Memory: ' + data.usedMem + 'GB';
    freeMem.innerText = 'Free Memory: ' + data.freeMem + 'GB';
    usage.innerText = 'Usage: ' + data.memUsage + '%';
}