document.addEventListener("DOMContentLoaded", () => {
    const madon = new URLSearchParams(location.search).get("madon");
    document.querySelector(".title").textContent = `Đơn thuốc #${madon}`
    
    
    fetch('/getMachineID')
    .then(req => {return req.json()})
    .then(res => {
        document.querySelector("#ID").textContent = `PharmaBox #${res.id}`
    })
    
    
    fetch(`/getCheckoutInfo?madon=${madon}`)
    .then(req => {return req.json()})
    .then(res => {
        const table = document.querySelector(".donthuoc > table");
        for (let i in res) {
            const stt = Number(i)+1;
            fetch(`/getMedicineInfo?id=${res[i].id}`)
            .then(req => {return req.json()})
            .then(re => {
                const entry = `<tr>
                <td>${stt}</td>
                <td>${re.name}</td>
                <td>${re.cost}</td>
                <td>${Number(res[i].amount)}</td>
                <td>${Number(res[i].amount)*Number(re.cost)}</td>
                </tr>`
                table.innerHTML += entry;
            })
        }
    })
})

const checkout = () => {
    location.replace(`/banking?madon=${new URLSearchParams(location.search).get("madon")}`);
}