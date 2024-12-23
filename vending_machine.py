import os
import sys

# Datos iniciales de los libros
books = [
    {"id": 1, "name": "El eco del destino - Gema Bonnin", "price": 15000, "stock": 10},
    {"id": 2, "name": "Trenza del mar esmeralda - Brandon Sanderson", "price": 18000, "stock": 8},
    {"id": 3, "name": "Yumi y el pintor de pesadillas - Brandon Sanderson", "price": 16000, "stock": 5},
    {"id": 4, "name": "Icarus - K. Ancrus", "price": 15000, "stock": 10},
    {"id": 5, "name": "The Seven Year Slip - Ashley Poston", "price": 17000, "stock": 7},
    {"id": 6, "name": "Donde los arboles cantan - Laura Gallego", "price": 20000, "stock": 9},
    {"id": 7, "name": "Vicious - V. E. Schwab", "price": 19000, "stock": 6},
    {"id": 8, "name": "Hija de humo y hueso - Laini Taylor", "price": 16000, "stock": 10},
    {"id": 9, "name": "La biblioteca de la medianoche - Matt Haig", "price": 15000, "stock": 8},
    {"id": 10, "name": "La ira y el amanecer - Renee Ahdieh", "price": 17000, "stock": 10},
    {"id": 11, "name": "Novia - Ali Hazelwood", "price": 15000, "stock": 12},
    {"id": 12, "name": "Lazos de sangre - Octavia E. Butler", "price": 20000, "stock": 7},
    {"id": 13, "name": "Check Mate - Kennedy Fox", "price": 15000, "stock": 8},
    {"id": 14, "name": "Manana, y manana, y manana - Gabrielle Zevin", "price": 19000, "stock": 6},
    {"id": 15, "name": "Lore Olympus - Rachel Smythe", "price": 21000, "stock": 5},
]

def clear_screen():
    # Limpia la pantalla para que el menu sea mas claro
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code):
    # Imprime texto con colores ANSI
    print(f"\033[{color_code}m{text}\033[0m")

def show_books():
    # Muestra el catalogo de libros
    print_colored("\nCatalogo de libros:\n", "1;36")
    print(f"{'ID':<5}{'Nombre':<40}{'Precio':<15}{'Stock':<10}")
    print(f"{'-'*5}{'-'*40}{'-'*15}{'-'*10}")
    for book in books:
        print(f"{book['id']:<5}{book['name'][:40]:<40}${book['price']:<15,}{book['stock']:<10}")

def get_book_by_id(book_id):
    # Busca un libro por su ID
    return next((book for book in books if book['id'] == book_id), None)

def validate_continue():
    # Pregunta al usuario si quiere seguir comprando
    while True:
        choice = input("\n¿Desea comprar otro producto? (s/n): ").strip().lower()
        if choice in ['s', 'n']:
            return choice == 's'
        print_colored("\nEntrada invalida. Por favor ingrese 's' para si o 'n' para no.", "1;35")

def get_customer_name():
    # Obtiene el nombre del cliente
    while True:
        name = input("\nIngrese su nombre: ").strip()
        if name:
            return name
        print_colored("\nEl nombre no puede estar vacio. Intente de nuevo.", "1;35")

def vending_machine():
    while True:
        cart = []
        total = 0
        clear_screen()
        show_books()

        while True:
            try:
                # Solicita el ID del libro
                book_id = int(input("\nIngrese el ID del libro que desea comprar: "))
                book = get_book_by_id(book_id)

                if not book:
                    print_colored("\nEl ID ingresado no corresponde a ningun libro. Intente de nuevo.", "1;35")
                    continue

                # Muestra el libro seleccionado
                print_colored(f"\nSelecciono: {book['name']} - ${book['price']:,}", "1;36")
                quantity = int(input("Ingrese la cantidad que desea comprar: "))

                # Valida que haya suficiente stock
                if quantity > book['stock']:
                    print_colored("\nCantidad no disponible en stock. Intente con una cantidad menor.", "1;35")
                    continue

                # Agrega el producto al carrito
                book['stock'] -= quantity
                cart.append({"name": book['name'], "quantity": quantity, "price": book['price']})
                total += book['price'] * quantity
                print_colored("\nProducto agregado al carrito.", "1;36")

                if not validate_continue():
                    break

            except ValueError:
                print_colored("\nEntrada invalida. Intente de nuevo.", "1;35")

        clear_screen()
        print_colored("\nResumen de la compra:\n", "1;36")
        print(f"{'Producto':<20}{'Cantidad':<10}{'Precio Total':<15}")
        print(f"{'-'*20}{'-'*10}{'-'*15}")
        for item in cart:
            print(f"{item['name'][:20]:<20}{item['quantity']:<10}${item['price'] * item['quantity']:<15,}")

        print(f"\nMonto total sin descuento: ${total:,}")

        # Solicita el metodo de pago
        payment_method = input("\nIngrese metodo de pago (credito/debito): ").strip().lower()
        if payment_method == 'credito':
            discount = total * 0.03
            total_with_discount = total - discount
            print_colored(f"\nDescuento aplicado (3%): -${discount:,}", "1;35")
            print_colored(f"\nMonto final con descuento: ${total_with_discount:,}", "1;36")
        else:
            total_with_discount = total

        # Muestra el resumen final de la compra
        customer_name = get_customer_name()
        print_colored(f"\nResumen final de la compra:", "1;36")
        print_colored(f"\nCliente: {customer_name}", "1;36")
        print(f"{'Producto':<20}{'Cantidad':<10}{'Precio Total':<15}")
        print(f"{'-'*20}{'-'*10}{'-'*15}")
        for item in cart:
            print(f"{item['name'][:20]:<20}{item['quantity']:<10}${item['price'] * item['quantity']:<15,}")
        print_colored(f"\nCantidad total de productos comprados: {sum(item['quantity'] for item in cart)}", "1;36")
        print_colored(f"Monto final sin descuento: ${total:,}", "1;35")
        if payment_method == 'credito':
            print_colored(f"Monto final con descuento: ${total_with_discount:,}", "1;36")
        else:
            print_colored(f"Monto final a pagar: ${total_with_discount:,}", "1;36")

        print_colored("\nGracias por su compra. Volviendo al catalogo...", "1;36")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    vending_machine()
