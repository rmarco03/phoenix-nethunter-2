import datetime


def banner():

    print("""
==============================
     Phoenix NetHunter
        Console
==============================
""")


def shell():

    banner()

    while True:

        command = input(
            "phoenix> "
        )

        if command == "exit":

            print(
                "Closing Phoenix Shell"
            )

            break


        elif command == "time":

            print(
                datetime.datetime.now()
            )


        elif command == "help":

            print(
                """
Commands:

help
time
exit

"""
            )


        else:

            print(
                "Unknown command"
            )


if __name__ == "__main__":

    shell()