import java.util.StringTokenizer

private class Solution6987 {
    private lateinit var countries: Array<Country>
    var isPossible = false
    private val turns = arrayOf(
        0 to 1, 0 to 2, 0 to 3, 0 to 4, 0 to 5,
        1 to 2, 1 to 3, 1 to 4, 1 to 5,
        2 to 3, 2 to 4, 2 to 5,
        3 to 4, 3 to 5,
        4 to 5,
    )
    fun play(match: Int) {
        if (match == 15) {
            isPossible = true
            return
        }

        val (c1, c2) = turns[match]
        if (countries[c1].win > 0 && countries[c2].lose > 0) {
            countries[c1].win--
            countries[c2].lose--
            play(match+1)
            countries[c1].win++
            countries[c2].lose++
        }
        if (countries[c1].draw > 0 && countries[c2].draw > 0) {
            countries[c1].draw--
            countries[c2].draw--
            play(match+1)
            countries[c1].draw++
            countries[c2].draw++
        }
        if (countries[c1].lose > 0 && countries[c2].win > 0) {
            countries[c1].lose--
            countries[c2].win--
            play(match+1)
            countries[c1].lose++
            countries[c2].win++
        }
    }

    fun init(
        countries: Array<Country>
    ) {
        this.countries = countries
        isPossible = false
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val testCount = 4
    val result = StringBuilder()
    val solution = Solution6987()

    var countries: Array<Country>
    var st: StringTokenizer
    var win: Int
    var draw: Int
    var lose: Int
    var totalPlay: Int

    repeat(testCount) {
        st = StringTokenizer(readLine())
        totalPlay = 0
        countries = Array(6) {
            win = st.nextToken().toInt()
            draw = st.nextToken().toInt()
            lose = st.nextToken().toInt()
            totalPlay += win + draw + lose
            Country(win, draw, lose)
        }

        solution.init(countries)
        if (totalPlay == 30) {
            solution.play(0)   
        }
        result.append(if (solution.isPossible) "1 " else "0 ")
    }

    print(result)
}

data class Country(
    var win: Int,
    var draw: Int,
    var lose: Int
)