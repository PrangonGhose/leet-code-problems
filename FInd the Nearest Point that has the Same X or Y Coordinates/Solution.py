class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        my_pos = [x,y]
        valid_points = []
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                valid = [points[i][0], points[i][1]]
                valid_points.append(valid)
        if len(valid_points) == 0:
            return -1
        else:
            dis = []
            pos = []
            for i in valid_points:
                md = abs(my_pos[0]-i[0]) + abs(my_pos[1] - i[1])
                dis.append(md)
            sort_dis = sorted(dis)
            for i in range(len(dis)):
                if dis[i] == sort_dis[0]:
                    pos.append(i)
            shortest = points.index(valid_points[pos[0]])
        return shortest