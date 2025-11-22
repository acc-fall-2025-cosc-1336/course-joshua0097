def get_p_distance(list1, list2):
    """
    Calculate the p-distance between two lists of equal length.
    
    The p-distance is the proportion of corresponding elements that differ
    between two sequences.
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        float: The p-distance (proportion of differing elements)
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    
    if len(list1) == 0:
        return 0.0
    
    differences = sum(1 for i in range(len(list1)) if list1[i] != list2[i])
    return differences / len(list1)

def get_p_distance_matrix(list1):
    """
    Calculate the p-distance matrix for a collection of DNA strings.
    
    Args:
        list1: A list of DNA strings (lists/sequences) of equal length
    
    Returns:
        list: A 2D matrix where element [i][j] is the p-distance between
              string i and string j
    """
    if not list1:
        return []
    
    n = len(list1)
    p_distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            p_distance_matrix[i][j] = get_p_distance(list1[i], list1[j])
    
    return p_distance_matrix