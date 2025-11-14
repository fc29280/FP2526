# Stable Matching Problem
# Author: Pedro Ângelo
# Course: Fundamentos de Programação 2025/26

# Submission for Group:
# Student 1: João Pedro Diogo Rebolho - 64494
# Student 2:Rui Miguel Martins Costa - 29280

### AUXILIARY DEFINITIONS
def no_repetitions(list):
    """
    Check if all elements of a list are unique i.e., there no are repetitions.
    """
    for item in list:
        if list.count(item) != 1:
            return False
    return True

def same_elements(list1, list2):
    """
    Check if list1 and list2 are the same size, and share the same elements.
    """
    # check if lists have equal size
    if len(list1) != len(list2):
        return False
    # check if elements are the same
    for item in list1:
        if list2.count(item) != 1:
            return False
    for item in list2:
        if list1.count(item) != 1:
            return False
    return True
    
# FUNCTIONS A1
def participants_from_prefs(prefs):
    """
    Takes as input preferences `prefs`, and returns the list of participants in order of appearance from the preferences.
    """
    # complete me
    participants = [] # cria uma lista vazia; (listas são mutáveis ex: podemos adicionar elementos)
    for pref in prefs: # percorre cada tuple dentro de cada lista
        participants.append(pref[0]) # usa o append para adicionar à nossa lista criada cada primeiro elemento (ex: nome) de cada tuple de cada lista
    return participants # devolve a lista completa com o primeiro elemento (ex: nome) adicionado de cada tuple de cada lista
                                                             
def verify_prefs(prefs, num_participants):
    """
    Takes as input preferences `prefs`, and number of participants `num_participants` and verifies if `prefs` are well-formed, by verifying the following conditions:
    - the length of `prefs` is equal to `num_participants`;
    - there are no repetitions of strings (representing participants) in the first element of the tuples of `prefs`;
    - the length of the second element of the tuples of `prefs` is equal to `num_participants`;
    - there are no repetitions of strings (representing participants) in the second element of the tuples of `prefs`
    - all lists in the second element of the tuples of `prefs` share the same `num_participants` strings;
    """
    # complete me
    # 1. verificar se o número de tuples é igual ao número de participantes
    if len(prefs) != num_participants: 
        return False # queremos que o número de tuple seja == num_participants
    
    # 2. verificar se não há nomes repetidos no primeiro elemento das tuples
    names = participants_from_prefs(prefs)     # usamos a função criada para obter a lista criada  com o nome dos participantes
    repetitions = no_repetitions(names)         # usamos a função para verifica se há repetições
    if repetitions == False:                    # se houver repetições devolve False
        return False
    
    # 3. verificar se todas as listas de preferências têm o tamanho correto
    for i in range(len(prefs)):                    # percorre cada tuple de uma lista (prefs) 
        list_length = len(prefs[i][1])             # vai a cada tuple de cada lista (prefs) e mede o tamanho da lista dessa tuple
        if list_length != num_participants:        # compara o número dos dois, se não tiver o tamanho esperado, devolve False
            return False                           

    # 4. verificar se não há elementos repetidos dentro de cada lista de preferências
    for i in range(len(prefs)):                        # percorre cada tuple de uma lista (prefs) 
        prefs_list = prefs[i][1]                         # vai a cada tuple e a cada lista desse tuple (lista de preferências)
        list_repetitions = no_repetitions(prefs_list)    # verifica se há elementos repetidos através da função
        if list_repetitions == False:  # se houver repetições é Falso, pois não queremos repeticoes de texto na lista de cada tuple
            return False                    

    # 5. verificar se todas as listas têm exatamente os mesmos elementos (mesmo que em ordem diferente)
    reference = prefs[0][1]                         # cria como referência a lista (preferências) da primeira tuple de uma lista
    for i in range(len(prefs)):                      # vai a cada tuple de uma lista (prefs)
        equal = same_elements(reference, prefs[i][1])  # compara a lista de referência com a lista de cada tuple usando a função para verificar se as duas listas têm os mesmos elementos, mesmo que em ordem diferente
        if equal == False:                          # se não tiverem os mesmos elementos, devolve False
            return False
        
    return True                             

def compatible_prefs(prefs1, prefs2):
    """
    Takes as input preferences `prefs1` and `prefs2` and check if both are compatible, by verifying the following conditions:
    - strings (representing participants) in the first element of the tuples of `prefs1` share the strings (representing preferences) in the second element of the tuples of `prefs2`, and vice-versa.
    """
    # complete me
    # obter as listas de participantes de cada conjunto de preferências
    participants1 = participants_from_prefs(prefs1) 
    participants2 = participants_from_prefs(prefs2)

    # verificar se todos os participantes de prefs1 aparecem nas preferências de prefs2
    for i in range(len(prefs2)): # percorre cada tuple de uma lista (prefs2)
        same = same_elements(participants1, prefs2[i][1]) # acede à lista (preferências) de cada tuple da lista (prefs2) e a função compara a lista com os nomes do outro grupo (participants1)
        if same == False: # se não forem iguais, as preferências não são compatíveis
            return False
    
    # verificar se todos os participantes de prefs2 aparecem nas preferências de prefs1
    for i in range(len(prefs1)): # percorre cada tuple de uma lista (prefs1)
        same = same_elements(participants2, prefs1[i][1]) # acede à lista (preferências) de cada tuple da lista (prefs1) e a função compara a lista com os nomes do outro grupo (participants2)
        if same == False: # se não forem iguais, as preferências não são compatíveis
            return False
    
    return True
