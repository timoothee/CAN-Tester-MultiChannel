
class Test_Module():
    def __init__(self):
        ...

    def negate_payload(self, payload):
        self.paylod_lenght = len(payload)
        self.negated_payload = int(payload, 16) ^ 0xffffffffffffffff
        return(hex(self.negated_payload)[-self.paylod_lenght:])

    def increment_payload(self, payload: list):
        num = ''
        for item in payload:
            item = int(item, 16) + 1
            num += str(hex(item)[2:])
        return(num)

    def decrement_payload(self, payload: list):
        num = ''
        print(payload)
        for item in payload:
            print(item)
            item = int(item, 16) - 1
            print(item)
            print(hex(item))
            num += str(hex(item)[2:])
            print('num', num)
        return(num)
    def echo(self, payload):
        return payload