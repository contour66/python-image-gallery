import os


def main():
    print("Hello " + os.getenv("PG_HOST"))
    # +.os.getenv("PG_HOST")


if __name__ == "__main__":
    main()
