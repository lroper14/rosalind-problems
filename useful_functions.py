# Function to open and convert file to list of sequences
def get_seq_list(filename):
    # String to add the sequence lines onto the string which will be stored in a list
    current_sequence = ''
    seq_list = [] # List of sequences from the file

    # Opens the sequence file
    sequence = open(filename, 'r')

    # Remove the \n's and add to list
    for line in sequence.readlines():
        line = line.strip()
        if line.startswith('>'):
            if current_sequence != '':
                seq_list.append(current_sequence)
                current_sequence = ''
        else:
            current_sequence += line
    return seq_list

