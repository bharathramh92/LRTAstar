from queue import PriorityQueue
from Config import EnvironmentDef
from State import State


def main():
    env = EnvironmentDef("Environment1.json")
    # env.print_boxes()
    # env.draw_env()
    print(env)
    obstacle_list = []  #Known obstacles for the robot

    def a_star():
        open_set_pq, open_set, closed_set = PriorityQueue(), {}, {}

        goal_state = State(env.goal_state, env.resolution, obstacle_list)
        initial_state = State(env.initial_state, env.resolution, obstacle_list, GOAL_STATE=goal_state)
        open_set_pq.put(initial_state)
        open_set[initial_state.position] = initial_state
        state_examinations, state_generated = 0, 1
        while True:
            if not open_set_pq.empty():
                current_state = open_set_pq.get()
                print(current_state)
                state_examinations += 1
                open_set.pop(current_state.position)
                closed_set[current_state.position] = current_state
            else:
                print('No solution')
                exit()
            if current_state.position == goal_state.position:
                return current_state, state_examinations, state_generated
            else:
                for x in current_state.successor():
                    if x.position in closed_set:
                        continue
                    g_cost = current_state.g+1      #STEP_COST --> 1
                    if x.position not in open_set or g_cost < open_set[x.position].g:
                        x.g = g_cost
                        x.parent = current_state
                        if x.position not in open_set:
                            state_generated += 1
                            open_set[x.position] = x
                            open_set_pq.put(x)

    def tree_traversal():
        current_state, state_examinations, state_generated = a_star()
        path = []
        while current_state.parent is not None:
            path.append(current_state)
            current_state = current_state.parent
        path.reverse()
        print(path)
        print('Total steps were %d, generated %d and expanded %d ' % (len(path), state_generated, state_examinations))
        env.draw_env(path)
    tree_traversal()

if __name__ == '__main__':
    main()