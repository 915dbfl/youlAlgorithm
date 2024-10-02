fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val circles = Array(n) {
        val (k, x, r) = readLine().split(" ").map { it.toInt() }
        Circle(k, x-r, x+r)
    }

    circles.sort()
    val dq = ArrayDeque<Circle>()
    dq.add(circles[0])
    val parent = Array(n+1) {0}
    for (i in 1..<circles.size){
        val curCircle = circles[i]
        while (dq.isNotEmpty() && dq.last().right < curCircle.left) {
            dq.removeLast()
        }
        if (dq.isNotEmpty()) {
            parent[curCircle.index] = dq.last().index
        }
        dq.add(curCircle)
    }

    var (c1, c2) = readLine().split(" ").map { it.toInt() }
    val c1Parent = ArrayDeque<Int>()
    val c2Parent = ArrayDeque<Int>()

    while(c1 != 0) {
        c1Parent.addLast(c1)
        c1 = parent[c1]
    }
    while(c2 != 0) {
        c2Parent.addLast(c2)
        c2 = parent[c2]
    }

    var firstParent = 0
    while(c1Parent.last() == c2Parent.last()) {
        firstParent = c1Parent.removeLast()
        c2Parent.removeLast()
    }

    println(c1Parent.size + c2Parent.size + 1)
    print(c1Parent.joinToString(" "))
    print(" $firstParent ")
    print(c2Parent.reversed().joinToString(" "))
}

data class Circle(val index: Int, val left: Int, val right: Int): Comparable<Circle> {
    override fun compareTo(other: Circle): Int {
        return this.left - other.left
    }
}