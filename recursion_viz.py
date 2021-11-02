import functools
import graphviz


def recursion_visualizer(func):
    func_name = func.__name__
    separator = '|  '
    recursion_visualizer.recursion_depth = 0
    recursion_visualizer.call_stack = [] # Store Nodes here
    recursion_visualizer.graph = graphviz.Digraph()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print(f'{separator * recursion_visualizer.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')

        node = f'{recursion_visualizer.recursion_depth}_{func_name}({", ".join(map(str, args))})'
        recursion_visualizer.graph.node(node, node)

        recursion_visualizer.recursion_depth += 1

        if len(recursion_visualizer.call_stack) > 0:
            recursion_visualizer.graph.edge(recursion_visualizer.call_stack[-1], node)

        recursion_visualizer.call_stack.append(node)
        result = func(*args, **kwargs)

        recursion_visualizer.graph.node(node, label=node+' -> '+result)

        recursion_visualizer.recursion_depth -= 1
        recursion_visualizer.call_stack.pop()
        print(f'{separator * (recursion_visualizer.recursion_depth + 1)}|-- return {result}')
        return result
    return wrapper

