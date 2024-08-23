const char homePage[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .button {
            height: 50px;
            width: 150px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 1.5px solid black;
            border-radius: 15px;
            background-color: orangered;
            color: white;
        }
        .button:active {
            background-color: rgb(132, 36, 1);
        }
        
        .device_list {
            flex-direction: row;
            flex-wrap: wrap;
        }
        
        .device {
            height: 150px;
            width: 150px;
            display: flex;
            align-items: center;
            flex-direction: column;
            border: 1px solid black;
            border-radius: 15px;
        }
        
        .device > .button {
            width: 75px;
        }
        .address {
            font-size: x-large;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="button" id="scanner">Scan all</div>
        <p>Devices</p>
        <div class="device_list" id="deviceList">
            <!-- <div class="device">
                <p class="address">1</p>
                <div class="button">Test</div>
            </div> -->
        </div>
    </div>
    <script>
        document.querySelector("#scanner").addEventListener("click", () => {
            const container = document.querySelector("#deviceList");
            container.innerHTML = "";
            fetch("/scan")
            .then((response) => {
                return response.json();
            })
            .then((response) => {
                alert(response);
                for (let i in response) {
                    const device = `<div class="device">
                <p class="address">${response[i]}</p>
                <div class="button" onclick="test(${response[i]})">Test</div>
            </div>`;
                    container.innerHTML += device;
                }
            })
        }); 
        const test = (address) => {
            fetch(`/test?device=${address}`)
            .then((response) => {
                alert(response.status);
            })
        }
    </script>
</body>
</html>
)rawliteral";