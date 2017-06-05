import importlib


class PyRun():
    SUBSITUTION_VAR = '_l'
    SUBSITUTION_INDEX = '_i'

    def __init__(self,
                 stream, command,
                 var=SUBSITUTION_VAR,
                 index=SUBSITUTION_INDEX,
                 modules=[],
                 print_line=False):

        self.stream = stream
        self.command = command
        self.print_line = print_line

        if self.print_line:
            self.command = "output = ({})".format(
                self.command
            )

        # subsitution variables
        self.var = var
        self.index = index

        # dictionary maintaining all variables in scope for the command
        self._scope = {}

        # import all modules desired for the command
        module_dict = {module: importlib.import_module(module)
                       for module in modules}
        self._update_scope(module_dict)

    def _update_scope(self, scopes):
        self._scope.update(scopes)

    def run_command(self, scopes):
        self._update_scope(scopes)
        exec(self.command, self._scope)
        return self._scope['output'] if self.print_line else None

    def run(self):
        for i, line in enumerate(self.stream):
            output = self.run_command({
                self.var: line.strip(),
                self.index: i
            })
            if output:
                print output
