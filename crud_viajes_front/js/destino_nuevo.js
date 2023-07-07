function guardar() {
    let n = document.getElementById("nombre").value
    let p = parseFloat(document.getElementById("precio").value)
    let e = parseInt(document.getElementById("estadia").value)
    let i = document.getElementById("imagen").value

    // {
    //     "imagen": "https://picsum.photos/200/300?grayscale",
    //     "nombre": "MICROONDAS",
    //     "precio": 50000,
    //     "stock": 10
    //   }

    let destino = {
        nombre: n,
        precio: p,
        estadia: e,
        imagen: i
    }
    let url = "http://localhost:5000/destinos"
    var options = {
        body: JSON.stringify(destino),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./destinos.html";  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}

