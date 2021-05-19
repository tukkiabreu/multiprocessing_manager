from collections.abc import Iterable
from multiprocessing.pool import Pool
from pandas import DataFrame
import sys


class RunFunctions:
    """This class runs the same function multiple times in parallel.

        To use, create the class while passing the function name and a list of
        arguments to be used by each instance.
        The class then will run one instance of the function for each
        list of arguments in parallel, then save the return values in the
        attribute self.return_values

        To change the arguments use the method self.set_arguments()

        To change the function you will need to create another instance of the class.
    """
    def __init__(self, runnable_function, *args, sys_out=None, n_processes=None):
        if sys_out is not None:
            sys.stdout = sys_out
        self.arguments = args
        self.n_processes = n_processes
        self.return_values = self.__run(runnable_function)

    def set_arguments(self, *args):
        self.arguments = args

    def __run(self, runnable):
        with Pool(self.n_processes) as pool:
            results = []
            for function_arguments in self.arguments:
                if isinstance(function_arguments, Iterable) and not isinstance(function_arguments, (DataFrame, str)):
                    returned = pool.apply_async(runnable, function_arguments)
                else:
                    returned = pool.apply_async(runnable, (function_arguments,))

                results.append(returned)
            returnable = [res.get() for res in results]
        return returnable

    @staticmethod
    def __error_manager():
        print(ValueError)
        print("There is something wrong with either the callable function or the arguments")
