# -*- coding: utf-8 -*-

"""
Test module for experiences assignment

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january
"""

from ast import If
import imp
import sys
import experience
import marker
from functools import cmp_to_key

from sorting import merge_sort

def compare (m1,m2):
    '''
    Compares two markers

    Args:
      m1 (Marker): A marker 
      m2 (Marker): Another marker
    
    Returns:
      int: -1 if `m1 < m2`, 0 if `m1 = m2` or 1 when `m1 > m2`
    '''
    global cpt 
    cpt+=1
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    Args:
      markers (list of str): The list of markers 
      positive (list of str): The list of positive markers

    Returns:
      list of str: The list of negative markers
    """
    negative = []
    for m in markers:
        k=0
        while k<len(positive) and compare(m,positive[k]) !=0:
            k+=1
        if k == len(positive):
            negative.append(m)

    return negative

def recherche_dichotomique( element, liste_triee ):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        comp = compare(liste_triee[m],element)
        if comp == 0 :
            return m
        elif comp == 1 :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

# STRATEGY 2
def negative_markers2(markers,positive):
    negative = []
    
     
 # Trier `positive` grâce au module sorting, qui vous est fourni (pensez à l'importer)
    if len(positive) !=0 :
        positive = merge_sort(positive,compare)
        for i in range(len(markers)):
            index= recherche_dichotomique(markers[i],positive)
            if compare(markers[i],positive[index])!=0:
                negative.append(markers[i])
    else:
        negative=[m for m in markers]
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    negative = []
    positivesorted=merge_sort(positive,compare)
    markerssorted=merge_sort(markers,compare)
    i=0
    j=0
    while j<len(positivesorted):


        if compare(markerssorted[i],positivesorted[j])==0:

            j+=1
            i+=1
        else:
            negative.append(markerssorted[i])
            i+=1
    if len(markerssorted)!=0:
        for k in range(i,len(markerssorted)):
            negative.append(markerssorted[k])

    return negative
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <p> <m>\n\n<p>: nombre de marqueurs positifs\n<m>: nombre de marqueurs".format(sys.argv[0]))
        sys.exit(1)
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    assert (m > 0), "The number of markers must be greater than 0"
    assert (p <= m), "The number of positive markers must be less or equal to the number of markers"

    """"
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()
    print("Markers: {}".format(markers))
    print("Positive markers: {}".format(positive))
    
    # test stategy 1
    cpt = 0                 # D'après vous à quoi peut servir cette variable ? …
    print("Negative markers: {}".format(negative_markers1(markers,positive)))
    print("Nb. comparisons : {}".format(cpt))

    # test stategy 2
    cpt = 0
    print("Negative markers: {}".format(negative_markers2(markers,positive)))
    print("Nb. comparisons pour stratégie 2: {}".format(cpt))

    # test stategy 3
    cpt = 0
    print("Negative markers: {}".format(negative_markers3(markers,positive)))
    print("Nb. comparisons pour stratégie 3: {}".format(cpt))
    """
for i in range(m):
        cpt=0
        p=i+1
        exp = experience.Experience(p,m)
        markers = exp.get_markers()
        positive = exp.get_positive_markers()
        line= str(p) + " " + str(m) + " {:d} {:d} {:d}"
        negative_markers1(markers,positive)
        cpt1 = cpt
        cpt = 0

        negative_markers2(markers,positive)
        cpt2 = cpt
        cpt = 0

        negative_markers3(markers,positive)
        cpt3 = cpt

        print(line.format(cpt1,cpt2,cpt3))
