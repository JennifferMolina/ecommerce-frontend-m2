// Seleccionar el contador del carrito
const contador = document.querySelector("#contador-carrito");

// Seleccionar todos los botones "Agregar al carrito"
const botones = document.querySelectorAll(".agregar-carrito");

// Variable para guardar la cantidad de productos
let cantidad = 0;

// Recorrer todos los botones
botones.forEach(function(boton) {

    boton.addEventListener("click", function() {

        cantidad = cantidad + 1;

        contador.textContent = cantidad;

    });

});