import os


class ViewModel:
    def __init__(self, path, model, columns, project):
        self.project = project
        self.path = path
        self.model = model
        self.columns = columns
        self.Create(self.model)

    def Create(self, model):

        if os.path.exists(f"{self.path}/{self.project}/ViewModels"):
            open(f"{self.path}/{self.project}/ViewModels/{model}Model.cs", "w")

        else:
            os.mkdir(f"{self.path}/{self.project}/ViewModels")
            open(f"{self.path}/{self.project}/ViewModels/{model}Model.cs", "w")

        self.Write()

    def Write(self):
        self.DataType()
        viewModelFileData = [
            "using System;\n",
            "using System.Collections.Generic;\n\n",
            "using System.Linq;\n",
            "using System.Threading.Tasks;\n",

            f"namespace {self.project}.ViewModels\n",
            "{\n\t",
            f"public partial class {self.model}Model\n",
            "\t{\n"]
        for x in self.columns:
            feild = f"\t\t public {x[1]} {str(x[0]).title()}" + " { get; set; }\n"
            viewModelFileData.append(feild)

            if str(x[0]).endswith("id"):
                x[0] = str(x[0]).replace("id", "")
                if not x[0] == "":
                    viewModelFileData.append(f"\t\t public {x[1]} {x[0].title()}" + " { get; set; }\n")

        viewModelFileData.append("\t}\n}")

        modelFile = open(f"{self.path}/{self.project}/ViewModels/{self.model}Model.cs", "w")
        modelFile.writelines(viewModelFileData)
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