# FUNCTIONS A2
def preferences_by_position(prefs, index):
    """
    Takes as input preferences `prefs`, and returns the list of preferences in position `index` for all participants.
    """
    # complete me
    result = []
    for pair in prefs:                  #  pair corresponde a um tuplo: (nome_participante, [lista de preferências])
        result.append(pair[1][index])   # 'index' - corresponde à posição da preferência na lista de preferências
    return result                                                                                                                     

def input_prefs(num_participants):
    """
    Takes as input the number of participants `num_participants`, stores preferences obtained from the standard input, and returns those preferences.
    """
    # complete me
    
    prefs = [] # Lista para armazenar as preferências de todos os participantes
    
    # Iteração sobre os participantes para recolher os seus dados
       
    for i in range(num_participants):
        name = input("Enter name of participant " + str(i + 1) + ": ") # Solicita o nome do participante atual (i+1 porque o índice começa em 0)
        print("Enter preferences in order (one per line):") #corrigido o output gerado, existia omissão de parte da linha, foi apontado pelo Professor
        preferences = [] # Lista para armazenar as preferências do participante
        
        # Recolhe preferências para os participantes
        for j in range(num_participants):
            pref = input() # Lê cada preferência individualmente e adiciona-a à lista de preferências deste participante
            preferences.append(pref)
        prefs.append((name, preferences)) # Armazena o par (tuplo) (nome, preferências) na lista principal
    
    return prefs # Retorna a lista completa


def show_prefs(prefs):
    """
    Takes as input preferences `prefs`, and prints the participants along with their list of preferences.
    """
    # complete me

    # Itera sobre os conjuntos de preferências dos participantes na lista
    for participant_prefs in prefs:
        participant_name = participant_prefs[0] # Extrai o nome do participante
        preferences_list = participant_prefs[1] # Extrai a lista de preferências do participante

        # Constrói a string de output concatenando, nome do participante, ":", separador de preferências " >" e junta a lista de preferências
        output = participant_name + ": " + " > ".join(preferences_list)
                                                                                                                                                                                                              

        print(output) # gera uma saída para a variável output


# FUNCTIONS A3

def most_chosen(prefs, participants_list):
    """
    Takes as input preferences `prefs` and a list of participants `participants_list` consisting of the participants used as preferences in `prefs` and returns the participant (or participants) who was chosen the most times as the first preference.
    """
    # complete me
    occurrences = [] # Inicializa a lista de ocorrências (um contador para cada participante)
    for participant in participants_list:
        occurrences.append(0)
    
    first_preferences = preferences_by_position(prefs, 0) # Participantes escolhidos na posição 0 (primeira preferência de cada um)
    
    # Conta as ocorrências de cada participante nas primeiras preferências
    for first_pref in first_preferences:
        # Encontra qual participante e incrementa o seu contador
        for i in range(len(participants_list)):
            if participants_list[i] == first_pref:
                occurrences[i] += 1
    
    # Obtém o número máximo de ocorrências, inicio a 0 até encontrar o maior valor
    max_occurrences = 0
    for count in occurrences:
        if count > max_occurrences:
            max_occurrences = count
    
    chosen = [] # Cria uma lista com todos que foram escolhidos o maior número de vezes
    for i in range(len(participants_list)):
        if occurrences[i] == max_occurrences:
            chosen.append(participants_list[i])
    
    return chosen
    
# FUNCTIONS B

def prefs_to_dict(prefs):
    """
    Takes as input preferences `prefs` and returns a dictionary of `prefs'.
    """
    #opção com funções built-in. Uso directo da função dict(), corresponde ao hint que o professor colocou no enunciado, esta função torna a aplicação mais practica e limpa.
    
    return dict(prefs)

    # complete me
    """
    Opção inicialmente construida, mas o uso da função dict() permite um código mais limpo e sem necessidade de linhas de código extras.
    dict_prefs = {} # cria um dicionário vazio
    for pair in prefs: # percorre cada tuple dentro de cada lista
        dict_prefs[pair[0]] = pair[1] # atribui ao dicionário o primeiro elemento do tuplo como chave e o segundo elemento como valor
    return dict_prefs # devolve o dicionário completo
    """


