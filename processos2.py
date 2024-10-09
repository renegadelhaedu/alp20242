import multiprocessing

def processoFilho(conn):
    conn.send("Pai, eu te amo")
    conn.close()


def processoPai(conn):
    msg = conn.recv()
    print(f"Pai recebeu: {msg}")


if __name__ == "__main__":
    pai_conn, filho_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=processoFilho, args=(filho_conn,))
    p.start()

    processoPai(pai_conn)
    p.join()
