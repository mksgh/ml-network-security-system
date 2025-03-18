import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        exc_be, _, exc_tb = error_details.exc_info()

        self.base_exception = exc_be
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        

    def __str__(self):
        return f"{self.base_exception} {self.e}: Error occured in script name [{self.file_name}] at line no. [{self.lineno}] error message [{str(self.error_message)}]"


# if __name__ == "__main__":
#     try:
#         logger.logging.INFO("test")
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)
