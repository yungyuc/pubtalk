from multiprocessing.connection import Client
with Client(("localhost", 8723), authkey=b"mypapaword") as conn:
    conn.send((sum, [1, 3, 5]))
