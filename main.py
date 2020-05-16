from pipelinex import __version__, configure_paths, FlexibleContext


print("pipelinex version: ", __version__)

project_path, src_path = configure_paths(__file__)
print("project path: ", project_path)
print("src path: ", src_path)

context = FlexibleContext(project_path)
context.run()
