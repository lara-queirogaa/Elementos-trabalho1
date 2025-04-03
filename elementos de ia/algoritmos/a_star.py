import sys
import os
import copy
import time
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from movimentos import *
from check_win import *
from heurística import *

def a_star_solution(initial_board, level, max_iterations=10000):
    """
    Implementação do algoritmo A* para resolver o Sport Sort.
    
    Retorna:
    - solution_path: lista de movimentos ou None
    - time_dict: dicionário com tempo de execução
    - move_count: número de movimentos na solução
    """
    start_time = time.perf_counter()
    
    def board_to_tuple(board):
        return tuple(tuple(row) for row in board)
    
    # Fila de prioridade: (f_score, g_score, board, path)
    heap = []
    
    # Estado inicial
    initial_heuristic = calculate_grouped_balls_heuristic(initial_board)
    heapq.heappush(heap, (initial_heuristic, 0, copy.deepcopy(initial_board), []))
    
    visited = {}
    visited[board_to_tuple(initial_board)] = 0  # Armazena o melhor g_score para cada estado
    
    iterations = 0
    
    while heap and iterations < max_iterations:
        current_f, current_g, current_board, path = heapq.heappop(heap)
        iterations += 1
        
        if check_win(current_board, level):
            elapsed = time.perf_counter() - start_time
            time_dict = {
                'minutes': int(elapsed // 60),
                'seconds': int(elapsed % 60),
                'milliseconds': int((elapsed % 1) * 1000)
            }
            return path, time_dict, len(path)
        
        all_possible = total_possible_moves(current_board, level)
        
        for move_info in all_possible:
            from_shelf, ball, to_shelves = move_info
            for to_shelf in to_shelves:
                new_board = copy.deepcopy(current_board)
                success = move_piece(new_board, from_shelf, to_shelf)
                
                if success:
                    new_state = board_to_tuple(new_board)
                    new_g = current_g + 1  # Custo de cada movimento é 1
                    
                    # Só processa se for um caminho melhor (g_score menor) ou estado novo
                    if new_state not in visited or new_g < visited[new_state]:
                        visited[new_state] = new_g
                        new_path = path + [(from_shelf, to_shelf)]
                        new_h = calculate_grouped_balls_heuristic(new_board)
                        new_f = new_g + new_h
                        heapq.heappush(heap, (new_f, new_g, new_board, new_path))
    
    # Caso não encontre solução dentro do limite de iterações
    elapsed = time.perf_counter() - start_time
    time_dict = {
        'minutes': int(elapsed // 60),
        'seconds': int(elapsed % 60),
        'milliseconds': int((elapsed % 1) * 1000)
    }
    return None, time_dict, 0

# Exemplo de uso
if __name__ == "__main__":
    print(a_star_solution(
        [[2, 4, 1, 4], 
         [3, 4, 1, 2], 
         [2, 3, 1, 1], 
         [3, 3, 2, 4], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]], 
        level=1))
