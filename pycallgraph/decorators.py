import functools

from .pycallgraph import PyCallGraph
from .output import GraphvizOutput


def trace(output=None, config=None):
    def inner(func):
        @functools.wraps(func)
        def exec_func(*args, **kw_args):

            graphviz = GraphvizOutput()
            graphviz.output_file = output

            with(PyCallGraph(output=graphviz, config=config)):
                return func(*args, **kw_args)

        return exec_func

    return inner
