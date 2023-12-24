import Data.List
--import Data.List (nub, sort)
--import Data.List hiding (nub)
import qualified Data.Map
--import qualified Data.Map as M

numUniques :: (Eq a) => [a] -> Integer
numUniques = length . nub

--Maps 1
findKey :: (Eq k) => k -> [(k,v)] -> v
findKey key xs = snd . head . filter (\(k,v) -> key == k) $ xs

--Maps 2
findKey' :: (Eq k) => k -> [(k,v)] -> Maybe v
findKey' key [] = Nothing
findKey' key ((k,v):xs) = if key == k
                            then Just v
                            else findKey key xs

--Maps 3
findKey'' :: (Eq k) => k -> [(k,v)] -> Maybe v
findKey'' key = foldr (\(k,v) acc -> if key == k then Just v else acc) Nothing
