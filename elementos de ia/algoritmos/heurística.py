def calculate_grouped_balls_heuristic(board):
    """
    Heurística que conta o número total de bolas do mesmo tipo que estão adjacentes.
    Quanto maior o valor, melhor o estado do tabuleiro.
    """
    grouped_balls = 0
    
    for shelf in board:
        if sum(shelf) == 0:  # Prateleira vazia
            continue
        
        current_ball = None
        current_count = 0
        
        for ball in shelf:
            if ball == 0:  # Ignorar espaços vazios
                continue
                
            if ball == current_ball:
                current_count += 1
            else:
                if current_count > 1:
                    grouped_balls += current_count
                current_ball = ball
                current_count = 1
        
        # Adicionar o último grupo da prateleira
        if current_count > 1:
            grouped_balls += current_count
    
    return grouped_balls
