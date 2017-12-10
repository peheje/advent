import java.io.File

fun main(args: Array<String>) {
    val lines = File("../data/2.txt").readText()
            .split("\n")
            .map { it.replace("\t", " ") }

    val data = lines.map { it.map { it.toString().toInt() } }
    println(data)
}