import copy
import os


class BO():
    def __init__(self, path, model, columns, project):
        self.project = copy.deepcopy(project)
        self.path = copy.deepcopy(path)
        self.model = copy.deepcopy(str(model).title())
        self.columns = copy.deepcopy(columns)

        if os.path.exists(f"{self.path}/{self.project}/Repository"):
            open(f"{self.path}/{self.project}/Repository/{model}BO.cs", "w")

        else:
            os.mkdir(f"{self.path}/{self.project}/Repository")
            open(f"{self.path}/{self.project}/Repository/{model}BO.cs", "w")

        if not (self.model.startswith("Vw_")):
            self.BO(columns)

    def BO(self, columns):
        data0 = [f"using {self.project}.Models;\n",
                 f"using {self.project}.ViewModels;\n",
                 f"using {self.project}.Models;\n",
                 f"using {self.project}.ViewModels;\n",
                 "using Microsoft.EntityFrameworkCore;\n",
                 "using System;\n",
                 "using System.Collections.Generic;\n",
                 "using System.IO;\n",
                 "using System.Linq;\n",
                 "using System.Transactions;\n\n",
                 f"namespace {self.project}.Repository\n",
                 " {\n",
                 f"    public class {self.model}BO\n",
                 "     \n{"
                 f"        public bool {self.model}Exists(string id\n)"
                 "         {\n",
                 f"            return _context.{self.model}.Any(e => e.Id == id)\n;"
                 "         }\n",
                 f"        private readonly {self.project}Context _context;\n",
                 f"        {self.model}DL dObj;\n",
                 f"        public {self.model}BO ({self.project}Context context)\n",
                 "         {\n",
                 "            _context = context;\n",
                 "          }\n",
                 f"        public Message Get{self.model}(string id)\n",
                 "         {\n",
                 "            Message result = new Message();\n",
                 f"            if ({self.model}Exists(id))\n",
                 "            {\n",
                 f"                dObj = new {self.model}DL(_context);\n",
                 f"                result.Object = dObj.Get{self.model}ById(id);\n",
                 "                 result.Result = true; \n",
                 "            }\n",
                 "            else\n",
                 "            {\n",
                 "                result.Object = null;\n",
                 "                result.Result = false;\n",
                 '                result.ResultMessage = "Record does not exists!";\n',
                 "            }\n",
                 "            return result\n;"
                 "          }\n",
                 f"        public Message GetAll{self.model}()\n",
                 "        {\n",
                 "            Message result = new Message();\n",
                 f"            dObj = new {self.model}DL(_context); \n",
                 f"           result.Object = dObj.GetAll{self.model}();\n",
                 "            result.Result = true;\n",
                 "           return result;\n",
                 "        }\n",

                 f"        public Message Update{self.model}({self.model}Model m{str(self.model).lower()}, string userId\n)"
                 "        \n{"
                 f"            dObj = new {self.model}DL(_context);\n"
                 f"            return dObj.Update{self.model}(m{str(self.model).lower()}, userId);\n"
                 "        \n}\n"

                 f"       public Message Save{self.model}({self.model}Model m{self.model}, string userId\n)"
                 "       \n{"
                 f"            dObj = new {self.model}DL(_context);\n"
                 f"            return dObj.Save{self.model}(m{self.model}, userId);\n"
                 "        }\n",
                 f"        public Message Delete{str(self.model)}(string id\n)"
                 "        \n{"
                 "            Message result = new Message()\n;"
                 f"            dObj = new {str(self.model)}DL(_context);\n"
                 f"            if (dObj.Delete{str(self.model)}(id)\n)"
                 "            \n{"
                 "                result.Result = true;\n"
                 f'                result.ResultMessage = "{str(self.model)} deleted successfully.";\n'
                 '            \n}'
                 "           else\n"
                 "            {\n"
                 "                result.Result = false;\n"
                 '                result.ResultMessage = "Some error ocurred. Please contact system administrator.";\n'
                 '            }\n',
                 '\n',
                 '            return result;\n',
                 '        }\n',
                 '    }\n',

                 f'    public class {str(self.model)}DL\n',
                 '    {\n',
                 f'        private readonly {str(self.project)}Context _context;\n',
                 f'        public {str(self.model)}DL({str(self.project)}Context context)\n',
                 '        {\n',
                 '            _context = context;\n',
                 '        }\n',
                 '\n',
                 f'        public List<{str(self.model)}Model> GetAll{str(self.model)}()\n',
                 '        {\n',
                 f'            List<{str(self.model)}Model> lst{str(self.model)} = new List<{str(self.model)}Model> ();\n',
                 f'            var {str(self.model).lower()} = _context.{str(self.model)}.ToList();\n',
                 f'            foreach ({str(self.model)}  {str(self.model)[0:2]} in {str(self.model).lower()})\n',
                 '            {\n',
                 f'                lst{str(self.model)}.Add(Get{str(self.model)}({str(self.model)[0:2]}));\n',
                 '            }\n',
                 '\n',
                 f'            return lst{str(self.model)};\n',
                 '        }\n',
                 '\n',
                 '\n',
                 f'        public {str(self.model)}Model Get{str(self.model)}({str(self.model)} {str(self.model).lower()})\n',
                 '        {\n',
                 '\n',
                 f'            {str(self.model)}Model m{str(self.model)} = new {str(self.model)}Model()\n',
                 '            {\n'
                 ]
        # data1
        data2 = ['            };\n',
                 f'            return m{str(self.model)};\n',
                 '        }\n',
                 '\n',
                 f'        public {str(self.model)}Model Get{str(self.model)}ById(string id)\n',
                 '        {\n',
                 f'            var {str(self.model).lower()} = _context.{str(self.model)}.Where(x => x.Id == id).FirstOrDefault();\n',
                 f'            return Get{str(self.model)}({str(self.model).lower()});\n',
                 '        }\n',

                 f'        public Message Update{str(self.model)}({str(self.model)}Model {str(self.model).lower()}, string userId)\n',
                 '        {\n',
                 '            Message result = new Message();\n',
                 '            try\n',
                 '            {\n',

                 f'                var m{str(self.model)} = _context.{str(self.model)}.Where(x => x.Id == {str(self.model).lower()}.Id).FirstOrDefault();\n',
                 f'                if (m{str(self.model)} != null)\n',
                 '                {\n',
                 ]
        # f'                    mProductDetails.Manufacturer = productDetails.ManufacturerId;\n',
        data3 = ['\n',
                 f'                    _context.Entry(m{str(self.model)}).State = EntityState.Modified;\n',
                 '                    _context.SaveChanges();\n',
                 '                    result.Result = true;\n',
                 f'                    result.ResultMessage = "{str(self.model).title()} updated successfully.";\n',
                 '                }\n',
                 '            }\n',
                 '            catch (Exception e)\n',
                 '            {\n',
                 '                result.Result = false;\n',
                 '                result.ResultMessage = "Some error ocurred. Please contact system administrator.";\n',
                 '            }\n',
                 '\n',
                 '            return result;\n',
                 '        }\n',
                 '\n',
                 f'        public Message Save{str(self.model)}({str(self.model)}Model {str(self.model).lower()}, string userId)\n',
                 '        {\n',
                 '            Message result = new Message();\n',
                 '            try\n',
                 '            {\n',
                 f'                if (!{str(self.model)}Exists({str(self.model).lower()}.Id ))\n',
                 '                {\n',

                 f'                    {str(self.model)} m{str(self.model)} = new {str(self.model)}()\n',
                 '                    {\n',
                 ]
        # data1
        data4 = ['                    };\n',
                 '\n',
                 f'                    _context.{str(self.model)}.Add(m{str(self.model)});\n',
                 '                    _context.SaveChanges();\n',
                 '\n',
                 f'                    result.Object = m{str(self.model)};\n',
                 '                    result.Result = true;\n',
                 f'                    result.ResultMessage = "{str(self.model).title()} updated successfully.";\n',
                 '                }\n',
                 '                else\n',
                 '                {\n',
                 '                    result.Result = false;\n',
                 f'                    result.ResultMessage = "{str(self.model).title()} already exists.";\n',
                 '                }\n',
                 '            }\n',
                 '            catch (Exception e)\n',
                 '            {\n',
                 '                result.Result = false;\n',
                 f'                result.ResultMessage = "Some error ocurred. Please contact system administrator." ;\n',
                 '            }\n',
                 '\n',
                 '            return result;\n',
                 '        }\n',
                 '\n',
                 f'        public bool Delete{str(self.model)}(string id)\n',
                 '        {\n',
                 '            try\n',
                 '            {\n',
                 '                using (TransactionScope trans = new TransactionScope())\n',
                 '                {\n',
                 f'                    var {str(self.model).lower()}= _context.{str(self.model)}.Find(id);\n',
                 f'                    _context.{self.model}.Remove({str(self.model).lower()});\n',
                 '\n',
                 '                    _context.SaveChanges();\n',
                 '                    trans.Complete();\n',
                 '                }\n',
                 '                return true;\n',
                 '            }\n',
                 '            catch (Exception)\n',
                 '            {\n',
                 '                return false;\n',
                 '            }\n',
                 '        }\n',
                 '\n',
                 f'        public bool {self.model}Exists(string id)\n',
                 '        {\n',
                 f'            return _context.{self.model}.Any(e => e.Id == id );\n',
                 '        }\n',
                 '    }\n',
                 '}\n',
                 ]
        # common one
        savedata = []
        for y in columns:
            feild = f" {str(y[0]).title()} = {self.model.lower()}.{str(y[0]).title()}, \n"
            savedata.append(feild)
        if not os.path.isfile(f"{self.path}/{self.project}/Repository/{self.model}BO.cs"):
            open(f"{self.path}/{self.project}/Repository/{self.model}BO.cs", "x")
            modelFile = open(f"{self.path}/{self.project}/Repository/{self.model}BO.cs", "a")
        else:
            modelFile = open(f"{self.path}/{self.project}/Repository/{self.model}BO.cs", "a")

        getdata = []
        for a in self.columns:
            x = copy.deepcopy(a)
            feild = f" {str(x[0]).title()} = {self.model.lower()}.{str(x[0]).title()}, \n"
            getdata.append(feild)

            if str(x[0]).endswith("id"):
                x[0] = str(x[0]).replace("id", "")
                if not x[0] == "" and x[0] in self.model:
                    getdata.append(
                        f" {x[0].title()} = _context.{self.model}.Where(x => x.Id == {self.model.lower()}.{x[0].title()}id).FirstOrDefault(), \n")

                if not (x[0] == "" and x[0] in self.model):
                    getdata.append(
                        f"{x[0].title()} = _context.Vw_Listitems.Where(x => x.Listtypeitemid == {self.model.lower()}.{x[0].title()}id).FirstOrDefault().Itemname,\n")

        # uncommon one
        updatedata = []
        for a in self.columns:
            x = copy.deepcopy(a)
            feild = f"m{self.model.title()}.{str(x[0]).title()} = {self.model.lower()}.{str(x[0]).title()}; \n"
            updatedata.append(feild)

        modelFile.writelines(data0)
        modelFile.writelines(getdata)
        modelFile.writelines(data2)
        modelFile.writelines(updatedata)
        modelFile.writelines(data3)
        modelFile.writelines(savedata)
        modelFile.writelines(data4)
