from typing import Tuple


class Maze:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:

        self._spaces = set()
        for i in range(0,25):
            for j in range(0,25):
                self._spaces.add((i,j))
        # model maze by providing a O(1) lookup of occupied spaces
        self._walls = set([
            (24,4), (24,5), (24,17), (24,18),
            (23,0), (23,1), (23,2), (23,3), (23,4), (23,5), (23,6), (23,7), (23,8), (23,9),
            (22,0), (22,1), (22,2), (22,3), (22,4), (22,8), (22,14), (22,15), (22,16), (22,17), (22,18), (22,19), (22,20),  
            (21,3), (21,4), (21,5), (21,8), (21,14), (21,15), (21,16), (21,17), (21,18), (21,19), (21,20),
            (20,3), (20,4), (20,5), (20,8), (20,9), (20,10), (20,14), (20,15), (20,16), (20,17), (20,18), (20,19), (20,20),
            (19,8), (19,9), (19,10),
            (18,8), (18,9), (18,10), (18,14), (18,15), (18,16), (18,17), (18,18), (18,19), (18,20),
            (17,0), (17,1), (17,2), (17,3), (17,4), (17,5), (17,6), (17,8),
            (16,10), (16,24),
            (15,10), (15,23), (15,24),
            (14,8), (14,9), (14,10), (14,11), (14,12), (14,15), (14,16), (14,22), (14,23), (14,24),
            (13,10), (13,15), (13,16), (13,21), (13,22), (13,23), (13,24),
            (12,10), (12,15), (12,16), (12,18), (12,21), (12,24),
            (11,4), (11,15), (11,16), (11,18), (11,21),
            (10,15), (10,16), (10,18), (10,21),
            (9,18), (9,21),
            (8,2), (8,3), (8,4), (8,18), (8,21),
            (7,2), (7,3), (7,4), (7,6), (7,7), (7,10), (7,11), (7,12), (7,18),
            (6,2), (6,6), (6,7), (6,10), (6,11), (6,12), (6,18), (6,19), (6,20), (6,21), (6,22), (6,23),
            (5,0), (5,1), (5,2), (5,6), (5,7), (5,10), (5,11), (5,12), (5,18), (5,19), (5,20), (5,21),
            (4,0), (4,1), (4,2), (4,6), (4,7), (4,10), (4,11), (4,12), (4,18), (4,19),
            (3,6), (3,7), (3,10), (3,11), (3,12), (3,18), (3,19),
            (2,10), (2,11), (2,12), (2,18), (2,19),
            (1,18), (1,19),
        ])
        if start in self._walls:
            raise Exception("Start point is a wall: {}".format(start))
        elif start not in self._spaces:
            raise Exception("Start point is not within the maze bounds: {}".format(start))
        else:
            self._start = start 
        if end in self._walls:
            raise Exception("End point is a wall: {}".format(end))
        elif end not in self._spaces:
            raise Exception("End point is not within the maze bounds: {}".format(end))
        else:
            self._end = end

    def getSpaces(self):
        return self._spaces

    def getWalls(self):
        return self._walls
    
    def getStart(self):
        return self._start

    def getEnd(self):
        return self._end

if __name__ == "__main__":
    maze = Maze((0,0), (24,24))
    print(len(maze.getSpaces()))
