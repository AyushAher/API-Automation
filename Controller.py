import copy
import os


class Controller:
    def __init__(self, path, model, columns, project):
        self.project = copy.deepcopy(project)
        self.path = copy.deepcopy(path)
        self.model = str(copy.deepcopy(model)).title()
        self.columns = copy.deepcopy(columns)
        self.Create()

    def Create(self):

        if os.path.exists(f"{self.path}/{self.project}/Controllers"):
            open(f"{self.path}/{self.project}/Controllers/{self.model}Controller.cs", "w")

        else:
            os.mkdir(f"{self.path}/{self.project}/Controllers")
            open(f"{self.path}/{self.project}/Controllers/{self.model}Controller.cs", "w")

        if not (self.model.startswith("Vw_")):

            self.Write()


    def Write(self):
        data = "using Microsoft.AspNetCore.Mvc;\n" \
               "using System.Security.Claims;\n" \
               "using Microsoft.AspNetCore.Authorization;\n" \
               f"using {self.project}.Models;\n" \
               f"using {self.project}.ViewModels;\n\n" \
               f"using {self.project}.Repository;\n\n" \
               "" \
               f"namespace {self.project}.Controllers\n" \
               "{\n" \
               "    [Authorize]\n" \
               '    [Route("api/[controller]")]\n' \
               "    [ApiController]\n" \
               f"    public class {self.model}Controller : ControllerBase\n" \
               "    {\n" \
               f"        private readonly {self.project}Context _context;\n\n" \
               f"        public {self.model}Controller({self.project}Context context)\n" \
               "        {\n" \
               "            _context = context;\n" \
               "        }\n" \
               "    [HttpGet]\n" \
               f"        public ActionResult<Message> Get{self.model}()\n" \
               "        {\n" \
               f"            {self.model}BO obj = new {self.model}BO (_context);\n" \
               f"            return obj.GetAll{self.model}();\n" \
               "        }\n\n" \
               '     [HttpGet("{id}")]\n' \
               f"        public ActionResult<Message> Get{self.model}(string id)\n" \
               "        {\n" \
               f"            {self.model}BO obj = new {self.model}BO(_context);\n" \
               f"            return obj.Get{self.model}(id);\n" \
               "        }\n\n" \
               '        [HttpPut("{id}")]\n' \
               f'        public ActionResult<Message> Put{self.model}(string id, {self.model}Model {self.model.lower()})\n' \
               '        {\n' \
               '            var claimsIdentity = this.User.Identity as ClaimsIdentity;\n' \
               '            var userId = claimsIdentity.FindFirst(ClaimTypes.Name)?.Value;\n\n' \
               f'            {self.model}BO obj = new {self.model}BO(_context);\n' \
               f'            return obj.Update{self.model}({self.model.lower()}, userId);\n' \
               '        }\n' \
               '' \
               '        [HttpPost]\n' \
               f'        public ActionResult<Message> Post{self.model}({self.model}Model {self.model.lower()})\n' \
               '        {\n' \
               '            var claimsIdentity = this.User.Identity as ClaimsIdentity;\n' \
               '            var userId = claimsIdentity.FindFirst(ClaimTypes.Name)?.Value;\n\n' \
               f'            {self.model}BO obj = new {self.model}BO(_context);\n' \
               f'            return obj.Save{self.model}({self.model.lower()}, userId);\n\n' \
               '        }\n' \
               '' \
               '        [HttpDelete("{id}")]\n' \
               f'        public ActionResult<Message> Delete{self.model}(string id)\n' \
               '        {\n' \
               f'            {self.model}BO obj = new {self.model}BO(_context);\n' \
               f'            return obj.Delete{self.model}(id);\n' \
               '        }\n' \
               '    }\n' \
               '}'
        if not os.path.exists(f"{self.path}/{self.project}/Controllers"):
            os.mkdir(f"{self.path}/{self.project}/Controllers")
        modelFile = open(f"{self.path}/{self.project}/Controllers/{self.model}Controller.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
