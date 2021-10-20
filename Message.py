import os


class MessageModel:
    def __init__(self, path, project):
        self.project = project
        self.model = "Message"
        self.path = path
        self.columns = [
            ['Result', "bool"],
            ["ResultMessage", "string"],
            ["Object", "object"],
            ["ExtraObject", "object"],
            ["IsTimeout", "bool"],
            ["HttpResponseCode", "HttpStatusCode"],
        ]
        self.Create(self.model)

    def Create(self, model):

        if os.path.exists(f"{self.path}/{self.project}/ViewModels"):
            open(f"{self.path}/{self.project}/ViewModels/{model}.cs", "w")

        else:
            os.mkdir(f"{self.path}/{self.project}/ViewModels")
            open(f"{self.path}/{self.project}/ViewModels/{model}.cs", "w")

        self.MessageModel()

    def MessageModel(self):
        viewModelFileData = [
            "using System;\n",
            "using System.Collections.Generic;\n",
            "using System.Linq;\n",
            "using System.Net;\n",
            "using System.Threading.Tasks;\n\n",
            f"namespace {self.project}.ViewModels\n",
            "{\n\t",
            f"public class {self.model}\n",
            "\t{\n",
            "\t\tpublic Message()\n",
            "\t\t{\n",
            "\t\t\tHttpResponseCode = HttpStatusCode.OK;\n\t\t}\n",
            "\t\tpublic Message(bool ResultParam)\n\t\t{\n",
            "\t\t\tResult = ResultParam;\n",
            "\t\t\tHttpResponseCode = HttpStatusCode.OK;\n\t\t}\n"

        ]
        for x in self.columns:
            feild = f"\t\t\t public {x[1]} {x[0]}" + " { get; set; }\n"
            viewModelFileData.append(feild)

        viewModelFileData.append("\t}\n}")

        modelFile = open(f"{self.path}/{self.project}/ViewModels/{self.model}.cs", "w")
        modelFile.writelines(viewModelFileData)
        modelFile.close()
        self.AppSettings()

    def AppSettings(self):
        columns = ["Host", "Port", "SSL", "SMTPUser", "SMTPPassword", "DisplayName", "Subject"]
        viewModelFileData = [
            "using System;\n",
            "using System.Collections.Generic;\n",
            "using System.Linq;\n",
            "using System.Threading.Tasks;\n\n",

            f"namespace {self.project}.ViewModels\n",
            "{\n\t",

            "public class AppSettingsModel\n",
            "\t{\n",
            "\t\tpublic string Secret {get; set;}\n",
            "\t\tpublic EmailSettingsModel EmailSettings {get; set;}\n",
            "\t}\n\t",

            "public class EmailSettingsModel\n",
            "\t{\n"
        ]

        for x in columns:
            feild = f"\t\t public string {x}" + " { get; set; }\n"
            viewModelFileData.append(feild)

        viewModelFileData.append("\t}\n}")

        modelFile = open(f"{self.path}/{self.project}/ViewModels/AppSettingsModel.cs", "w")
        modelFile.writelines(viewModelFileData)
        modelFile.close()
        self.AuthenticationModel()

    def AuthenticationModel(self):
        columns = ["Username", "Password"]

        data = [
            "using System;\n",
            "using System.ComponentModel.DataAnnotations;\n",
            "using System.Collections.Generic;\n",
            "using System.Linq;\n",
            "using System.Threading.Tasks;\n\n",
            f"namespace {self.project}.ViewModels\n",
            "{\n\t",
            "public class AuthenticationModel\n\t{\n",
        ]

        for x in columns:
            feild = "\t\t[Required]\n" + f"\t\t public string {x}" + " { get; set; }\n"
            data.append(feild)

        data.append("\t}\n}")
        modelFile = open(f"{self.path}/{self.project}/ViewModels/AuthenticationModel.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.LoggerService()

    def LoggerService(self):
        data = f"using {self.project}.Contracts;\n" \
               "using NLog;\n" \
               "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Threading.Tasks;\n" \
               f"namespace {self.project}.Common\n" \
               "{\n" \
               "    public class LoggerManager : ILoggerManager\n" \
               "    {\n" \
               "        private static NLog.ILogger logger = LogManager.GetCurrentClassLogger();\n" \
               "        public void LogDebug(string message)\n" \
               "        {\n" \
               "            logger.Debug(message);\n" \
               "        }\n" \
               "        public void LogError(string message)\n" \
               "        {logger.Error(message);}\n" \
               "        public void LogInfo(string message)\n" \
               "        {logger.Info(message);}\n" \
               "        public void LogWarn(string message)\n" \
               "        {logger.Warn(message);\n" \
               "}\n" \
               "}\n" \
               "}\n"
        if not os.path.exists(f"{self.path}/{self.project}/Common"):
            os.mkdir(f"{self.path}/{self.project}/Common")
        modelFile = open(f"{self.path}/{self.project}/Common/LoggerService.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.ILoggerManager()

    def ILoggerManager(self):
        data = "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Threading.Tasks;\n\n" \
               f"namespace {self.project}.Contracts\n" \
               "{\n" \
               "\tpublic interface ILoggerManager\n\t" \
               "{\n" \
               "        void LogInfo(string message);\n" \
               "        void LogWarn(string message);\n" \
               "        void LogDebug(string message);\n" \
               "        void LogError(string message);\n" \
               "\t}\n" \
               "}"

        if not os.path.exists(f"{self.path}/{self.project}/Contracts"):
            os.mkdir(f"{self.path}/{self.project}/Contracts")
        modelFile = open(f"{self.path}/{self.project}/Contracts/ILoggerManager.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.IRepository()

    def IRepository(self):
        data = "using System;" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Linq.Expressions;\n" \
               "using System.Threading.Tasks;\n" \
               "\n" \
               f"namespace {self.project}.Contracts\n" \
               "{\n" \
               "    public interface IRepositoryBase<T>\n" \
               "    {\n" \
               "        IQueryable<T> FindAll();\n" \
               "        IQueryable<T> FindByCondition(Expression<Func<T, bool>> expression);\n" \
               "        void Create(T entity);\n" \
               "        void Update(T entity);\n" \
               "        void Delete(T entity);\n" \
               "\n" \
               "    }\n" \
               "}\n"
        if not os.path.exists(f"{self.path}/{self.project}/Contracts"):
            os.mkdir(f"{self.path}/{self.project}/Contracts")
        modelFile = open(f"{self.path}/{self.project}/Contracts/IRepository.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.IUser()

    def IUser(self):
        data = f"using {self.project}.Models;\n" \
               f"using {self.project}.ViewModels;\n" \
               "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Threading.Tasks;\n\n" \
               f"namespace {self.project}.Contracts\n" \
               "{\n" \
               "    public interface IUser\n" \
               "    {\n" \
               "        UserModel Authenticate(string username, string password);\n" \
               "        Message PostUser(User user);\n" \
               "        Message GetUserById(string id);\n" \
               "        Message GetAll();\n" \
               "    }\n" \
               "}\n"

        if not os.path.exists(f"{self.path}/{self.project}/Contracts"):
            os.mkdir(f"{self.path}/{self.project}/Contracts")
        modelFile = open(f"{self.path}/{self.project}/Contracts/IUser.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.ErrorHandlingFilter()

    def ErrorHandlingFilter(self):
        data = f'using {self.project}.Contracts;\n' \
               'using Microsoft.AspNetCore.Mvc.Filters;\n' \
               'using System;\n' \
               'using System.Collections.Generic;\n' \
               'using System.Linq;\n' \
               'using System.Threading.Tasks;\n\n' \
               f'namespace {self.project}.Filters\n' \
               '{\n' \
               '    public class ErrorHandlingFilter : ExceptionFilterAttribute, IExceptionFilter\n' \
               '    {\n' \
               '        private ILoggerManager _logger;\n' \
               '        public ErrorHandlingFilter(ILoggerManager logger)\n' \
               '        {\n' \
               '            _logger = logger;\n' \
               '        }\n' \
               '        public void OnException(ExceptionContext context)\n' \
               '        {\n' \
               '            HandleExceptionAsync(context);\n' \
               '            context.ExceptionHandled = true;\n' \
               '        }\n' \
               '        private void HandleExceptionAsync(ExceptionContext context)\n' \
               '        {\n' \
               '            _logger.LogError("Exception Message - " + context.Exception.Message);\n' \
               '            _logger.LogError("Exception Details - " + context.Exception.StackTrace);\n' \
               '        }\n' \
               '    }\n' \
               '}'

        if not os.path.exists(f"{self.path}/{self.project}/Filters"):
            os.mkdir(f"{self.path}/{self.project}/Filters")
        modelFile = open(f"{self.path}/{self.project}/Filters/ErrorHandlingFilter.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.ServiceExtensions()

    def ServiceExtensions(self):
        data = f"using {self.project}.Contracts;\n" \
               f"using {self.project}.Repository;\n" \
               f"using {self.project}.ViewModels;\n" \
               "using Microsoft.AspNetCore.Builder;\n" \
               "using Microsoft.Extensions.DependencyInjection;\n" \
               "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Threading.Tasks;\n" \
               f"namespace {self.project}.Common\n" \
               "{\n" \
               "    public static class ServiceExtensions\n" \
               "    {\n" \
               "        public static void ConfigureCors(this IServiceCollection services)\n" \
               "        {\n" \
               "            services.AddCors(options =>\n {\n" \
               + '                options.AddPolicy("CorsPolicy",\n' \
                 '                    builder => builder.AllowAnyOrigin()\n' \
                 '                    .AllowAnyMethod()\n' \
                 '                    .AllowAnyHeader());\n' \
                 '            });\n' \
                 '        }\n' \
                 '        public static void ConfigureIISIntegration(this IServiceCollection services)\n' \
                 '        {\n' \
                 '            services.Configure<IISOptions>(options =>\n' \
                 '            {\n' \
                 '            });\n' \
                 '        }\n' \
                 '        public static void ConfigureLoggerService(this IServiceCollection services)\n' \
                 '        {\n' \
                 '            services.AddScoped<ILoggerManager, LoggerManager>();\n' \
                 '        }\n' \
                 '        public static void ConfigureCustomService(this IServiceCollection services)\n' \
                 '        {\n' \
                 '            services.AddScoped<IUser, UserBO>();\n' \
                 '        }\n' \
                 '    }\n' \
                 '    public static class ExtensionMethods\n' \
                 '    {\n' \
                 '        public static IEnumerable<UserModel> WithoutPasswords(this IEnumerable<UserModel> users)\n' \
                 '        {\n' \
                 '            return users.Select(x => x.WithoutPassword());\n' \
                 '        }\n' \
                 '        public static UserModel WithoutPassword(this UserModel user)\n' \
                 '        {\n' \
                 '            user.Password = null;\n' \
                 '            return user;\n' \
                 '        }\n' \
                 '    }\n' \
                 '}\n'

        if not os.path.exists(f"{self.path}/{self.project}/Common"):
            os.mkdir(f"{self.path}/{self.project}/Common")
        modelFile = open(f"{self.path}/{self.project}/Common/ServiceExtension.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.BaseBO()

    def BaseBO(self):
        data = "using Microsoft.Win32.SafeHandles;\n" \
               "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Runtime.InteropServices;\n" \
               "using System.Threading.Tasks;\n" \
               f"namespace {self.project}.Repository\n" \
               "{\n" \
               "    public class BaseBO : IDisposable\n" \
               "    {\n" \
               "        private bool _disposed = false;\n" \
               "        private SafeHandle _safeHandle = new SafeFileHandle(IntPtr.Zero, true);\n" \
               "        public void Dispose() => Dispose(true);\n" \
               "        protected virtual void Dispose(bool disposing)\n" \
               "        {\n" \
               "            if (_disposed)\n" \
               "            {\n" \
               "                return;\n" \
               "            }\n\n" \
               "            if (disposing)\n" \
               "            {\n" \
               "                  _safeHandle?.Dispose();\n" \
               "            }\n" \
               "            _disposed = true;\n" \
               "        }\n" \
               "    }\n" \
               "}"

        if not os.path.exists(f"{self.path}/{self.project}/Repository"):
            os.mkdir(f"{self.path}/{self.project}/Repository")
        modelFile = open(f"{self.path}/{self.project}/Repository/BaseBO.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.Repository()

    def Repository(self):
        data = f"using {self.project}.Contracts;\n" \
               f"using {self.project}.Models;\n" \
               "using Microsoft.EntityFrameworkCore;\n" \
               "using System;\n" \
               "using System.Collections.Generic;\n" \
               "using System.Linq;\n" \
               "using System.Linq.Expressions;\n" \
               "using System.Threading.Tasks;\n" \
               f"namespace {self.project}.Repository\n" \
               "{\n" \
               "    public abstract class RepositoryBase<T> : IRepositoryBase<T> where T : class\n" \
               "    {\n" \
               f"        protected {self.project}Context agDBContext" \
               " { get; set; }\n" \
               "        //change\n" \
               f"        public RepositoryBase({self.project}Context agContext)\n" \
               "        {\n" \
               "            this.agDBContext = agContext;\n" \
               "        }\n" \
               "        public IQueryable<T> FindAll()\n" \
               "        {\n" \
               "            return this.agDBContext.Set<T>().AsNoTracking();\n" \
               "        }\n" \
               "        public IQueryable<T> FindByCondition(Expression<Func<T, bool>> expression)\n" \
               "        {\n" \
               "            return this.agDBContext.Set<T>().Where(expression).AsNoTracking();\n" \
               "        }\n" \
               "        public void Create(T entity)\n" \
               "        {\n" \
               "            this.agDBContext.Set<T>().Add(entity);\n" \
               "        }\n" \
               "        public void Update(T entity)\n" \
               "        {\n" \
               "            this.agDBContext.Set<T>().Update(entity);\n" \
               "        }\n" \
               "        public void Delete(T entity)\n" \
               "        {\n" \
               "            this.agDBContext.Set<T>().Remove(entity);\n" \
               "        }\n" \
               "    }\n" \
               "}"
        if not os.path.exists(f"{self.path}/{self.project}/Repository"):
            os.mkdir(f"{self.path}/{self.project}/Repository")
        modelFile = open(f"{self.path}/{self.project}/Repository/Repository.cs", "w")
        modelFile.writelines(data)
        modelFile.close()
        self.nlog()

    def nlog(self):
        data = r'<?xml version="1.0" encoding="utf-8" ?><nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"      autoReload="true"      internalLogLevel="Trace"      internalLogFile="F:\NicheBees\AvantGrade\Code\WebApi\Logs\internallog.txt">  <targets>    <target name="logfile" xsi:type="File"            fileName="F:/NicheBees/AvantGrade/Code/WebApi/Logs/${shortdate}_logfile.txt"            layout="${longdate} ${level:uppercase=true} ${message}"/>  </targets>  <rules>    <logger name="*" minlevel="Debug" writeTo="logfile" />  </rules></nlog>'
        # data = "<nlog>?"
        if not os.path.exists(f"{self.path}/{self.project}"):
            os.mkdir(f"{self.path}/{self.project}/")
        modelFile = open(f"{self.path}/{self.project}/nlog.config", "w")
        modelFile.writelines(data)
        modelFile.close()


