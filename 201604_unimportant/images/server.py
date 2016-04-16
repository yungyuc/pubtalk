from multiprocessing.connection import Listener
with Listener(("localhost", 8723), authkey=b"mypapaword") as listener:
    with listener.accept() as conn:
        func, data = conn.recv()
        print(func(data))
