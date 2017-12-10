import System.IO  
import Control.Monad
import Data.List.Split

main = do  
    contents <- readFile "../data/2.txt"
    let list = map readInt (words contents)
    let split = chunksOf 16 list
    sum [big - small | (big, small) <- [row | row <- split]]
    s = sum [big - small | (big, small) <- split]
    print split

readInt :: String -> Int
readInt = read