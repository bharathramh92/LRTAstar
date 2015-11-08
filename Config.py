import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from Environment import environment


class EnvironmentDef:

    def __init__(self):
        self.obstacles_polygon = []
        self.initial_state, self.goal_state = [], []
        self.resolution = 0
        self.read_env_from_file()

    def read_env_from_file(self):
        if not (environment.get('resolution') and environment.get('obstacles') and \
            environment.get('initial_state') and environment.get('goal_state')):
            print("Invalid Environment definition")
            exit(1)
        self.initial_state, self.goal_state = tuple(environment['initial_state']), tuple(environment['goal_state'])
        self.resolution = environment['resolution']
        for obs in environment['obstacles']:
            if not obs.get('shape') and obs.get('property') and obs['property'].get('vertices'):
                print("Shape element not present for the obstacles")
                continue
            if obs['shape'] == 'polygon':
                # print("Polygon with vertices %s" %(np.array(obs['property']['vertices'])/100))
                polygon = Polygon(np.array(obs['property']['vertices']))
                self.obstacles_polygon.append(polygon)
            else:
                print("Undefined shape")
                break

    def draw_env(self):
        fig, ax = plt.subplots()
        colors = 100*np.random.rand(len(self.obstacles_polygon))
        print(colors)
        p = PatchCollection(self.obstacles_polygon, cmap=matplotlib.cm.jet, alpha=0.4)
        p.set_array(np.array(colors))
        ax.add_collection(p)
        plt.colorbar(p)
        plt.plot([self.initial_state[0]], [self.initial_state[1]], 'bs', self.goal_state[0], self.goal_state[0], 'g^')
        plt.axis([0, self.resolution, 0, self.resolution])
        plt.show()

    def __str__(self):
        return "Obstacle list: %s\nInitial State: %s\nGoal State: %s\nResolution: %d\n" \
               % ([cord.xy for cord in self.obstacles_polygon], self.initial_state, self.goal_state, self.resolution)


if __name__ == '__main__':
    env = EnvironmentDef()
    print(str(env))
    env.draw_env()