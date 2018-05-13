object Solution {

    def fact(num: Int): Int = return (1 to num).foldLeft(1)((a,b) => (a * b))

    def e(x:Double, prec:Int):Double=return (0 to prec-1).map(y => scala.math.pow(x,y)/fact(y)).sum
    
    def main(args: Array[String]) {
        val stdin = scala.io.StdIn
        val n = stdin.readLine.trim.toInt
        for (nItr <- 1 to n) {
            val x = stdin.readLine.trim.toDouble
            println(e(x,10))
        }
    }
}
