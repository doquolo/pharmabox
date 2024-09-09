const handleNumpad = (elem) => {
    const inp = elem.textContent;
    const field = document.querySelector("#madon");
    if (inp == 'bksp') {
        field.value = field.value.substring(0, field.value.length - 1);
    } else if (inp == 'enter') {
        handleEnter();
    } else {
        field.value += inp;
    }
}

const handleEnter = () => {
    const field = document.querySelector("#madon")
    fetch(`/getCheckoutInfo?madon=${field.value}`)
    .then(res => {return res.json()})
    .then(data => {
        if (data.state == 'error') {
            alert("Mã đơn không tồn tại!");
            field.value = "";
        } else {
            location.replace(`/checkout?madon=${field.value}`);
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    fetch('/getMachineID')
    .then(req => {return req.json()})
    .then(res => {
        document.querySelector("#ID").textContent = `PharmaBox #${res.id}`
    })
})