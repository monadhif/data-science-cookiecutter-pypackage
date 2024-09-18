# from jinja2.ext import Extension
# from rich.console import Console

# class AdditionalPrompts(Extension):

#     def __init__(self, environment):
#         """Jinja2 Extension Constructor."""
#         super().__init__(environment)

#         def additional_prompt():
#             console = Console()
#             while True:
#                 console.print("\nPlease select dependency manager", style="bold white")
#                 console.print("==========================",style="bold white")
#                 use_dependency_manager = input('Please type "poetry", "pipenv" or "none":')
#                 if use_dependency_manager.lower() in ['poetry', 'pipenv', 'none']:
#                     break

#             if use_dependency_manager.lower() == 'none':
#                 while True:
#                     console.print("\nDo you want to create a virtual environment?", style="bold white")
#                     console.print("==========================",style="bold white")
#                     create_virtualenv = input('Please type "yes" or "no":')
#                     if create_virtualenv.lower() in ['yes', 'no']:
#                         break
#             else:
#                 create_virtualenv = 'no'

#             return use_dependency_manager, create_virtualenv

#         environment.globals.update(additional_prompt=additional_prompt)