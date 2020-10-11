from scipy.sparse import *
import numpy as np


def csr_vappend(a, b):

    a.data = np.hstack((a.data, b.data))
    a.indices = np.hstack((a.indices, b.indices))
    a.indptr = np.hstack((a.indptr, (b.indptr + a.nnz)[1:]))
    a._shape = (a.shape[0]+b.shape[0], b.shape[1])

    # print(f"RESHAPE: {a.shape}")  # for test

    return a


def findCurrentNodeCol(currentRow):
    # input CSR_SPARSE
    indices = currentRow.indices
    indptr = currentRow.indptr
    data = currentRow.data

    # for debug
    currentNodesColPos = indices[indptr[0]:indptr[0+1]]
    currentNodesVal = data[indptr[0]:indptr[0+1]]

    for col, value in zip(currentNodesColPos, currentNodesVal):
        if value == 1:

            # print(f"CURRENT NODES at column {col}")  # for debug
            return col


def findConnectEdges(csc_sparse, col):
    # input CSC_SPARSE
    indices = csc_sparse.indices
    indptr = csc_sparse.indptr
    data = csc_sparse.data

    if not data.any():
        # if all 0 in one column
        return []

    currentEdgesRowPos = indices[indptr[col]:indptr[col+1]]
    currentEdgesVal = data[indptr[col]:indptr[col+1]]

    edgeRowIndexList = []
    for row, value in zip(currentEdgesRowPos, currentEdgesVal):

        if value == -1:
            # print(f"EDGE IN row {row}")  # for debug
            edgeRowIndexList.append(row)

    return edgeRowIndexList


def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''

    sets = csc_matrix(sets)

    while sets != []:
        # print("=====CYCLE START=====")

        try:
            currentRowSparse = sets[0].tocsr()
            sets = sets[1:]
        except:
            sets = []
            # print("SETS CLEAR")
            continue
        # for debug
        # print(currentRowSparse)

        currentNodeCol = findCurrentNodeCol(currentRowSparse)
        connectEdgesRowIndexList = findConnectEdges(
            sets, currentNodeCol)

        # for test
        # print(f"ORIGINAL SETS SHAPE: ({original_row_num},{col_num})")

        # print(f"WANT TO RESHAPE TO ({row_num},{col_num})")

        csr_sets = csr_matrix(sets)

        for row_index in connectEdgesRowIndexList:
            edgeRow = csr_sets[row_index]

            newRow = currentRowSparse + edgeRow
            if not newRow.toarray().any():
                # print("======CYCLE END =======")
                return True

            csr_vappend(csr_sets, newRow)

        sets = csr_sets.tocsc()

        # print("=====CYCLE END=====")

    return False
