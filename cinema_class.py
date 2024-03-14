
import pathlib
import json

class Cinema:
    
    def __init__(self,rows,sits) -> None:
        self.sits=sits
        self.rows=rows
        self.hall=[1<<sits for n in range(rows)]
        
    def import_from_file(self):
        with open(pathlib.Path(__file__).parent.joinpath('cinema_hall.json'),'r') as f:
            print(f)
            
            text=f.read()
       
            self.hall=json.loads(text)
            self.rows = len(self.hall)
            self.sits = len(f'{self.hall[0]:b}') - 1         
            pass
    def save(self):
        with open(pathlib.Path(__file__).parent.joinpath('cinema_hall.json'),'w') as f:
            json.dump(self.hall,f)
            pass
    def sale_ticket(self,row,sit):
        # self.print_hall()
        # row,sit=self.menu()
        # print(self.hall[row-1])
        # print(sit)
        sit=self.sits-sit
        self.hall[row-1] = self.set_bit(self.hall[row-1],sit)        
        pass
    def return_ticket(self,row,sit):
        sit=self.sits-sit
        self.hall[row-1] = self.clear_bit(self.hall[row-1],sit)
        pass
    
    def hall_to_matrix(self):
        
        return [
            [int(c) for c in f"{row:b}"[1:]] 
            for row in self.hall
        ]
    
  
    
    @staticmethod
    def set_bit(value,bit_number):return value|(1<<bit_number)
    @staticmethod
    def clear_bit(value,bit_number):return value&~(1<<bit_number)
    @staticmethod
    def get_bit(value,bit_number):return 1&(value>>bit_number)


