// 40분

val br = System.`in`.bufferedReader()
lateinit var parent: Array<Int>
lateinit var road: ArrayList<IntArray>

fun find(target: Int): Int {
    if (parent[target] == target) return target
    else {
        parent[target] = find(parent[target])
        return parent[target]
    }
}

fun union(h1: Int, h2: Int) {
    val p1 = find(h1)
    val p2 = find(h2)

    if (p1 < p2) {
        parent[p2] = p1
    } else {
        parent[p1] = p2
    }
}

fun main() = with(System.out.bufferedWriter()) {

    while (true) {
        val (m, n) = br.readLine().split(" ").map {it.toInt()}
        if (m == 0 && n == 0) break
        
        road = ArrayList<IntArray>()
        parent = Array(m){it}

        var total = 0
        repeat(n) {
            val arr = br.readLine().split(" ").map {it.toInt()}.toIntArray()
            road.add(arr)
            total += arr[2]
        }

        road.sortBy {it[2]}
        var minTotal = 0
        // 최소신장트리 활용
        for (r in road) {
            if (find(r[0]) != find(r[1])) {
                minTotal += r[2]
                union(r[0], r[1])
            }
        }
        write("${total - minTotal}\n")
    }

    close()
}