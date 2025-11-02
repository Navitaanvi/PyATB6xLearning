def validate_status_code(response_code):
    if response_code > 0:
        if response_code == 200:
            print("The request is success")
        else:
            print("There is error in the request")

    else:
        print("Error in the request code, Negative request code not allowed")
validate_status_code(200)
validate_status_code(204)
validate_status_code(response_code = 200)
validate_status_code(int(input("Enter the status code: ")))

