class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_population = {}

        for birth, death in logs:
            year_population[birth] = year_population.get(birth, 0) + 1
            year_population[death] = year_population.get(death, 0) - 1
        
        max_population, curr_population = 0, 0
        earliest_year = 0

        for year in sorted(year_population.keys()):
            curr_population += year_population[year]

            if curr_population > max_population:
                max_population = curr_population
                earliest_year = year
                
        return earliest_year