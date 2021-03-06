import os
from lib import action
from python_terraform import *

class Show(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec):
        """
        Provide human-readable output from a state or plan file

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform show command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.show(no_color=IsFlagged)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
	    return (False, output)
