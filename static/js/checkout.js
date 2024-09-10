let total = 0;
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
    .then(async (res) => {
        const table = document.querySelector(".donthuoc > table");
        for (let i in res) {
            const stt = Number(i)+1;
            await fetch(`/getMedicineInfo?id=${res[i].id}`)
            .then(req => {return req.json()})
            .then(re => {
                let subtotal = Number(res[i].amount)*Number(re.cost);
                total += subtotal;
                const entry = `<tr>
                <td>${stt}</td>
                <td>${re.name}</td>
                <td>${re.cost}</td>
                <td>${Number(res[i].amount)}</td>
                <td>${subtotal}</td>
                <td>${res[i].usage}</td>
                </tr>`
                table.innerHTML += entry;
            })
        }
        const calTotal = `
        <tr>
            <td colspan="4" style="text-align: right;">Tổng</td>
            <td>${total}</td>
            <td></td>
        </tr>
        `
        table.innerHTML += calTotal;
    })
})

const checkout = () => {
    location.replace(`/banking?madon=${new URLSearchParams(location.search).get("madon")}&total=${total}`);
}