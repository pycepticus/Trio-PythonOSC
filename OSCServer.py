import trio
from pprint import pprint
from pythonosc.osc_message import OscMessage
from AsyncDispatcher import AsyncDispatcher


    
class TrioOSCServer:

    def __init__(self, ip, port, dispatcher=None):
        self.ip = ip
        self.port = port
        self._map = {}
        self.dispatcher = dispatcher 
        
    async def datagram_received(self, data: bytes, client_address: tuple[str, int]) -> None:
        await self.dispatcher.call_handlers_for_packet(data, client_address)
    
    async def start(self):
        sock = trio.socket.socket(trio.socket.AF_INET, 
                                trio.socket.SOCK_DGRAM)
        await sock.bind((self.ip, self.port))
        while True:
            data, addr = await sock.recvfrom(1024)
            await self.datagram_received(data, addr)
            await trio.sleep(0)



# def main ():
#     #test function to print out the address and value of the message
#     async def testmap(address, value):
#         print(f'{address}: {value}')

#     dispatcher = AsyncDispatcher()
#     dispatcher.map('/avatar/parameters/*', testmap)
#     osc = TrioOSCServer('127.0.0.1', 9001, dispatcher)
#     trio.run(osc.start)
    

# if __name__ == '__main__':
#     main()
