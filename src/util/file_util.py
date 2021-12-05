class FileUtil:
    @staticmethod
    def file_to_list(file_name: str) -> list[str]:
        with open(file_name, 'r', encoding='utf-8') as file:
            return [line.rstrip() for line in  file.readlines()]

    @ staticmethod
    def file_to_numbers_and_boards(file_name: str) -> tuple[list[int], list[list[list[int]]]]:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            numbers = list(map(int,lines[0].rstrip().split(',')))
            board_strs =  ''.join(lines[1:]).strip().split('\n\n')
            board_str_to_row = lambda board_str: [list(map(int,row.split())) for row in board_str.split('\n')]
            
            return numbers, list(map(board_str_to_row, board_strs))
