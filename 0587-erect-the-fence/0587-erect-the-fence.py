class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        hull = []


        trees.sort(key=lambda x: (x[0], x[1]))

        def cross(p: List[int], q: List[int], r: List[int]) -> int:

            px, py = p
            qx, qy = q
            rx, ry = r
            return (qy - py) * (rx - qx) - (qx - px) * (ry - qy)

        # Build lower hull: left-to-right scan
        for tree in trees:

            while len(hull) > 1 and cross(hull[-2], hull[-1], tree) < 0:
                hull.pop()
            hull.append(tree)

        # Build upper hull: right-to-left scan
        for tree in reversed(trees):
            while len(hull) > 1 and cross(hull[-2], hull[-1], tree) < 0:
                hull.pop()
            hull.append(tree)


        return [list(x) for x in set(tuple(x) for x in hull)]