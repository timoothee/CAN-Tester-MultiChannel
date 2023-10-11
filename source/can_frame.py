# Working on it

class CanFrame():
    def __init__(self, frame_id: int = 1, brs: int = 1,extented_id_status: bool = True, fd_id_status: bool = True, payload_size: int = 1, payload: int = 1, delay: int = 0):
        self.frame_id = frame_id
        self.extented_id_status = extented_id_status
        self.fd_id_status = fd_id_status
        self.payload_size = payload_size
        self.payload = payload 
        self.delay = delay
        self.brs = ""
        self.id_list = []
        self.brs_list = []
        self.payload_list = []
        self.fd_list = []

    # id
    def set_id(self, new_id):
        self.id_list.append(new_id)

    def get_id(self, index):
        return self.id_list[index]

    # fd flag
    def set_fd_flag(self, new_fd_flag):
        self.fd_list.append(new_fd_flag)

    def get_fdflag(self, index):
        return self.fd_list[index]

    # ext id status
    def set_extflag(self, new_extented_id_status):
        self.extented_id_status = new_extented_id_status

    def get_extflag(self):
        print(self.extented_id_status)
        return self.extented_id_status
    
    # payload
    def set_payload(self, new_payload):
        self.payload_list.append(new_payload)

    def get_payload(self, index):
        return self.payload_list[index]
    
    # brs
    def set_brs(self, new_brs):
        self.brs_list.append(new_brs)

    def get_brs(self, index):
        return self.brs_list[index]

