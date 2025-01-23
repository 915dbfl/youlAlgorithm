import java.util.StringTokenizer

data class Rectangle(val x1: Int, val y1: Int, val x2: Int, val y2: Int) {
    fun isCrossed(other: Rectangle): Boolean {
        if (other.x1 > this.x2 || other.x2 < this.x1 || other.y1 > this.y2 || other.y2 < this.y1) {
            return false
        }
        if (this.x1 < other.x1 && other.x2 < this.x2 && this.y1 < other.y1 && other.y2 < this.y2) {
            return false
        }
        if (other.x1 < this.x1 && this.x2 < other.x2 && other.y1 < this.y1 && this.y2 < other.y2) {
            return false
        }
        return true
    }

    val isOriginIncluded: Boolean
        get() = ((x1 == 0 || x2 == 0) && y1 <= 0 && 0 <= y2) || ((y1 == 0 || y2 == 0) && x1 <= 0 && 0 <= x2)
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val rectangles = Array(n) {
        val st = StringTokenizer(readLine())
        Rectangle(
            st.nextToken().toInt(),
            st.nextToken().toInt(),
            st.nextToken().toInt(),
            st.nextToken().toInt()
        )
    }
    var answer = 0

    for (rect in rectangles) {
        if (rect.isOriginIncluded) {
            answer = -1
            break
        }
    }

    val parent = IntArray(n) {it}

    fun find(a: Int): Int {
        if (parent[a] != a) {
            parent[a] = find(parent[a])
        }
        return parent[a]
    }

    fun union(a: Int, b: Int) {
        val pa = find(a)
        val pb = find(b)

        if (pa < pb) {
            parent[pb] = pa
        } else {
            parent[pa] = pb
        }
    }

    for (i in 0 until n-1) {
        for (j in  i+1 until n) {
            if (rectangles[i].isCrossed(rectangles[j])) {
                union(i, j)
            }
        }
    }

    for (i in 0 until n) {
        if (parent[i] == i) {
            answer += 1
        }
    }

    println(answer)
}