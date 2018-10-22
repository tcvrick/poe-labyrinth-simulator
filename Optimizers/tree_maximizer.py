class TreeMaximizer:

    def __init__(self, max_depth):
        self.max_depth = max_depth

    def get_best_action(self, game_state):
        max_tree = self.maximize(game_state)

        assert max_tree.children
        print(max_tree.children)
        best_action = max_tree.children.value[0]
        return best_action

    def convert_to_action_list(self, tree):
        result = []
        node = tree
        while node.children:
            result.append(tree.children)
            node = node.children
        return result[:-1]

    def maximize(self, game_state, debug=False):
        return self._maximize(game_state, 0, None, 0, debug)

    def _maximize(self, game_state, depth, action, score, debug):
        depth += 1

        value = (action, score)
        parent = self
        children = []

        # Evaluate all of the next level.
        next_game_states = []
        actions = game_state.get_legal_actions()
        for action in actions:
            next_state = game_state.get_next_state(action)
            next_state.world.tick()
            if next_state.world.agent.check_if_dead():
                continue

            score = next_state.world.agent.evaluate()
            if score > -1000:
                next_game_states.append((next_state, action, score))

        if depth <= self.max_depth:
            for next_game_state, action, score in next_game_states:
                children.append(self._maximize(next_game_state, depth, action, score, debug))

            orig_len = len(children)
            if depth + 1 < self.max_depth:
                children = [x for x in children if x.children]
            if len(children) < orig_len:
                print('pruned a dead branch')
        if not debug and children:
            # print('!!!!')
            # print(children)
            children = max(children, key=lambda x: x.value[1])
            # print(children)
            # print('======')
        return Node(value, parent, children)


class Node:

    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children

    def __repr__(self):
        return "Node" + str(self.value)


