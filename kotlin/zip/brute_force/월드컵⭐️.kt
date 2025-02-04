import java.util.*

private class Solution6987 {
    private lateinit var countries: Array<Country>
    private val games = listOf(
        Pair(0, 1), Pair(0, 2), Pair(0, 3), Pair(0, 4), Pair(0, 5),
        Pair(1, 2), Pair(1, 3), Pair(1, 4), Pair(1, 5),
        Pair(2, 3), Pair(2, 4), Pair(2, 5),
        Pair(3, 4), Pair(3, 5), Pair(4, 5)
    )
    var isPossible = false

    fun play(matchIndex: Int) {
        if (matchIndex == games.size) {
            isPossible = true
            return
        }

        val (t1, t2) = games[matchIndex]

        // Kotlin's let and also destructuring declaration
        countries[t1].let { team1 ->
            countries[t2].let { team2 ->
                //  Simplified conditional checks
                if (team1.draw > 0 && team2.draw > 0) {
                    team1.draw--
                    team2.draw--
                    play(matchIndex + 1)
                    team1.draw++
                    team2.draw++
                }
                if (team1.win > 0 && team2.lose > 0) {
                    team1.win--
                    team2.lose--
                    play(matchIndex + 1)
                    team1.win++
                    team2.lose++
                }
                if (team1.lose > 0 && team2.win > 0) {
                    team1.lose--
                    team2.win--
                    play(matchIndex + 1)
                    team1.lose++
                    team2.win++
                }
            }
        }
    }

    fun init(countries: Array<Country>) {
        this.countries = countries
        isPossible = false
    }
}

data class Country(var win: Int, var draw: Int, var lose: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val sb = StringBuilder()
    val solution = Solution6987()

    repeat(4) {
        val st = StringTokenizer(readLine())
        var totalGames = 0

        val countries = Array(6) {
            val win = st.nextToken().toInt()
            val draw = st.nextToken().toInt()
            val lose = st.nextToken().toInt()
            totalGames += win + draw + lose
            Country(win, draw, lose)
        }

        solution.init(countries)

        if (totalGames == 30) {
            solution.play(0)
        }

        sb.append(if (solution.isPossible) "1 " else "0 ")
    }
    println(sb)
}