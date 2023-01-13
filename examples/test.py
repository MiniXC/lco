import lco

import multiprocessing

def worker():
    import lco
    print(lco["test"], multiprocessing.current_process().name)

if __name__ == "__main__":
    lco.init("test.yaml")
    print(lco["test"])
    del lco
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()