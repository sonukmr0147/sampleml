import sys
#import traceback

def error_message_details(error,error_detail:sys):
    _, _, exec_tb=error_details.exec_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error meassage [{2}]".format(
        file_name,exec_tb.tb_lineno, str(error)
    )

class CustomException(Exception):
    def __init__(self,error_message, error_detail: sys):
        super.__init__(error_message)
        self.error_message=error_message_details(error_message , error_details=error_detail)
    
    def __str__(self):
        return self.error_message


