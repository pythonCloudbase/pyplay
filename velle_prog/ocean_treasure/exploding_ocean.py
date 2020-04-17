# can't make out head or tail 
# but it sure works

import math
import random
import tkinter

def odd(n):
    return n & 1

def color(a):
    return 'green' if (odd(a)) else 'blue'

class Map:

    def __init__(self, master, rows=15, columns=15):
        self.master = master
        self.row = random.randrange(rows)
        self.col = random.randrange(columns)
        self.cost = 0
        self.found = False
        Button = tkinter.Button
        self.buttons = []
        options = dict(text = '~~',font='Courier 14')
        for r in range(rows):
            br = []
            self.buttons.append(br)
            for c in range(columns):
                b = Button(
                    master,
                    command = lambda r=r,c=c: self(r,c),
                    fg = color(r+c),
                    **options
                )
                b.grid(row=r,column=c)
                br.append(b)
        master.mainloop()
    
    def __bool__(self):
        return self.found

    def __call__(self, row, col):
        if self:
            self.master.quit()
        distance = int(round(math.hypot(row-self.row, col-self.col)))
        #self.buttons[row][col].configure(text = '{}'.format(distance), bg='yellow',fg='red')

        # exploding variation
        for i in range(-1,2):
            self.buttons[row + i][col +i].configure(text = '{}'.format(distance), bg='yellow',fg='red')
            self.buttons[row][col +i].configure(text = '{}'.format(distance), bg='yellow',fg='red')
            self.buttons[row + i][col].configure(text = '{}'.format(distance), bg='yellow',fg='red')
            self.buttons[row + i][col - i].configure(text = '{}'.format(distance), bg='yellow',fg='red')
            self.buttons[row - i][col + i].configure(text = '{}'.format(distance), bg='yellow',fg='red')


        self.cost += 1
        if not distance:
            print('You win ! at the cost of {} sonar devices.'.format(self.cost))           
            self.found = True

def main():
    root = tkinter.Tk()
    map = Map(root)
    root.destroy()

if __name__ == '__main__':
    main()