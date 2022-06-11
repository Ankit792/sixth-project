import math
key = input('Enter key : ')

# Encryption
def encryption(msge):
    cipher = ""
    k_indx = 0                               # track key indices

    msg_len = float(len(msge))
    msg_lst = list(msge)
    key_lst = sorted(list(key))

    column = len(key)                        # calculate column of the matrix
    row = int(math.ceil(msg_len / column))   # calculate maximum row of the matrix

    # add the padding character '*' in empty,
    # the empty cell of the matrix
    fill_blank = int((row * column) - msg_len)
    msg_lst.extend('*' * fill_blank)

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i: i + column]
        for i in range(0, len(msg_lst), column)]
    count = 0
    for i in matrix:
        count += 1
        print(i)


    # read matrix column-wise using key
    for _ in range(column):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher


# Decryption
def decryption(cipher):
    message = ""

    # track key indices
    k_indx = 0

    # track msgsage indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

#  incripted
    for row in range(8):
        matrix1 = [msg_lst[row: row + col]]
        count1 = 0
        for k in matrix1:
            count1 += 1
            print(k)

    # convert decrypted message matrix into a string
    try:
        msgsage = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")

    null_count = msgsage.count('*')

    if null_count > 0:
        return msgsage[: -null_count]

    return msgsage


# Driver Code
msg = input('Enter the message: ')

cipher = encryption(msg)
print("Encrypted Message is: {}".format(cipher))

print("Decrypted Message is: {}".format(decryption(cipher)))
