const contador = document.querySelector("#contador-carrito");
const totalCarrito = document.querySelector("#total-carrito");
const botonesAgregar = document.querySelectorAll(".agregar-carrito");
const botonVaciar = document.querySelector("#vaciar-carrito");

let cantidad = Number(localStorage.getItem("carrito")) || 0;

function actualizarContador() {
    if (contador) {
        contador.textContent = cantidad;
    }

    if (totalCarrito) {
        totalCarrito.textContent = cantidad;
    }
}

botonesAgregar.forEach(function (boton) {
    boton.addEventListener("click", function () {
        cantidad = cantidad + 1;
        localStorage.setItem("carrito", cantidad);
        actualizarContador();
    });
});

if (botonVaciar) {
    botonVaciar.addEventListener("click", function () {
        cantidad = 0;
        localStorage.setItem("carrito", cantidad);
        actualizarContador();
    });
}

actualizarContador();