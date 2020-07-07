import os


def main():
    print("Hello " + os.getenv("PG_HOST")+" (running as "+str(os.getuid())+")")
    # +.os.getenv("PG_HOST")


if __name__ == "__main__":
    main()
