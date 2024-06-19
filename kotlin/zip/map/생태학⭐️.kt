// TreeMap
// O(logN + logN) -> 삽입 + 검색
import java.util.*
val br = System.`in`.bufferedReader()
fun main() = with(System.out.bufferedWriter()) {
    val map = TreeMap<String, Double>()
    var size = 0
    while(true) {
        val input = br.readLine() ?: break
        map[input] = map.getOrDefault(input, 0.0) + 1
        size++
    }

    map.forEach{
        write("${it.key} ${String.format("%.4f", it.value/size*100)}\n")
    }
    flush()
    close()
}

// trie + treeSet
// trie 
// 길이 L / 문자열의 수 M -> O(L*M)
import java.util.*

val br = System.`in`.bufferedReader()

class Trie(var cnt: Int, val node: MutableMap<Char, Trie>) {
    fun insert(word: String) {
        var child: Trie = this

        for(ch in word) {
            if (child.node.containsKey(ch)) {
                child = child.node[ch]
            }
            else {
                child.node[ch] = Trie(0, mutableMapOf())
                child = child.node[ch]
            }
        }
        // 단어 끝에 카운팅
        child.cnt++
    }

    fun getCount(word: String): Int {
        var child = this
        for(ch in word) {
            child = child.node[ch]!!
        }
        return child.cnt
    }
}

fun main() = with(System.out.bufferedWriter()) {
    val root = Trie(0, mutableMapOf())
    val treeSet = TreeSet<String>()
    var size = 0

    while(true) {
        val input = br.readLine() ?: break
        root.inset(input)
        treeSet.add(input)
        size++
    }

    for(set in treeSet) {
        write("$set ${String.format("%.4f", root.getCount(set).toDouble/size*100)}\n")
    }

    close()
}