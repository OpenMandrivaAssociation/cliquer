env = Environment()   # Create an environmnet

lib_target  = "cliquer"
lib_sources = ["cl.c","cliquer.c","graph.c","reorder.c"]

libcliquer = env.SharedLibrary(target = lib_target, source = lib_sources)

env.Install(dir = "Build", source = libcliquer)
env.Alias('install', ['Build'])

