# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Abe Kim
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import *
from random import *

def sum_of_squares(n):
    ''' return the sum of all squares from 1 to n '''
    return sum([i**2 for i in range(n+1)])

# unit testing
def test(f, inputs):
    ''' Runs unit test for f with inputs '''
    return map(lambda x: f(x), inputs)

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output

def split_by_length(s, n=3):
    """
    Split string s into chunks of length n
    """
    res = [s[i:i+n] for i in range(0,len(s),n) if not len(s[i:i+n]) < n]

    return res + [s[len(collapse(res)):]]

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    # if len(dna) is not divisible by 3, instead of raising an exception, only return
    # the amino acid sequence of first 
    if len(dna) % 3:
        dna = dna[:-(len(dna) % 3)]
        # raise Exception("DNA seq not divisible by 3")

    
    acids = ""

    for seg in split_by_length(dna.upper()):
        try:
            acids += aminos[seg]
        except KeyError:
            raise Exception("Key not found in list of amino acids.")

    return acids

def coding_strand_to_AA_unit_tests(inputs):
    """ Unit tests for the coding_strand_to_AA function """
    return test(coding_strand_to_AA, inputs)

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    # dict of gene pairs
    genes = { 'A':'T', 'T':'A', 'C':'G', 'G':'C' }

    if type(dna) == type([]): raise Exception("whoa")
    print "dna", dna
    
    try:
        return collapse([genes[c] for c in dna.upper()[::-1]])
    except KeyError:
        raise Exception("You done fucked up. No such nucleotide exists.")
    
def get_reverse_complement_unit_tests(inputs):
    """ Unit tests for the get_complement function """
    return test(get_reverse_complement, inputs)

def is_stop(seq):
    ''' Returns True if seq is a stop codon '''
    if len(seq) < 3: return False
    return aminos[seq] == '|'

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    start = 'ATG'
    segs = split_by_length(dna.upper())
    
    for i in range(len(segs)):
        if is_stop(segs[i]): return collapse(segs[:i])

    return collapse(segs)

def rest_of_ORF_unit_tests(inputs):
    """ Unit tests for the rest_of_ORF function """
    return test(rest_of_ORF, inputs)

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    start = 'ATG'
    res = []
    i = 0

    while i < len(dna):
        if dna[i:i+3] == start:
            res.append(rest_of_ORF(dna[i:]))
            i += len(res[-1])
        i += 3
    
    return res
     
def find_all_ORFs_oneframe_unit_tests(inputs):
    """ Unit tests for the find_all_ORFs_oneframe function """
    test(find_all_ORFs_oneframe, inputs)

# helpful flatten function
def flatten(li):
    ''' flattens a set of nested lists to a single layer list '''
    if not True in [type(e) == type([]) for e in li]: # check for type of each element
        return li
    
    flattened = []

    for e in li:
        if type(e) == type([]): flattened += flatten(e)
        else: flattened.append(e)

    return flattened

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return flatten([find_all_ORFs_oneframe(dna[i:]) for i in range(3)])

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on bothn
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    return reduce(lambda x, y: x if len(x) > len(y) else y, find_all_ORFs_both_strands(dna))

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    def auxiliary_shuffle(s):
        ''' shuffles a string '''
        a = list(s) # placeholder
        shuffle(a)

        return collapse(a)
    
    a_shuf = auxiliary_shuffle # alias

    return max(flatten([[len(o) for o in longest_ORF(a_shuf(dna))] for _ in range(num_trials)]))

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    sequences = []

    orfs = find_all_ORFs_both_strands(dna)
    print orfs

    for o in orfs:
        print o
        if len(o) >= threshold:
            sequences.append(coding_strand_to_AA(o))

    return sequences

if __name__ == '__main__':
    # print gene_finder('', 1)

    from load import *

    dna = load_seq("./data/X73525.fa")
    salmonella = load_salmonella_genome()

    threshold = longest_ORF_noncoding(dna, 15)

    print gene_finder(salmonella, threshold)

