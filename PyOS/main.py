from icecream import ic

def manipulate_os():
    import os
    import multiprocessing

    ic(os.environ['HOME'])

    # environment variable configuration
    # os.environ['variable'] = 'value' 

    ic(os.getcwd())
    ic(os.makedirs('test', exist_ok=True))
    ic(os.listdir('.'))
    ic(os.rmdir('test'))
    ic(os.listdir('.'))

    ic(os.cpu_count())
    ic(multiprocessing.cpu_count())

    # os.urandom() generate more safer random code than random package
    ic(os.urandom(10))

def manipulate_io():
    """
    Use IO to deal with streaming
    """
    import io
    from unittest.mock import patch

    stream = io.StringIO("this is test\n")
    ic(stream.getvalue())
    ic(len(stream.getvalue()))
    # set offset and read until the position of offset
    ic(stream.read(10))
    # return the current offset of the stream
    ic(stream.tell())
    # move the offset to the end of the stream
    ic(stream.seek(0, io.SEEK_END))
    ic(stream.close())
    try:
        # error: when stream is closed, stream can't be written
        ic(stream.write('test'))  
    except ValueError as e:
        ic(e)

if __name__ == "__main__":
    # manipulate_os()
    manipulate_io()
