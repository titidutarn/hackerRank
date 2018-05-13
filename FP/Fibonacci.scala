object Solution {
    
     def fibonacci(n:Int):Int = {
         if (n <= 1) n
         else (1 to n-1).foldLeft((0, 1)) {case ((a,b), i) => (b, a+b)}._1
     }

    def main(args: Array[String]) {
         println(fibonacci(readInt()))
    }
}