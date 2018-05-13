def f(arr:List[Int]):List[Int] =
    return arr.foldLeft(List[Int]())((acc,v) => v::acc)