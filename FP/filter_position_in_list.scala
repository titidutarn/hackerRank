def f(arr:List[Int]):List[Int] = {
    return arr.zipWithIndex.filter(_._2 %2 == 1).map(_._1)
}