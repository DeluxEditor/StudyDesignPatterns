from mainwindow import Window

if __name__ == "__main__":
    handle = Window()
    handle2 = Window()
    handle.title("DAW")
    handle.geometry("1280x720")
    handle2.title("DAW")
    handle2.geometry("1280x720")

    assert(handle is handle2) # Without singleton pattern, this should fail that the two windows are not the same object (instance)

    handle.mainloop()
    handle2.mainloop()
