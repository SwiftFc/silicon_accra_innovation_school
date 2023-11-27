class Division:
    def divide(self, num,deno):
        try:
            result = num /deno
        except (Exception) as e:
            print(f" Invalid {e}")

        except SyntaxError:
            print("Syntax Error")
        else:
            print(f" result is {result}")
