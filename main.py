from hashlib import sha256
import orjson


class Block(object):
    def __init__(self, transaction, data_create, name_creator, hash_block, number_of_block):
        self.transaction = transaction
        self.data_create = data_create
        self.name_creator = name_creator
        self.hash_block = hash_block
        self.number_of_block = number_of_block

    def compute_hash(self):
        pass


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.create_genezis_block()

    def create_genezis_block(self):
        pass

    def last_block(self):
        return self.chain[-1]

    def mining(self):
        pass





