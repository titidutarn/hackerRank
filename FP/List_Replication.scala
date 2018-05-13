 def f(num:Int,arr:List[Int]):List[Int] =
    return arr.flatMap(List.fill(num)(_))