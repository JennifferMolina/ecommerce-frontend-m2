# ecommerce_m3.py

catalogo = [
    {"id": 1, "nombre": "Mouse Inalámbrico", "categoria": "tecnología", "precio": 19990},
    {"id": 2, "nombre": "Audífonos Gamer", "categoria": "tecnología", "precio": 29990},
    {"id": 3, "nombre": "Teclado Mecánico", "categoria": "tecnología", "precio": 39990},
    {"id": 4, "nombre": "Notebook Lenovo", "categoria": "tecnología", "precio": 499990},
    {"id": 5, "nombre": "Monitor Full HD", "categoria": "tecnología", "precio": 129990}
]

carrito = []


def mostrar_menu():
    print("\nBienvenido/a a tu Ecommerce")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")


def listar_productos(catalogo):
    print("\nCatálogo de productos:")
    for producto in catalogo:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Categoría: {producto['categoria']} | Precio: ${producto['precio']}")


def buscar_producto_por_id(catalogo, id_producto):
    for producto in catalogo:
        if producto["id"] == id_producto:
            return producto
    return None


def buscar_productos(catalogo):
    texto = input("\nIngrese nombre o categoría a buscar: ").lower()
    encontrados = []

    for producto in catalogo:
        nombre = producto["nombre"].lower()
        categoria = producto["categoria"].lower()

        if texto in nombre or texto in categoria:
            encontrados.append(producto)

    if len(encontrados) > 0:
        print("\nProductos encontrados:")
        for producto in encontrados:
            print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Categoría: {producto['categoria']} | Precio: ${producto['precio']}")
    else:
        print("\nNo se encontraron productos con esa búsqueda.")


def agregar_al_carrito(catalogo, carrito):
    try:
        id_producto = int(input("\nIngrese el ID del producto que desea agregar: "))
        producto = buscar_producto_por_id(catalogo, id_producto)

        if producto is None:
            print("Error: el ID ingresado no existe.")
            return

        cantidad = int(input("Ingrese la cantidad: "))

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
            return

        item = {
            "id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad
        }

        carrito.append(item)
        print(f"Producto agregado: {producto['nombre']} x {cantidad}")

    except ValueError:
        print("Error: debe ingresar números válidos.")


def calcular_total(carrito):
    total = 0

    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total = total + subtotal

    return total


def mostrar_carrito_y_total(carrito):
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
    else:
        print("\nCarrito de compras:")

        for item in carrito:
            subtotal = item["precio"] * item["cantidad"]
            print(f"ID: {item['id']} | Nombre: {item['nombre']} | Cantidad: {item['cantidad']} | Precio unitario: ${item['precio']} | Subtotal: ${subtotal}")

        total = calcular_total(carrito)
        print(f"\nTotal a pagar: ${total}")


def vaciar_carrito(carrito):
    carrito.clear()
    print("\nEl carrito fue vaciado correctamente.")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_productos(catalogo)

    elif opcion == "2":
        buscar_productos(catalogo)

    elif opcion == "3":
        agregar_al_carrito(catalogo, carrito)

    elif opcion == "4":
        mostrar_carrito_y_total(carrito)

    elif opcion == "5":
        vaciar_carrito(carrito)

    elif opcion == "0":
        print("\nGracias por visitar TecnoStore. ¡Hasta pronto!")
        break

    else:
        print("\nOpción inválida. Intente nuevamente.")