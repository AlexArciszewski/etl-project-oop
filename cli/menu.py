

class Menu:
    """Menu class"""
    
    
    def __init__(self) -> None:
        pass
    
    
    def run(self) -> None:
        """Application controller"""
        while True:
            print() 
            self.display()
            choice:str = input("Pls choose 1 or 2: ")
            
            if choice == "1":
                try:
                    self._run_etl()
                except Exception as e:
                    print(f"Error:{e}")
            elif choice == "2":
                print("Program will now exit.")
                break
            else:
                print("invalid option")     
        
    
    def display(self) -> None:
        """Method used to show the program Menu"""
        
        print("1 - Run ETL process")
        print("2 - Exit")
    
    
    def _run_etl(self) -> None:
        """Builds components and runs the ETL pipeline."""
        
        pass


if __name__ == "__main__":
    Menu().run()
    
    