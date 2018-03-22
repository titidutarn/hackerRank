import java.io.PrintWriter

object Solution {
    
    def main(args: Array[String]) {
        val scan = scala.io.StdIn
        val fw = new PrintWriter(sys.env("OUTPUT_PATH"))
        val n = scan.readLine.trim.toInt
        val A = scan.readLine.split(" ").map(_.trim.toInt)
        val result = uniqueRecycledPairs(A)
        fw.println(result)
        fw.close()
    }
    
    // grouping the set by size of the string inputed
    // filtering sole groups and apply count_per_group1 on each groups then reduce
    def uniqueRecycledPairs(A: Array[Int]): Int = {
        val groups_by_size : Map[Int, List[String]] = A.map(_.toString).toList.distinct.groupBy(_.size).filter(_._1>1)
        val res1 : Int = groups_by_size.foldLeft(0)((acc, x) => acc + count_per_group1(x._2))
        return res1
    }
    
    // grouping the string (already same size) if they contain same char 
    // filtering sole groups and apply count_per_group2 on each groups then reduce
    def count_per_group1(group: List[String]): Int = {
        val group_by_char : Map[List[Char],List[List[Char]]]=group.map(_.toList).groupBy(_.sorted).filter(_._2.size>1)
        val res2 : Int=group_by_char.values.foldLeft(0)((acc, x) => acc + count_per_group2(x))
        return res2
    }
    
    // calculating number of uniqueRecycledPairs in groups of same number of char and same char
    def count_per_group2(group: List[List[Char]]): Int = {
        
        var all_same_char_in_group : Boolean = group(0).distinct.size == group(0).size
        
        // if all the char are different in this group, it's not greedy
        if (all_same_char_in_group){ return cheap_count(group) }
            
        // else it's rude
        else { return greedy_count(group) }
    }

    // In this List[List[Char]], if all Char are different, 
    // we place ourself on the index of one random value for all groups
    // and count rotatedView that are same 
    // if n is the number given by the groupby : the number of pairs is sum(range(n))
    def cheap_count(X: List[List[Char]]): Int ={
        val lists_and_index : List[(Int, List[Char])]= X.map(x=>(x.indexOf(X(0)(0)),x))
        val res3 : Int = lists_and_index.map(x => rotatedView(x._2,x._1))
                                 .groupBy(x=>x).mapValues(_.size).values
                                 .foldLeft(0)( (acc, a) => if (a>0) acc + a*(a-1)/2 else acc)
        return res3
    }
    
    // else we try all combinaisons 
    def greedy_count(X: List[List[Char]]): Int = {
        val group_size=X.size
        val nb_chars=X(0).size
        var count = 0
        for (i <- 0 to group_size-1){
            var a = X(i)
            var lists_a : List[List[Char]] = List()
            for (k <- 0 to nb_chars-1){
                lists_a = lists_a :+ rotatedView(a,k)
            }
            for (j<- i+1 to group_size-1){
                var b = X(j)
                if (lists_a.contains(b)) {count+=1}
            }
        }
        return count
    }
    
    // i-shift of a list with last terms comming front
    def rotatedView(list : List[Char],i:Int) = { list.drop(i)++list.take(i) }
    
}
