// 오답

import kotlin.math.*

private class Tree {
    var oddNode: Int = 0
    var evenNode: Int = 0
    var reverseOddNode: Int = 0
    var reverseEvenNode: Int = 0
    
    fun isTree(): Boolean {
        return (oddNode == 1 && evenNode == 0) || (oddNode == 0 && evenNode == 1)
    }
    
    fun isReverseTree(): Boolean {
        return (reverseOddNode == 1 && reverseEvenNode == 0) || (reverseOddNode == 0 && reverseEvenNode == 1)
    }
}

class Solution {
    private lateinit var parents: IntArray
    private lateinit var inDegree: IntArray
    
    private fun find(num: Int): Int {
        if (parents[num] != num) {
            parents[num] = find(parents[num])
        }
        return parents[num]
    }
    
    private fun merge(a: Int, b: Int) {
        val pa = find(a)
        val pb = find(b)
        
        if (a != b) {
            if (a < b) {
                parents[b] = a
            } else {
                parents[a] = b
            }
        }
    }
    
    fun solution(nodes: IntArray, edges: Array<IntArray>): IntArray {
        var lastNode = 0
        for (node in nodes) {
            lastNode = max(lastNode, node)
        }
        
        inDegree = IntArray(lastNode + 1)
        parents = IntArray(lastNode + 1) {it}
        
        // union - find 구하기
        for ((start, end) in edges) {
            inDegree[start]++
            inDegree[end]++
            merge(start, end)
        }
        
        var hashMap = HashMap<Int, Tree>()
        // 루트가 정해지지 않았을 때 상태 구하기
        for (node in nodes) {
            val parent = find(node)
            val tree = hashMap.getOrDefault(parent, Tree())
            
            if ((node % 2 == 0) && (inDegree[node] % 2 == 0)) {
                tree.evenNode++
            } else if ((node % 2 == 0) && (inDegree[node] % 2 == 1)) {
                tree.reverseEvenNode++
            } else if ((node % 2 == 1) && (inDegree[node] % 2 == 1)) {
                tree.oddNode++
            } else if ((node % 2 == 1) && (inDegree[node] % 2 == 0)) {
                tree.reverseOddNode++
            }
            
            hashMap.put(parent, tree)
        }
        
        var treeCnt = 0
        var reverseTreeCnt = 0
        for (tree in hashMap.values) {
            if (tree.isTree()) {
                treeCnt++
            }
            if (tree.isReverseTree()) {
                reverseTreeCnt++
            }
        }
        
        return intArrayOf(treeCnt, reverseTreeCnt)
    }
}