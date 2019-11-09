import base64
import hashlib

from oracle import encrypt, is_padding_ok, BLOCK_SIZE, _decrypt

##def attack(ciphertext):
##	guessed_clear = b''
##	blocks = get_blocks(ciphertext, BLOCK_SIZE)
##	
##	for block_n in range( len(blocks) - 1, 0, -1 ): #build pair of blocks starting from end of message
##		spliced_ciphertext = blocks[block_n - 1] + blocks[block_n]
##
##		decoded_bytes = b'?' * BLOCK_SIZE #output of block cipher decoding values
##
##		##GET VALUE OF SECRET BYTE byte
##		for byte in range(BLOCK_SIZE - 1, -1, -1):
##			new_pad_len = BLOCK_SIZE - byte
##
##			#Build hacked ciphertext tail with values to obtain desired padding
##			hacked_ciphertext_tail = b''
##			for padder_index in range( 1, new_pad_len ):
##				hacked_ciphertext_tail += bytearray.fromhex('{:02x}'.format( new_pad_len ^ decoded_bytes[byte + padder_index] ) )
##			
##			for i in range( 0, 256 ):
##				attack_str = bytearray.fromhex( '{:02x}'.format( ( i ^ spliced_ciphertext[byte] ) ) )
##				hacked_ciphertext = spliced_ciphertext[:byte] + attack_str + hacked_ciphertext_tail + spliced_ciphertext[byte + 1 + new_pad_len - 1:]
##
##				if( is_padding_ok( hacked_ciphertext ) ):
##					test_correctness = hacked_ciphertext[:byte - 1] + bytearray.fromhex( '{:02x}'.format( ( 1 ^  hacked_ciphertext[byte] ) ) )  + hacked_ciphertext[byte:]
##					if( not is_padding_ok( test_correctness ) ):
##						continue
##					
##					decoded_bytes = decoded_bytes[:byte] + bytearray.fromhex('{:02x}'.format( hacked_ciphertext[byte] ^ new_pad_len ) ) + decoded_bytes[byte + 1:]
##					guessed_clear = bytearray.fromhex('{:02x}'.format( i ^ new_pad_len ) ) + guessed_clear
##					break	
##	return guessed_clear[:-guessed_clear[-1]] #remove padding!

def attack(ciphertext):
        output = b''
        blocks = get_blocks(ciphertext, BLOCK_SIZE)
        for i in range( 0, 256 ):
                fake_cipher = spliced_ciphertext[:byte] + attack_str + hacked_ciphertext_tail + spliced_ciphertext[byte + 1 + new_pad_len - 1:]
        return output

def get_blocks(ciphertext, siz):
        out = [ciphertext[i:i+siz] for i in range(0, len(ciphertext), siz)]        
        return out

def run():
    messages = ([b"In symmetric cryptography, the padding oracle attack can be applied to the CBC mode of operation"])
    #messages[0][5] = b"E"
    for msg in messages:
        this_cipher = encrypt(msg)
        
        cracked_msg = attack(this_cipher)
        
        print(f'{msg}\n{cracked_msg}')

        


if __name__ == '__main__':
        run()
