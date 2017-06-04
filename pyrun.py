import importlib


class PyRun():

    def __init__(self,
                 stream,
                 command,
                 linewise,
                 var,
                 index,
                 modules):

        self.stream = stream
        self.command = command
        self.linewise = linewise

        # subsitution variables
        self.var = var
        self.index = index

        # dictionary maintaining all variables in scope for the command
        self.scope = {}

        # import all modules desired for the command
        module_dict = {module: importlib.import_module(module)
                       for module in modules}
        self._update_scope(module_dict)

    def _update_scope(self, scopes):
        self.scope.update(scopes)

    def run_command(self, scopes):
        self._update_scope(scopes)
        exec(self.command, self.scope)

    def run(self):
        if self.linewise:
            for i, line in enumerate(self.stream):
                self.run_command({
                    self.var: line.strip(),
                    self.index: i
                })
        else:
            self.run_command({self.var: self.stream.read()})