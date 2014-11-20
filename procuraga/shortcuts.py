import inspect

def compact(*names):
    caller = inspect.stack()[1][0] # caller of compact()
    vars = {}
    for n in names:
        if n in caller.f_locals:
            vars[n] = caller.f_locals[n]
        elif n in caller.f_globals:
            vars[n] = caller.f_globals[n]
    return vars

def extract(vars):
    caller = inspect.stack()[1][0] # caller of extract()
    for n, v in vars.items():
        caller.f_locals[n] = v   # NEVER DO THIS ;-)
