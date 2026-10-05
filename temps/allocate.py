import sys
import os

def seperate(file: str) -> tuple:
    file_name, file_extension = file.split(".")
    name_components = file_name.split("_")

    num = 0
    name = name_components[0]
    if len(name_components) > 1:
        num = int(name_components[1])

    return name, num, file_extension


def main(arguments: list[str] = []):
    path = arguments[0] if len(arguments) > 0 else ""
    with open("temps/templates/Main.java", "r") as f:
        template = f.read()
        f.close()
    with open("temps/templates/check.py", "r") as f:
        check = f.read()
        f.close()

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    max_dictionary = dict()

    for file in files:
        name, num, extension = seperate(file)

        if extension not in ["dat", "out"]: continue

        if not name in max_dictionary:
            max_dictionary[name] = num
            continue
        max_dictionary[name] = max(num, max_dictionary[name])


    working_dir = "working"
    for name in max_dictionary.keys():
        num = max_dictionary[name]

        print("-" * 20)
        print(f"Working on problem {name}")

        problem_dir = os.path.join(working_dir, f"problem_{name}")
        os.path.exists(working_dir) or os.makedirs(working_dir)
        os.path.exists(problem_dir) or os.makedirs(problem_dir)

        input_dir = os.path.join(problem_dir, "inputs")
        os.makedirs(input_dir, exist_ok=True)
        output_dir = os.path.join(problem_dir, "outputs")
        os.makedirs(output_dir, exist_ok=True)

        for i in range(num + 1):
            file_name = name if i == 0 else f"{name}_{i}"
            input_file_name = f"{file_name}.dat"
            output_file_name = f"{file_name}.out"

            if os.path.exists(os.path.join(path, input_file_name)):
                with open(os.path.join(path, input_file_name), "r") as f:
                    input_file_content = f.read()
                with open(os.path.join(input_dir, f"input{i+1}.txt"), "w") as f:
                    f.write(input_file_content)
            if os.path.exists(os.path.join(path, output_file_name)):
                with open(os.path.join(path, output_file_name), "r") as f:
                    output_file_content = f.read()
                with open(os.path.join(output_dir, f"output{i+1}.txt"), "w") as f:
                    f.write(output_file_content)


        with open(os.path.join(problem_dir, "Main.java"), "w") as f:
            f.write(template)

        with open(os.path.join(problem_dir, "check.py"), "w") as f:
            f.write(check)


if __name__ == "__main__":
    main(sys.argv[1:])