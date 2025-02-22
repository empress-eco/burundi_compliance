import requests
import time  # Import the time module
from frappe import _
import frappe
from ..doctype.custom_exceptions import AuthenticationError

class OBRAPIBase:
            
    def __init__(self):
        self.BASE_LOGIN_URL = self.get_api_from_ebims_settings("login")

    '''Confirm if connected to the internet
    if yes, procced with the authentication
    if no, wait for 10 seconds and try again'''
    def check_internet_connection(self):
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def authenticate(self, max_retries=1000):
        retries = 0
        while retries < max_retries:
            if self.check_internet_connection():
                try:
                    
                    return self.authenticate_with_retry()
                except AuthenticationError as auth_error:
                    frappe.log_error(str(auth_error), "Authentication Error")
                    retries += 1
            else:
                frappe.log_error("No internet connection. Retrying...", "Connection Error")
                self.wait_for_internet(delay=5)  # Introduce a delay of 10 seconds
                retries += 1

        raise AuthenticationError("Maximum retries reached. Network issues.")

    def authenticate_with_retry(self):
        auth_details = self.get_auth_details()
        login_url = f"{self.BASE_LOGIN_URL}"
        headers = {"Content-Type": "application/json"}
        data = {"username": auth_details["username"], "password": "|7:%AnXy"}

        try:
            response = requests.post(login_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()

            if result.get("success"):
                return result["result"]["token"]
            else:
                raise AuthenticationError(result["msg"])

        except requests.exceptions.RequestException as e:
            error_message = f"Error during authentication: {str(e)}"
            frappe.log_error(error_message, "OBRAPIBase Authentication Error")
            raise AuthenticationError(error_message)

    def get_auth_details(self):
        ebims_settings = frappe.get_doc("EBIMS Settings")
        auth_details = {
            "username": ebims_settings.username,
            "password": ebims_settings.password,
            "environment": ebims_settings.environment,
            "tp_legal_form": ebims_settings.taxpayers_legal_form,
            "tp_activity_sector": ebims_settings.taxpayers_sector_of_activity,
            "system_identification_given_by_obr": ebims_settings.system_identification_given_by_obr,
            "the_taxpayers_commercial_register_number": ebims_settings.the_taxpayers_commercial_register_number,
            "the_taxpayers_tax_center": ebims_settings.the_taxpayers_tax_center,
            "type_of_taxpayer": ebims_settings.type_of_taxpayer,
        }
        return auth_details

    def get_api_from_ebims_settings(self, method_name):
        ebims_settings = frappe.get_doc("EBIMS Settings")
        for api_row in ebims_settings.get("testing_apis"):
            if api_row.get("method_name") == method_name:
                return api_row.get("api")
        return None

    def wait_for_internet(self, delay=5):
        time.sleep(delay)  # Sleep for 10 seconds
