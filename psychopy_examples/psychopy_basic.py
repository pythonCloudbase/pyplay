from psychopy import visual, core

win = visual.Window()
msg = visual.TextStim(win, text=u"\u00A1Hello peeps")

msg.draw()
win.flip()
core.wait(60)
win.close()