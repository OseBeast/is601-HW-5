import pkgutil
import importlib
import multiprocessing
from app.commands import CommandHandler
from app.commands import Command
#from app.commands.exit import ExitCommand
#from app.commands.menu import MenuCommand
#from app.commands.add import AddCommand
#from app.commands.subtract import SubtractCommand
#from app.commands.multiply import MultiplyCommand
#from app.commands.divide import DivideCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Register commands here
        self.load_plugins()
        #self.command_handler.register_command("exit", ExitCommand())
        #self.command_handler.register_command("menu", MenuCommand())
        #self.command_handler.register_command("add", AddCommand())
        #self.command_handler.register_command("subtract", SubtractCommand())
        #self.command_handler.register_command("multiply", MultiplyCommand())
        #self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