def permutations(list, perms=[]):
    """
    Takes as input a list `list`, and an optional list of permutations `perms`, and calculates the permutations of `list`, adding `perms` to the top.
    """
    # complete me

    # if list is empty , return list of perms
    if len(list) == 0:
        return [perms]
    
    # initialise empty list of all permutations
    all_perms = []
    
    # for each element in the list
    for i in range(len(list)):
        # obtain the remaining elements of the list
        current = list[i]
        
        # recursively call permutations , with the remaining elements , and the new permutations formed by adding the chosen element of the list
        # lista[:i] = elementos antes de i
        # lista[i+1:] = elementos depois de i
        remaining = list[:i] + list[i+1:]
        
        # Cria novas permutações adicionando o elemento atual às perms existentes
        new_perms = perms + [current]
        
        # Recursão para obter permutações dos elementos restantes
        sub_perms = permutations(remaining, new_perms)
        
        # add all new permutation in a list of permutations
        all_perms = all_perms + sub_perms #evitar alterar a lista enquanto se itera sobre ela (all_perms += sub_perms)
    
    return all_perms


def generate_all_matchings(proposers, acceptors):
    """
    Takes as input a list of proposers `proposers` and a list of acceptors `acceptors` and returns a list of all possible one-to-one matchings between proposers and acceptors.
    """
    # complete me

    # Obtém todas as permutações dos acceptors
    # Reutiliza a função permutations criada anteriormente
    acceptor_perms = permutations(acceptors)
    
    # Inicializa lista para guardar todos os matchings
    all_matchings = []
    
    # Para cada permutação de acceptors
    for perm in acceptor_perms:
        # Cria um matching emparelhando cada proposer com o acceptor correspondente
        matching = []
        for i in range(len(proposers)):
            # Cria par (proposer, acceptor)
            pair = (proposers[i], perm[i])
            matching.append(pair)

        # Adiciona o matching à lista
        all_matchings.append(matching)
    
    return all_matchings

def is_matching_stable(proposers_dict, acceptors_dict, matching):
    """
    Takes as input proposer's preferences dictionary `proposers_dict`, acceptor's preferences dictionary `acceptors_dict` and matching `matching`, and returns `true` if `matching` is stable, or `false` otherwise.
    """
    # complete me

    #Criar dicionários para saber quem está emparelhado com quem
    proposer_matches = {}  # Dicionário: proposer → acceptor
    acceptor_matches = {}  # Dicionário: acceptor → proposer

    # Preencher os dicionários com o emparelhamento atual
    for proposer, acceptor in matching:
        proposer_matches[proposer] = acceptor
        acceptor_matches[acceptor] = proposer
    
    #Verificação de cada proposer
    for proposer, acceptor in matching:
        # Obter resultados de emparelhamento de acceptor com proposer 
        current_acceptor = proposer_matches[proposer]
        
        # Obter a lista de preferências do proposer
        proposer_prefs = proposers_dict[proposer]
        
        # Encontrar a posição do emparelhamento atual na lista
        current_position = proposer_prefs.index(current_acceptor)
        
        # Verificar todos os acceptors que o proponente prefere mais
        # (todos os que estão antes na lista de preferências)
        for i in range(current_position):
            preferred_acceptor = proposer_prefs[i]
            
            # Descobrir com quem este acceptor preferido está emparelhado
            current_proposer_of_acceptor = acceptor_matches[preferred_acceptor]
            
            # Obter as preferências deste acceptor
            acceptor_prefs = acceptors_dict[preferred_acceptor]
            
            # Encontrar posições na lista de preferências do acceptor
            position_of_current = acceptor_prefs.index(current_proposer_of_acceptor)
            position_of_proposer = acceptor_prefs.index(proposer)
            
            # Verificar se o acceptor também prefere este proposer
            # Se a posição do proposer < posição do atual → prefere o proposer
            if position_of_proposer < position_of_current:
                # Ambos se preferem mas não estão juntos - emparelhamento instável
                return False
    
    # nenhum par instável foi encontrado
    return True

def calculate_likeability_match(proposers_dict, acceptors_dict, match):
    """
    Takes as input proposer's preferences dictionary `proposers_dict`, acceptor's preferences dictionary `acceptors_dict` and a match `match`, of the form (proposer, acceptor), and returns the likeability score of that match.
    """
    # complete me

def calculate_likeability_matching(proposers_dict, acceptors_dict, matchings):
    """
    Takes as input proposer's preferences dictionary `proposers_dict`, acceptor's preferences dictionary `acceptors_dict` and matchings `matchings`, and returns the global likeability score of the matching.
    """
    # complete me

def calculate_best_matching(proposers_dict, acceptors_dict):
    """
    Takes as input proposer's preferences dictionary `proposers_dict` and acceptor's preferences dictionary `acceptors_dict`, and calculates and returns the stable matchings that have better (lower) global likeability score.
    """
    # complete me

def most_desirable(prefs, participants_list):
    """
    Takes as input preferences `prefs` and a list of participants `participants_list` consisting of the participants used as preferences in `prefs` and returns the participant (or participants) who is considered the most desirable across all choice positions i.e., ties are resolved by searching on the next position of preferences.
    """
    # complete me
