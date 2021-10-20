import copy
import os
import time

import mysql.connector as sql

import BO
import Controller
import Message
import Model
import ViewModel


class Main:

    def __init__(self):
        self.database = input("Database Name: ")
        self.databaseHost = input("Database Host: ")
        self.databaseUser = input("Database User: ")
        self.databasePassword = input("Database Password: ")
        self.path = input("Full path of Location Folder: ")
        self.projectname = input("Project Name: ")

        # self.database = "agpc_prod"
        # self.databaseHost = "localhost"
        # self.databaseUser = "root"
        # self.databasePassword = "ayushaher"
        # self.path = "G:\Projects\.Net\API"
        # self.projectname = "Auto"
        # self.projectname = f"{self.projectname}API"

        try:
            db = sql.connect(
                host=self.databaseHost,

                user=self.databaseUser,
                password=self.databasePassword,
                auth_plugin='mysql_native_password',
            )
            self.mycursor = db.cursor()
            self.mycursor.execute("SHOW DATABASES")
            lstdatabase = self.mycursor.fetchall()
            databaseExists = False

            for d in lstdatabase:
                if self.database in d:
                    databaseExists = True

            if databaseExists:
                self.mycursor.execute(f"USE {self.database}")
                if not os.path.exists(f"{self.path}/{self.projectname}"):
                    os.mkdir(f"{self.path}/{self.projectname}")
                    os.mkdir(f"{self.path}/{self.projectname}/Models")
                    self.context = f"{self.path}/{self.projectname}/Models/{self.projectname}Context.cs"
                else:
                    self.context = f"{self.path}/{self.projectname}/Models/{self.projectname}Context.cs"
                self.CreateContext()
            else:
                print("Database Does Not Exists")
        except Exception as e:
            print("Error Occurred", e)

    def CreateContext(self):
        contextList = [
            "using System;\n",
            "using Microsoft.EntityFrameworkCore;\n",
            "using Microsoft.EntityFrameworkCore.Metadata;\n",
            f"using {self.projectname}.Models;\n",
            f"namespace {self.projectname}.Models\n",
            "{\n",
            f"public partial class {self.projectname}Context : DbContext\n ", "{\n"
                                                                              f"public {self.projectname}Context(DbContextOptions<{self.projectname}Context> options)\n",
            ": base(options){}\n"]
        Message.MessageModel(self.path, self.projectname)
        columnlist = []

        self.mycursor.execute("SHOW TABLES")
        if not os.path.isfile(f"{self.path}/{self.projectname}/Models/{self.projectname}Context.cs"):
            open(f"{self.path}/{self.projectname}/Models/{self.projectname}Context.cs", "x")
        else:
            open(f"{self.path}/{self.projectname}/Models/{self.projectname}Context.cs", "w")
        for x in self.mycursor.fetchall():
            x = str(x).replace("(", "").replace("'", "").replace(",", "").replace(")", "").title()
            self.mycursor.execute(f"show columns from `{x}`")
            lstColumns = self.mycursor.fetchall()
            contextDef = ("public virtual DbSet<" + x + "> " + x + " { get; set; }\n")
            contextList.append(contextDef)

            for columns in lstColumns:
                columnlist.append(list(columns[0:2]))

            ListColumns = copy.deepcopy(columnlist)
            ListModel = copy.deepcopy(x)

            ListColumns0 = copy.deepcopy(columnlist)
            ListModel0 = copy.deepcopy(x)

            ListColumns1 = copy.deepcopy(columnlist)
            ListModel1 = copy.deepcopy(x)

            ListColumns2 = copy.deepcopy(columnlist)
            ListModel2 = copy.deepcopy(x)

            Model.Model(self.path, ListModel, ListColumns, self.projectname)
            BO.BO(self.path, ListModel0, ListColumns0, self.projectname)
            ViewModel.ViewModel(self.path, ListModel1, ListColumns1, self.projectname)
            Controller.Controller(self.path, ListModel2, ListColumns2, self.projectname)

            columnlist.clear()

        contextList.append("}\n}")
        self.WriteContextFile(contextList)

    def WriteContextFile(self, contextList):
        contextFile = open(self.context, "w")
        contextFile.writelines(contextList)
        contextFile.close()


start = time.time()
Main()
end = time.time()
totaltime = round(float(end - start), 4)
print("-"*100)
print("Note:")
print("\t 1. UserBO.cs and ServiceExtension.cs files should be Edited before running the code ")
print("\t 2. Controller and BO for Views are not automated ")
print("-"*100)


input("Press any Key to exit")
