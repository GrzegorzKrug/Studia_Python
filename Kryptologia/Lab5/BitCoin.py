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
        combine_text = previous_hash + str(num) + merkle_hash
        nonce, mine_time, hashwithzeros = self.find_nonce(combine_text, J=J)

        final_hash = self.hash(combine_text + str(nonce))

        block = {"block_num": num,
                 "prev_hash": previous_hash,
                 "merkle_hash": merkle_hash,
                 "nonce": nonce,
                 "mine_time": round(mine_time, 6),
                 "hashwithzeros": hashwithzeros,
                 "final_hash": final_hash}
        return block

    def find_nonce(self, str_input, J):
        flag_found = False
        time0 = time.time()
        nonce = 0

        while not flag_found:
            new_string = str_input+str(nonce)
            hashwithzeros = self.hash(new_string)
            if hashwithzeros.startswith("0"*J):
                time_end = time.time()
                flag_found = True
                duration = time_end - time0
            else:
                nonce += 1

        return nonce, duration, hashwithzeros

    @classmethod
    def hash(cls, text):
        shaHash = sha256()
        shaHash.update(text.encode('utf-8'))
        response = shaHash.hexdigest()
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
        return tree_leaves[0]


def validate(block_list):
    for i in range(len(block_list)-1, 0, -1):
        current_block = block_list[i]
        prev_block = block_list[i-1]

        text = current_block['prev_hash'] \
            + str(current_block['block_num']) \
            + current_block['merkle_hash'] \
            + str(current_block['nonce'])

        proof_of_work = BitCoinBlock.hash(text)

        hash_proof = BitCoinBlock.hash(prev_block['prev_hash']
                                       + str(prev_block['block_num'])
                                       + prev_block['merkle_hash']
                                       + str(prev_block['nonce']))

        if not proof_of_work.startswith("0"*J) \
                or current_block['prev_hash'] != hash_proof:
            return False
    return True


def pretty_print(bc_block):
    print("="*30)
    for key, val in bc_block.items():
        print(key.ljust(15), ":", val)
    print("="*30, "\n")


pay_list1 = ['Bob pays Alice',
             'Tom pays bob']
pay_list2 = ["Trump buys wall",
             "Putin hires spies",
             "Iran buys rockets",
             "Elon invest in GIGA factory"]

J = 5
BC = BitCoinBlock()


init_block = BC.generate_Block(J=J)
pretty_print(init_block)

# print("="*30, "\n")
block1 = BC.next_Block(pay_list1, init_block, J=J)
pretty_print(block1)

# print("="*30, "\n")
block2 = BC.next_Block(pay_list2, block1, J=J)
pretty_print(block2)
# for x in range(5):
#     abc.find_hash(test_string, 5)


val = validate([init_block, block1, block2])
print("Validate:", val)
