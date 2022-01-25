import inspect
import itertools

class Logic:
    def __init__(self, v):
        self._val = max(min(1, int(v)), 0)

    def set(self, v) -> None:
        """ If for some reason you want to set a value, use this. """
        self._val = max(min(1, int(v)), 0)

    @staticmethod
    def print_truthtable(fn):
        """ Print a truth table for a given logic function.
            The function can take any number of arguments. """

        assert inspect.isfunction(fn), "Argument 'fn' must be a function"
        params = inspect.signature(fn).parameters

        print("Parameters of the function:", params)
        # TODO: Generate a truth table. Look at itertools.product - that can be helpful.
        # Perhaps you'll get inspired by another 
        ...

        # Following snippets might also be helpful:

        # Create a list of parameters. Number of items in the list
        # is the same as the number of parameters fn takes.
        args = [Logic(0)] * len(params)

        # Make a string with a pretty function name.
        pretty_func_name = f"{fn.__name__}({','.join(map(str, args))})"
        # nb. Don't quite need to know how it works.
        # If you're curious come and ask me after the lesson.

        print(f"Calling {pretty_func_name} => {fn(*args)}")
        raise NotImplementedError("Don't know how to generate the truth table. Yet... (meaning code it yourself, I'm happy to help)")

    @staticmethod
    def is_equivalent(fn1, fn2):
        """ Given two functions taking the same number of arguments, check if they are
            equivalent - for the same inputs they produce the same output. """
        
        assert callable(fn1), "Parameter fn1 must be a function"
        assert callable(fn2), "Parameter fn2 must be a function"

        f1p = inspect.signature(fn1).parameters
        f2p = inspect.signature(fn2).parameters
        assert len(f1p) == len(f2p), "fn1 and fn2 must take the same number of parameters"

        for args in itertools.product([Logic(0), Logic[1]], repeat=len(f1p)):
            ...
        raise NotImplementedError("Don't know how to commpare functions. Yet... (meaning code it yourself, I'm happy to help)")

    # Get nice strings when we print Logic variables.
    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "1" if self._val >= 1 else "0"

    # Operator overloads - this takes care of automatically 
    def __int__(self) -> int:
        assert self._val in [0, 1]
        return self._val

    def __bool__(self) -> bool:
        assert self._val in [0, 1]
        return bool(self._val)

    # Operator overloads - this allows us to do A + B and get the right behaviour.
    def __add__(self, other) -> 'Logic':
        """ A + B implements logical OR. """
        return Logic(int(self) + int(other))

    def __or__(self, other) -> 'Logic':
        """ A | B implements logical OR. """
        return self.__add__(other)

    def __mul__(self, other) -> 'Logic':
        """ A * B implements logical AND. """
        return Logic(int(self) * int(other))

    def __and__(self, other) -> 'Logic':
        """ A & B implements logical AND. """
        return self.__mul__(other)

    def __invert__(self) -> 'Logic':
        """ ~A implements logical NOT. """
        return Logic(1 - self._val)

    def __xor__(self, other) -> 'Logic':
        """ A ^ B implement logical XOR. """
        raise NotSupportedErr("Don't know how to XOR. Yet... (meaning code it yourself, I'm happy to help)")

    def __eq__(self, other) -> bool:
        return bool(self) == bool(other)
