# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import *

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
    return [s[i:i+n] for i in range(0,len(s),n) if not len(s[i:i+n]) < n]

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    if len(dna) % 3:
        raise Exception("You done fucked up. DNA seq not divisible by 3")
    
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
    
    return ''.join([genes[i] for i in dna.upper()[::-1]])
    
def get_reverse_complement_unit_tests(inputs):
    """ Unit tests for the get_complement function """
    return test(get_reverse_complement, inputs)

def has_codon(seq):
    '''
    Checks if a DNA sequence corresponds to an existing codon
    '''
    return seq in aminos.keys()

def is_stop(seq):
    ''' Returns True if seq is a stop codon '''
    return aminos[seq] == '|'

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    filtered = filter(lambda x: has_codon(x), split_by_length(dna.upper()))
    
    for i in range(len(filtered)):
        if is_stop(filtered[i]): return ''.join(filtered[:i])

    return ''.join(filtered)


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
    
    # YOUR IMPLEMENTATION HERE
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE