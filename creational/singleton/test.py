from creational.singleton.singletone import Singleton

if __name__ == "__main__":
    s = Singleton("AG")
    t = Singleton("RN")
    print(f"instances: {s}, and  {t}")