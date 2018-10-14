import io
try:

    try:
        file = open('data.txt','w')
        # data = file.read()
        file.write("Hello")
        # print(data)
        file.close()
        # quit()
        # print("Python quit")
    except io.UnsupportedOperation as ex:
        print(ex)
    except BaseException:
        print("error")
    else:
        print("Else executed")
    finally:
        print("I will always execute")
        file.read()

except BaseException:
    print("error")