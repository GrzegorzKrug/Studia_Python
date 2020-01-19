import time
import random
import string
from hashlib import sha256
from Crypto.Hash import SHA256


class TimeServer:
    @classmethod
    def time(cls):
        time_now = time.time() * 1000
        return int(time_now)

    @classmethod
    def time_str(cls):
        t = str(cls.time())
        # print
        return t


class BitCoinBlock:
    shaHash = sha256()

    def __init__(self):
        pass

    def next_Block(self, pay_list, block, J):
        new_block = self.generate_Block(
            pay_list=pay_list, previous_hash=block['final_hash'],
            num=block['block_num']+1, J=J
        )

        return new_block

    def generate_Block(self, pay_list=None, previous_hash=None, num=0, J=3):

        if type(pay_list) is str:
            pay_list = [pay_list]
        elif pay_list is None:
            pay_list = [""]

        if previous_hash is None:
            previous_hash = "None"

        timestamp = TimeServer.time_str()
        merkle_hash = self.merkle_tree(pay_list)
        combine_text = timestamp + merkle_hash + str(num)
        nonce, mine_time, final_hash = self.find_nonce(combine_text, J=J)

        block = {"block_num": num,
                 "mine_time": mine_time,
                 "prev_hash": previous_hash,
                 "merkle": merkle_hash,
                 "nonce": nonce,
                 "final_hash": final_hash}
        return block

    def find_nonce(self, str_input, J):
        flag_found = False
        time0 = time.time()
        nonce = 0
        while not flag_found:
            final_hash = self.hash(str_input+str(nonce))
            if final_hash.startswith("0"*J):
                time_end = time.time()
                flag_found = True
                duration = time_end - time0
            else:
                nonce += 1

        return nonce, duration, final_hash

    @classmethod
    def hash(cls, text):
        cls.shaHash.update(text.encode('utf-8'))
        response = cls.shaHash.hexdigest()
        return response

    def merkle_tree(self, transations_list):
        tree_leaves = []
        if len(transations_list) < 1:
            raise ValueError("List is too short")

        # First Loop
        for transaction in transations_list:
            new_hash = self.hash(transaction)
            tree_leaves.append(new_hash)

        # Loop to the End
        while(len(tree_leaves) >= 1):
            # print("leaves:\n", tree_leaves)
            old_tree_leaves = tree_leaves
            tree_leaves = []
            for i in range(0, len(old_tree_leaves), 2):
                try:
                    combi_hash = old_tree_leaves[i] + old_tree_leaves[i+1]
                except IndexError:
                    combi_hash = old_tree_leaves[i] + "None"

                new_hash = self.hash(combi_hash)
                tree_leaves.append(new_hash)

            if len(tree_leaves) == 1:
                break

        assert(len(tree_leaves) == 1), "Lenght of tree leaves is not 1"
        # print("Leaves at end\n", tree_leaves)
        return tree_leaves[0]


class Miner:
    pass


pay_list1 = ['Bob pays Alice',
             'Tom pays bob']
pay_list2 = ["Trump buys wall",
             "Putin hires spies",
             "Iran buys rockets"]

J = 5

BC = BitCoinBlock()

print("="*30, "\n")
init_block = BC.generate_Block(J=J)
print(init_block)

print("="*30, "\n")
block1 = BC.next_Block(pay_list1, init_block, J=J)
print(block1)

print("="*30, "\n")
block2 = BC.next_Block(pay_list2, block1, J=J)
print(block2)
# for x in range(5):
#     abc.find_hash(test_string, 5)
