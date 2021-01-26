import os

def config_file_readIP_Port(conf_file_name):
    c_ip=None
    c_port=None
    try:
        config_fhandle = open(conf_file_name, "r")
        try:
            line_count = 0
            for line in config_fhandle:
                if line != "\n":
                    line_count += 1
            config_fhandle.close()
        except:
            print("e_cf01")
        
        if line_count > 0:
            config_fhandle = open(conf_file_name, "r")
            try:
                for line in config_fhandle:
                    if line.startswith('IP'):
                        line=line.split("=")
                        c_ip=line[1]
                        c_ip=str(c_ip)
                        c_ip = c_ip.rstrip("\n")
                        continue
                    elif line.startswith('Port'):
                        line=line.split("=")
                        c_port=line[1]
                        c_port=str(c_port)
                        c_port = c_port.rstrip("\n")
            except:
                print("IP/port issue")
        else:
            print("file empty")
    except:
        print("something went wrong with the file")
    return c_ip,c_port

def config_file_create(conf_file_name):
    conf_file_available = os.path.isfile(conf_file_name)
    if conf_file_available is False:
        try:
            fhandle= open(conf_file_name,"x")
            fhandle.close()
        except:
            print("creation of file is not possible!")

def writeIPPort_configfile(conf_file_name, ip, port):
    try:
        config_fhandle = open(conf_file_name, "w")
        config_fhandle.write("IP="+ ip +"\n")
        config_fhandle.write("Port="+ port +"\n")
        config_fhandle.close()
    except:
        print("something went wrong while writing file")
