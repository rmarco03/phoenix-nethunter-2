import platform


def run():

    print("CPU Test")
    print("Architecture:",
          platform.machine())


if __name__ == "__main__":

    run()