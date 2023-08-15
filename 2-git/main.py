class Main:
    def run(self):
        option = self.get_option()

        a, b = (None, None)

        while option:
            if option == 1:
                a = float(input("Ingrese valor 1\n"))
            elif option == 2:
                b = float(input("Ingrese valor 2\n"))
            elif not a or not b:
                print("Debe ingresar ambos valores primero")
            elif option == 3:
                print(self.sum(a, b))
            elif option == 4:
                print(self.sub(a,b))
            elif option == 5:
                print(self.mul(a, b))
            elif option == 6:
                print(self.div(a, b))

            option = self.get_option()

    def get_option(self):
        print("1. Ingresar valor 1")
        print("2. Ingresar valor 2")
        print("3. Mostrar suma")
        print("4. Mostrar resta")
        print("5. Mostrar multiplicación")
        print("6. Mostrar división")
        print("7. Salir")

        option = int(input("Elija una opción:\n"))

        if option == 7:
            print("Adiós")
            return None

        if option < 1 or option > 7:
            print("Opción inválida")

        return option

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2


if __name__ == '__main__':
    Main().run()
