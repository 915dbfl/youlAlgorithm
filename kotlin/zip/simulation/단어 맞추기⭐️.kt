/*
1. 오른쪽에 있는 문자들 중 더 큰 값이 있는 특정 값을 찾는다. ⭐️
2. 오른쪽에 있는 더 큰 문자 중, 가장 작은 문자와 swap한다.
3. 해당 문자 오른쪽에 존재하는 문자들을 정렬한다.
*/

fun main() = with(System.`in`.bufferedReader()) {
    val t = readLine().toInt()

    repeat(t) {
        val input = readLine().toCharArray()
        for(i in input.size - 2 downTo 0) {
            // 오른쪽에 더 큰 값이 있는 특정 값 찾기 
            var target = -1
            for (j in i until input.size) {
                if (input[i] < input[j]) {
                    if (target == -1 || input[target] > input[j]) {
                        target = j
                    }
                }
            }

            if(target != -1) {
                // swap 진행하기
                val tmp = input[i]
                input[i] = input[target]
                input[target] = tmp
                // 특정 값 오른쪽 값 정렬
                input.sort(i+1, input.size)
                break
            }
        }

        println(input.joinToString(""))
    }
}