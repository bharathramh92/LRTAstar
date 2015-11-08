from Config import EnvironmentDef


def main():
    env = EnvironmentDef("Environment1.json")
    # print(str(env))
    # env.convert_to_block()
    env.print_boxes()
    env.draw_env()

if __name__ == '__main__':
    main()