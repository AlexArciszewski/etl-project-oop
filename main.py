from interface.menu import Menu
from etl.logger import get_logger


def main() -> None:
    logger = get_logger(__name__)
    logger.info("Application started")
   
    menu = Menu()
    menu.run()
    logger.info("Application finished")

if __name__ == "__main__":
    
    main()
    
