def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            # This case might be implicitly handled by other checks, but good to have
            return "Error: Problem format incorrect."

        num1_str, operator, num2_str = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1_str.isdigit() or not num2_str.isdigit():
            return "Error: Numbers must only contain digits."

        num1 = int(num1_str)
        num2 = int(num2_str)

        if len(num1_str) > 4 or len(num2_str) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(num1_str), len(num2_str))
        width = max_len + 2  # +2 for the operator and space

        first_num_padded = num1_str.rjust(width)
        second_num_padded = operator + " " + num2_str.rjust(max_len)
        dashes = "-" * width

        if operator == '+':
            answer = str(num1 + num2)
        else:
            answer = str(num1 - num2)
        answer_padded = answer.rjust(width)

        if i < len(problems) - 1:
            first_line += first_num_padded + "    "
            second_line += second_num_padded + "    "
            dashes_line += dashes + "    "
            answers_line += answer_padded + "    "
        else:
            first_line += first_num_padded
            second_line += second_num_padded
            dashes_line += dashes
            answers_line += answer_padded

    if show_answers:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes_line + "\n" + answers_line
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes_line

    return arranged_problems
