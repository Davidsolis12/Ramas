import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre} | {self.telefono} | {self.email}"


class Agenda:
    PATRON_TELEFONO = r"^\d{3}-\d{3}-\d{3}$"
    PATRON_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def __init__(self):
        self.contactos = []

    def validar_telefono(self, telefono):
        return re.match(self.PATRON_TELEFONO, telefono)

    def validar_email(self, email):
        return re.match(self.PATRON_EMAIL, email)

    def añadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono (123-456-789): ")
        email = input("Email: ")

        if not self.validar_telefono(telefono):
            print("❌ Teléfono inválido")
            return

        if not self.validar_email(email):
            print("❌ Email inválido")
            return

        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("✅ Contacto añadido")

    def mostrar_contactos(self):
        if not self.contactos:
            print("Agenda vacía")
            return

        for c in self.contactos:
            print(c)

    def buscar_contacto(self):
        nombre = input("Nombre a buscar: ")
        encontrados = [c for c in self.contactos if nombre.lower() in c.nombre.lower()]

        if not encontrados:
            print("No encontrado")
        else:
            for c in encontrados:
                print(c)

    def eliminar_contacto(self):
        nombre = input("Nombre del contacto a eliminar: ")

        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                self.contactos.remove(c)
                print("Contacto eliminado")
                return

        print("Contacto no encontrado")

    def menu(self):
        while True:
            print("\n--- AGENDA ---")
            print("1. Añadir contacto")
            print("2. Mostrar contactos")
            print("3. Buscar contacto")
            print("4. Eliminar contacto")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.eliminar_contacto()
            elif opcion == "5":
                print("Hasta luego")
                break
            else:
                print("Opción inválida")
                
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()