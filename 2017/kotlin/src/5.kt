import azagroup.test.simpleMeasureTest
import java.io.File
import java.nio.charset.Charset
import kotlin.system.measureNanoTime
import kotlin.system.measureTimeMillis

fun part1(steps: List<Int>): Int {
    val steps = steps.toMutableList()
    var nSteps = 0
    var pos = 0
    while (-1 < pos && pos < steps.size) {
        var offset = steps[pos]
        steps[pos] += 1
        pos += offset
        nSteps += 1
    }
    return nSteps
}

fun part2(steps: List<Int>): Int {
    val steps = steps.toMutableList()
    var nSteps = 0
    var pos = 0
    var offset: Int
    while (-1 < pos && pos < steps.size) {
        offset = steps[pos]
        if (offset > 2) steps[pos] -= 1 else steps[pos] += 1
        pos += offset
        nSteps += 1
    }
    return nSteps
}

fun main(args: Array<String>) {

    val steps = mutableListOf<Int>()
    val txt = File("/Users/phj/GitRepos/advent/2017/data/5.txt").readLines(Charset.defaultCharset())
    txt.mapTo(steps) { it.toInt() }

    /*// println(steps)
    println("pt1 ${part1(steps)}")

    var pt2res = 0
    val ms2 = measureTimeMillis {
        pt2res = part2(steps)
    }
    println("pt2 $pt2res")
    println("part2 time $ms2 ms")*/

    // simpleMeasureTest { part2(steps) }

    simpleMeasureTest(ITERATIONS = 1, TEST_COUNT = 10, WARM_COUNT = 10) { part2(steps) }

}