import tkinter as tk
from cinema_class import Cinema


class Cinema_GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x600')
        self.cinema = Cinema(10, 10)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=0)
        self.hall_frame=tk.Frame(bg='grey',padx=50,pady=50)
        self.hall_frame.grid(row=0, column=0)
        self.ticket_frame=tk.Frame()
        self.ticket_frame.grid(row=1, column=0)
        self.btn_sell=tk.Button(self.ticket_frame,text='Sale ticket',command=self.sell_GUI)
        self.btn_sell.grid(row=1,column=1,sticky='w,e')
        self.btn_return=tk.Button(self.ticket_frame,text='Return ticket',command=self.return_GUI,anchor='w')
        self.btn_return.grid(row=1,column=2,sticky='w,e')
        self.btn_sell=tk.Button(self.ticket_frame,text='Import hall',command=self.import_hall,anchor='e')
        self.btn_sell.grid(row=1,column=3,sticky='w,e')
        self.btn_return=tk.Button(self.ticket_frame,text='Save hall',command=self.cinema.save,anchor='e')
        self.btn_return.grid(row=1,column=4,sticky='w,e')
        self.init_hall()
        self.mainloop()
        
    def init_hall(self):
        tk.Label(self.hall_frame,bg='black',text='SCREEN',fg='white').grid(row=0,columnspan=11, sticky='we')
        self.buttons=[]
        hall = self.cinema.hall_to_matrix()
        for index_row in range(len(hall)):
            tk.Label(self.hall_frame,padx=10,pady=5,text=index_row+1).grid(row=index_row+1,column=0)
            btn_row=[]
            for index_seat in range(len(hall[index_row])):
                if hall[index_row][index_seat]==0:
                    btn=tk.Button(self.hall_frame,padx=10,pady=10, text=index_seat+1, bg='light green',state='disabled')
                else:
                    btn=tk.Button(self.hall_frame,padx=10,pady=10, text=index_seat+1, bg='red',state='disabled')
                btn.grid(row=index_row+1,column=index_seat+1)
                btn_row.append(btn)
            self.buttons.append(btn_row)
    def clear_hall(self):
        for row in self.buttons:
            for seat in row:
                seat.destroy() 
    def import_hall(self):
        self.clear_hall()
        self.cinema.import_from_file()
        self.init_hall()      
    def __enable_btns(self):
        for row in self.buttons:
            for button in row:
                button.config(state='normal')
    def __disable_btns(self):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')    
    def sell_GUI(self):
        self.__enable_btns()
        for row_ind in range(len(self.buttons)):
            for seat_ind in range(len(self.buttons[row_ind])):
                button_for_sell=self.buttons[row_ind][seat_ind]
                button_for_sell.config(command=lambda r=row_ind,s=seat_ind:self.sell_ticket(r+1,s+1))
    def return_GUI(self):
        self.__enable_btns()
        for row_ind in range(len(self.buttons)):
            for seat_ind in range(len(self.buttons[row_ind])):
                button_for_sell=self.buttons[row_ind][seat_ind]
                button_for_sell.config(command=lambda r=row_ind,s=seat_ind:self.return_ticket(r+1,s+1))   
    def sell_ticket(self,row,seat):
        self.cinema.sale_ticket(row,seat)
        self.buttons[row-1][seat-1].config(bg='red')
        self.__disable_btns()        
    def return_ticket(self,row,seat):
        self.cinema.return_ticket(row,seat)
        self.buttons[row-1][seat-1].config(bg='light green')
        self.__disable_btns()

        
        
                
   
  
# if __name__ == "__main__":
#     gui = Cinema_GUI()