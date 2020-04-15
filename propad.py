import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('ProPad Office')

########################## main menu ################################
############################## end main menu #######################

main_menu = tk.Menu()
#file#############
#file icons
new_icon = tk.PhotoImage(file='icons/add-file.png')
open_icon = tk.PhotoImage(file='icons/folder.png')
save_icon = tk.PhotoImage(file='icons/save.png')
saveas_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')


file = tk.Menu(main_menu, tearoff=False)

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')


##########edit
#########edit icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clearall_icon = tk.PhotoImage(file='icons/clear.png')
find_icon = tk.PhotoImage(file='icons/find.png')


edit = tk.Menu(main_menu, tearoff=False)

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X')
edit.add_command(label='Exit',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')

#######toolbar#############
##########toolbar icons####################
tool_bar_icon = tk.PhotoImage(file='icons/toolbar.png')
status_bar_icon = tk.PhotoImage(file='icons/status.png')

view = tk.Menu(main_menu, tearoff=False)

view.add_checkbutton(label='Toolbar',image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Statusbar',image=status_bar_icon,compound=tk.LEFT)


color_theme = tk.Menu(main_menu, tearoff=False)

#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Theme',menu=color_theme)



########################## toolbar ################################
############################## end toolbar #######################

########################## text editor ################################
############################## end text editor #######################

########################## main status bar ################################
############################## end status bar #######################

############################## end main menu functionality #######################
############################## end main menu functionality #######################

main_application.config(menu=main_menu)
main_application.mainloop()