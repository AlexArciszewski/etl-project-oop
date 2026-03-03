from colorama import init, Fore, Back, Style


def show_logo() -> None:
    """Creates the program logo""" 
           
    logo:str = r"""
███████╗████████╗██╗     
██╔════╝╚══██╔══╝██║     
█████╗     ██║   ██║       
██╔══╝     ██║   ██║       
███████╗   ██║   ███████╗
╚══════╝   ╚═╝   ╚══════╝

        E  T  L
       Project
"""
    print(Fore.RED + Style.BRIGHT + logo)