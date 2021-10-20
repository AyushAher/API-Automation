import os


class Model:
    def __init__(self, path, model, columns, project):
        self.project = project
        self.path = path
        self.model = model
        self.columns = columns
        self.Create(self.model)

    def Create(self, model):

        if os.path.exists(f"{self.path}/{self.project}/Models"):
            open(f"{self.path}/{self.project}/Models/{model}.cs", "w")

        else:
            os.mkdir(f"{self.path}/{self.project}/Models")
            open(f"{self.path}/{self.project}/Models/{model}.cs", "w")

        self.Write()

    def Write(self):
        self.DataType()
        modelFileData = [
            "using System;\n",
            "using System.Collections.Generic;\n\n",
            f"namespace {self.project}.Models\n",
            "{\n\t",
            f"public partial class {self.model}\n",
            "\t{\n"]
        for x in self.columns:
            feild = f"\t\t public {x[1]} {str(x[0]).title()}" + " { get; set; }\n"
            modelFileData.append(feild)

        modelFileData.append("\t}\n}")

        modelFile = open(f"{self.path}/{self.project}/Models/{self.model}.cs", "w")
        modelFile.writelines(modelFileData)
        modelFile.close()

    def DataType(self):
        for x in self.columns:
            if str(x[1]).startswith("b'datetime'"):
                x[1] = "DateTime"

            elif str(x[1]).startswith("b'decimal"):
                x[1] = "decimal"

            elif str(x[1]).startswith("b'tinyint"):
                x[1] = "bool"

            else:
                x[1] = "string"
